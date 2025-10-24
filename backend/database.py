import pandas as pd
import os

def carregar_dados(caminho, colunas):
    # Se o arquivo não existir, cria um DataFrame vazio com colunas
    if not os.path.exists(caminho):
        df = pd.DataFrame(columns=colunas)
        df.to_csv(caminho, index=False)
        return df

    # Tenta ler o arquivo; se estiver vazio, recria
    try:
        return pd.read_csv(caminho)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=colunas)
        df.to_csv(caminho, index=False)
        return df


def salvar_dados(df, caminho):
    df.to_csv(caminho, index=False)
