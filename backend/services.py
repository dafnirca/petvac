from backend.database import carregar_dados, salvar_dados, COLUNAS
from backend.pet import Pet
import pandas as pd
from datetime import datetime

"""
def cadastrar_pet_service(nome, especie, raca, dataNascimento, idTutor):
    colunas = ["idPet", "nome", "especie", "raca", "dataNascimento", "idTutor"]
    df_pets = carregar_dados("data/pets.csv", colunas)

    novo_id = len(df_pets) + 1
    novo_pet = {
        "idPet": novo_id,
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "dataNascimento": str(dataNascimento),
        "idTutor": idTutor
    }

    df_pets = df_pets._append(novo_pet, ignore_index=True)  # pandas >= 2.0 usa _append
    salvar_dados(df_pets, "data/pets.csv")

    return "Pet cadastrado com sucesso!"
"""

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