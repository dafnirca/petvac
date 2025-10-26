import pandas as pd
import os

def carregar_dados(caminho, colunas):
    if not os.path.exists(caminho):
        df = pd.DataFrame(columns=colunas)
        df.to_csv(caminho, index=False)
        return df
    try:
        return pd.read_csv(caminho)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=colunas)
        df.to_csv(caminho, index=False)
        return df

def salvar_dados(df, caminho):
    df.to_csv(caminho, index=False)

COLUNAS = {
    "pets": ["idPet", "nome", "especie", "raca", "dataNascimento", "idTutor"],
    "tutores": ["idTutor", "nome", "telefone", "email", "endereco"],
    "vacinas": ["idVacina", "idPet", "nome", "dataAplicacao", "dataProximaDose", "status"],
    "usuarios": ["idUsuario", "nome", "cargo"],
    "notificacoes": ["idNotificacao", "mensagem", "dataEnvio", "status"]
}
