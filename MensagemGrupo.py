from Mensagem import Mensagem

class MensagemGrupo(Mensagem):
    def __init__(self, remetente, conteudo):
        super().__init__(remetente, conteudo)
        self.lida_por = []

    def marcar_como_lida(self, usuario):
        if usuario.email not in self.lida_por:
            self.lida_por.append(usuario.email)