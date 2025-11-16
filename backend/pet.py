class Pet:
    def __init__(self, idPet, nome, especie, raca, dataNascimento, idTutor):
        self.idPet = idPet
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.dataNascimento = dataNascimento
        self.idTutor = idTutor

    def atualizar_pet(self, df_pets, novos_dados):
        for key, value in novos_dados.items():
            if key in df_pets.columns:
                df_pets.loc[df_pets["idPet"] == self.idPet, key] = value
        return df_pets
