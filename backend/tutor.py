class Tutor:
    def __init__(self, idTutor, nome, telefone, email, endereco):
        self.idTutor = idTutor
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def atualizar_tutor(self, df_tutores, novos_dados):
        for key, value in novos_dados.items():
            if key in df_tutores.columns:
                df_tutores.loc[df_tutores["idTutor"] == self.idTutor, key] = value
        return df_tutores
    