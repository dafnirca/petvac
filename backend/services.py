from backend.database import carregar_dados, salvar_dados, COLUNAS
from backend.pet import Pet
from backend.tutor import Tutor
from backend.vacina import Vacina
from backend.historico_vacinas import HistoricoVacinas

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
def registrar_vacina(idPet, nome, dataAplicacao, dataProximaDose, status="aplicada"):
    df = carregar_dados("data/vacinas.csv", COLUNAS["vacinas"])
    novo_id = len(df) + 1
    vacina = Vacina(novo_id, idPet, nome, dataAplicacao, dataProximaDose, status)
    df = df._append(vars(vacina), ignore_index=True)
    salvar_dados(df, "data/vacinas.csv")
    return "Vacina registrada com sucesso!"

def consultar_vacinas_pendentes():
    df = carregar_dados("data/vacinas.csv", COLUNAS["vacinas"])
    if df.empty:
        return pd.DataFrame()
    hoje = datetime.now().date()
    df["dataProximaDose"] = pd.to_datetime(df["dataProximaDose"], errors="coerce").dt.date
    pendentes = df[df["dataProximaDose"] <= hoje]
    return pendentes

def consultar_historico_pet(idPet):
    df_vacinas = carregar_dados("data/vacinas.csv", COLUNAS["vacinas"])
    historico = df_vacinas[df_vacinas["idPet"] == idPet]
    if historico.empty:
        return "Nenhum registro de vacina para este pet."
    return historico

