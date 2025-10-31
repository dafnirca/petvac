class HistoricoVacinas:
    def __init__(self, idHistorico, idPet):
        self.idHistorico = idHistorico
        self.idPet = idPet
        self.listaVacinas = []

    def adicionar_vacina(self, vacina):
        self.listaVacinas.append(vacina)

    def consultar_historico(self):
        if not self.listaVacinas:
            return "Nenhuma vacina registrada para este pet."
        return [vars(v) for v in self.listaVacinas]