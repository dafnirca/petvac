class Usuario:
    def __init__(self, idUsuario, nome, cargo: {"recepcionista", "veterinario","tutor"}):
        self.idUsuario = idUsuario
        self.nome = nome
        self.cargo = cargo
        self.logado = False
    
    def login(self):
        if self.logado:
            return f"{self.nome} já está logado."
        
        self.logado = True
        return f"{self.nome} login realizado."

    def logout(self):
        if not self.logado:
            return f"{self.nome} já está deslogado."
        
        self.logado = False
        return f"{self.nome} logout realizado."