class Mensagem:
    def __init__(self, remetente, conteudo):
        self.remetente = remetente
        self.conteudo = conteudo
        self.reacoes = []
        self.fixada = False
        self.expira_em = None

    def add_reacao(self, reacao):
        self.reacoes.append(reacao)

    def fixar(self):
        self.fixada = True

    def definir_tempo_expiracao(self, segundos):
        import time
        self.expira_em = time.time() + segundos

    def expirou(self):
        import time
        return self.expira_em is not None and time.time() >= self.expira_em

    def formatar_reacoes(self):
        if not self.reacoes:
            return ""
        return " (" + " ".join(self.reacoes) + " )"

    def exibir(self, indice=None):
        prefixo = f"{indice} - " if indice is not None else ""
        fixada = "[FIXADA] " if self.fixada else ""
        print(f"{fixada}{prefixo}{self.remetente.email}: {self.conteudo}{self.formatar_reacoes()}")