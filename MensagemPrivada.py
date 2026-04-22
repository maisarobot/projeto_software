from Mensagem import Mensagem

class MensagemPrivada(Mensagem):
    def __init__(self, remetente, conteudo):
        super().__init__(remetente, conteudo)
        self.visualizada = False

    def marcar_como_visualizada(self):
        self.visualizada = True