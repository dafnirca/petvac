from backend.database import carregar_dados, salvar_dados

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
