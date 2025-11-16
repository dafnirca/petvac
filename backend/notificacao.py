from datetime import datetime

class Notificacao:
    def __init__(self, idNotificacao, mensagem):
        self.idNotificacao = idNotificacao
        self.mensagem = mensagem
        self.dataEnvio = None
        self.status = "pendente"

    def enviarNotificacao(self):
        if self.status == "pendente":
            self.status = "enviada"
            self.dataEnvio = datetime.now().strftime("%d/%m %H:%M")
            return f"Notificação {self.idNotificacao} enviada."
        else:
            return "Notificação já foi enviada."
        

    def marcarComoLida(self):
        self.status = "Lida"
        return