class Pet:
    def __init__(self, idPet, nome, especie, raca, dataNascimento, idTutor):
        self.idPet = idPet
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.dataNascimento = dataNascimento
        self.idTutor = idTutor

    def cadastrar_pet(self, df_pets):
        novo_pet = {
            "idPet": self.idPet,
            "nome": self.nome,
            "especie": self.especie,
            "raca": self.raca,
            "dataNascimento": self.dataNascimento,
            "idTutor": self.idTutor
        }
        df_pets = df_pets.append(novo_pet, ignore_index=True)
        return df_pets
