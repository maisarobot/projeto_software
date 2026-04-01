class Usuario: 
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.logado = False

    def login(self, email, senha):
        if self.email == email and self.senha == senha:
            self.logado = True
            print("Login realizado")
        else:
            print("Erro no login")


class Mensagem:
    def __init__(self, remetente, conteudo):
        self.remetente = remetente
        self.conteudo = conteudo
        self.reacoes = []
        self.fixada = False

    def add_reacao(self, reacao):
        self.reacoes.append(reacao)

    def fixar(self):
        self.fixada = True


class MensagemGrupo(Mensagem):
    def __init__(self, remetente, conteudo):
        super().__init__(remetente, conteudo)
        self.lida_por = []

    def marcar_como_lida(self, usuario):
        self.lida_por.append(usuario.email)

    def mostrar_lidos(self):
        print(f"Mensagem '{self.conteudo}' lida por: ", self.lida_por)


class MensagemPrivada(Mensagem):
    def __init__(self, remetente, conteudo):
        super().__init__(remetente, conteudo)
        self.visualizada = False


class Chat:
    def __init__(self):
        self.mensagens = []

    def enviar_mensagem(self, mensagem):
        self.mensagens.append(mensagem)

    def listar_mensagens(self):
        for m in self.mensagens:
            print(f"{m.remetente.email}: {m.conteudo}")


class ChatIndividual(Chat):
    def __init__(self, usuario1, usuario2):
        super().__init__()
        self.usuario1 = usuario1
        self.usuario2 = usuario2


class Grupo(Chat):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.membros = []

    def add_membro(self, usuario):
        self.membros.append(usuario)

    def mencionar_todos(self):
        print("@todos", [u.email for u in self.membros])

class Enquete:
    def __init__(self, pergunta):
        self.pergunta = pergunta
        self.votos = {}

    def votar(self, usuario, opcao):
        self.votos[usuario.email] = opcao

    def resultado(self):
        print(self.votos)


class Evento:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
        self.status = "programado"

    def cancelar(self):
        self.status = "cancelado"



u1 = Usuario("fulano@email.com", "123")
u2 = Usuario("beltrano@email.com", "456")
u3 = Usuario("cicrano@email.com", "789")

grupo = Grupo("Amigos")
grupo.add_membro(u1)
grupo.add_membro(u2)
grupo.add_membro(u3)

msg = MensagemGrupo(u1, "tomara q funcione")
msg2 = MensagemGrupo(u3, "funcionou")

grupo.enviar_mensagem(msg)
grupo.enviar_mensagem(msg2)

msg.marcar_como_lida(u2)
msg.marcar_como_lida(u3)
msg2.marcar_como_lida(u1)

grupo.listar_mensagens()
grupo.mencionar_todos()
msg.mostrar_lidos()
msg2.mostrar_lidos()





