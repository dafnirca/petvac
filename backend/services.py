from backend.database import carregar_dados, salvar_dados, COLUNAS
from backend.pet import Pet
from backend.tutor import Tutor
from backend.vacina import Vacina
from backend.usuario import Usuario
from backend.historico_vacinas import HistoricoVacinas
from backend.notificacao import Notificacao

from datetime import date, datetime
import pandas as pd
from datetime import datetime

# ---------- PETS ----------

def cadastrar_pet(nome, especie, raca, dataNascimento, idTutor):
    df = carregar_dados("data/pets.csv", COLUNAS["pets"])
    novo_id = len(df) + 1
    pet = Pet(novo_id, nome, especie, raca, dataNascimento, idTutor)
    df = df._append(vars(pet), ignore_index=True)
    
    salvar_dados(df, "data/pets.csv")
    return "Pet cadastrado com sucesso!"

def atualizar_pet(idPet, novos_dados):
    df = carregar_dados("data/pets.csv", COLUNAS["pets"])
    pet = Pet(idPet, None, None, None, None, None)
    df = pet.atualizar_pet(df, novos_dados)
    
    salvar_dados(df, "data/pets.csv")
    return "Pet atualizado com sucesso!"

def listar_pets():
    return carregar_dados("data/pets.csv", COLUNAS["pets"])


# ---------- TUTORES ----------

def cadastrar_tutor(nome, telefone, email, endereco):
    df = carregar_dados("data/tutores.csv", COLUNAS["tutores"])
    novo_id = len(df) + 1
    tutor = Tutor(novo_id, nome, telefone, email, endereco)
    df = df._append(vars(tutor), ignore_index=True)
    
    salvar_dados(df, "data/tutores.csv")
    return "Tutor cadastrado com sucesso!"

def atualizar_tutor(idTutor, novos_dados):
    df = carregar_dados("data/tutores.csv", COLUNAS["tutores"])
    tutor = Tutor(idTutor, None, None, None, None)
    df = tutor.atualizar_tutor(df, novos_dados)
    
    salvar_dados(df, "data/tutores.csv")
    return "Tutor atualizado com sucesso!"

def listar_tutores():
    return carregar_dados("data/tutores.csv", COLUNAS["tutores"])


# ---------- VACINAS E HISTÓRICO ----------
def registrar_vacina(idPet, nome, dataAplicacao=None, dataProximaDose=None):
    """
    dataAplicacao pode ser: None, datetime.date, datetime.datetime ou string 'YYYY-MM-DD'
    dataProximaDose idem.
    Regra de status:
      - se dataAplicacao é None -> pendente
      - se dataAplicacao <= hoje -> aplicada
      - se dataAplicacao > hoje -> pendente (aplicacao agendada)
    """
    df = carregar_dados("data/vacinas.csv", COLUNAS["vacinas"])
    novo_id = len(df) + 1

    def to_date_or_none(v):
        if v is None:
            return None
        if isinstance(v, date):
            return v
        try:
            return pd.to_datetime(v, errors="coerce").date()
        except Exception:
            return None

    dataAplicacao_date = to_date_or_none(dataAplicacao)
    dataProximaDose_date = to_date_or_none(dataProximaDose)

    hoje = datetime.now().date()

    if dataAplicacao_date is None:
        status = "pendente"
    else:
        # se a aplicação ocorreu hoje ou antes -> aplicada
        if dataAplicacao_date <= hoje:
            status = "aplicada"
        else:
            # aplicação informada para o futuro -> é um agendamento
            status = "pendente"

    vacina = {
        "idVacina": novo_id,
        "idPet": idPet,
        "nome": nome,
        "dataAplicacao": str(dataAplicacao_date) if dataAplicacao_date else "",
        "dataProximaDose": str(dataProximaDose_date) if dataProximaDose_date else "",
        "status": status
    }

    df = df._append(vacina, ignore_index=True)
    salvar_dados(df, "data/vacinas.csv")
    return "Vacina registrada com sucesso!"


def consultar_vacinas_pendentes():
    df = carregar_dados("data/vacinas.csv", COLUNAS["vacinas"])
    if df.empty:
        return pd.DataFrame()
    
    # Hoje como Timestamp
    hoje = pd.Timestamp.now().normalize()

    # Converter TODAS as datas para Timestamp (sem .dt.date)
    df["dataProximaDose"] = pd.to_datetime(df["dataProximaDose"], errors="coerce")
    df["dataAplicacao"] = pd.to_datetime(df["dataAplicacao"], errors="coerce")

    # Filtrar apenas pendentes
    pendentes = df[df["status"] == "pendente"].copy()

    # Atrasada = próxima dose < hoje
    pendentes["atrasada"] = pendentes["dataProximaDose"] < hoje

    return pendentes



def consultar_historico_pet(idPet):
    df = carregar_dados("data/vacinas.csv", COLUNAS["vacinas"])

    historico = df[df["idPet"] == idPet]

    if historico.empty:
        return "Nenhum registro de vacina para este pet."

    historico["dataAplicacao"] = pd.to_datetime(historico["dataAplicacao"], errors="coerce")
    historico["dataProximaDose"] = pd.to_datetime(historico["dataProximaDose"], errors="coerce")

    historico = historico.sort_values(by=["dataAplicacao", "dataProximaDose"], ascending=True)

    return historico


def aplicar_dose(idVacina, dataAplicacao, dataProximaDose=None):
    df = carregar_dados("data/vacinas.csv", COLUNAS["vacinas"])

    # Seleciona a vacina pendente que será aplicada
    vacina_antiga = df[df["idVacina"] == idVacina]

    if vacina_antiga.empty:
        return "Vacina não encontrada."

    idPet = int(vacina_antiga.iloc[0]["idPet"])
    nome = vacina_antiga.iloc[0]["nome"]

    # Atualiza o status da vacina antiga
    df.loc[df["idVacina"] == idVacina, "status"] = "concluída"

    # Registra nova dose aplicada como novo registro
    novo_id = len(df) + 1
    novo_registro = {
        "idVacina": novo_id,
        "idPet": idPet,
        "nome": nome,
        "dataAplicacao": str(dataAplicacao),
        "dataProximaDose": str(dataProximaDose) if dataProximaDose else None,
        "status": "aplicada"
    }

    df = df._append(novo_registro, ignore_index=True)

    salvar_dados(df, "data/vacinas.csv")
    return "Dose aplicada com sucesso!"


# ---------- LOGIN ----------

def login_usuario(nome, senha, cargo):
    df = carregar_dados("data/usuarios.csv", COLUNAS["usuarios"])

    if df.empty:
        return False, "❌ Não há usuários cadastrados."

    # Normalização forte dos inputs
    nome_norm = nome.strip().lower()
    senha_norm = senha.strip()
    cargo_norm = cargo.strip().lower()

    # Criar colunas normalizadas apenas em memória
    df["nome_norm"] = df["nome"].astype(str).str.strip().str.lower()
    df["cargo_norm"] = df["cargo"].astype(str).str.strip().str.lower()
    df["senha_norm"] = df["senha"].astype(str).str.strip()

    match_index = df[
        (df["nome_norm"] == nome_norm) &
        (df["senha_norm"] == senha_norm) &
        (df["cargo_norm"] == cargo_norm)
    ].index

    if match_index.empty:
        return False, "❌ Usuário ou senha inválidos."

    # Marca como logado
    index = match_index[0]
    df.loc[index, "logado"] = True

    # ⚠️ REMOVE colunas normalizadas antes de salvar
    df = df.drop(columns=["nome_norm", "cargo_norm", "senha_norm"])

    salvar_dados(df, "data/usuarios.csv")

    return True, f"Login realizado com sucesso! Bem-vindo(a), {df.loc[index, 'nome']}."


def cadastrar_usuario(nome, senha, cargo):
    df = carregar_dados("data/usuarios.csv", COLUNAS["usuarios"])

    novo_id = len(df) + 1

    novo_usuario = {
        "idUsuario": novo_id,
        "nome": nome,
        "senha": senha,
        "cargo": cargo
    }

    df = df._append(novo_usuario, ignore_index=True)
    salvar_dados(df, "data/usuarios.csv")

    return True, "Usuário cadastrado com sucesso!"


def logout_usuario(nome, senha, cargo):
    df = carregar_dados("data/usuarios.csv", COLUNAS["usuarios"])

    if df.empty:
        return "⚠️ Nenhum usuário cadastrado."

    if "logado" not in df.columns:
        return "⚠️ Nenhum usuário está logado atualmente."

    # busca por nome + cargo
    match_index = df[
        (df["nome"].str.strip().str.lower() == nome.strip().lower()) &
        (df["senha"] == senha) &
        (df["cargo"].str.strip().str.lower() == cargo.strip().lower())
    ].index

    if match_index.empty:
        return "❌ Usuário não encontrado para logout."

    index = match_index[0]

    df.loc[index, "logado"] = False
    salvar_dados(df, "data/usuarios.csv")

    return f"👋 Logout realizado. Até logo, {nome}!"


# ---------- NOTIFICAÇÕES ----------
def gerar_notificacoes_pendentes():
    vacinas = consultar_vacinas_pendentes()
    if vacinas.empty:
        return "Nenhuma vacina pendente."
    df_not = carregar_dados("data/notificacoes.csv", COLUNAS["notificacoes"])
    count = 0
    for _, v in vacinas.iterrows():
        msg = f"Vacina '{v['nome']}' do pet {v['idPet']} está pendente!"
        notificacao = Notificacao(len(df_not) + 1, msg, datetime.now().strftime("%Y-%m-%d"), "pendente")
        df_not = df_not._append(vars(notificacao), ignore_index=True)
        count += 1
    salvar_dados(df_not, "data/notificacoes.csv")
    return f"{count} notificações geradas."

def marcar_notificacao_como_lida(idNotificacao):
    df = carregar_dados("data/notificacoes.csv", COLUNAS["notificacoes"])
    df.loc[df["idNotificacao"] == idNotificacao, "status"] = "lida"
    salvar_dados(df, "data/notificacoes.csv")
    return f"Notificação {idNotificacao} marcada como lida."