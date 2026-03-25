class Usuario: 
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.logado = False

    def __login__(self, email, senha):
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

    def __add_reacao__(self, reacao):
        self.reacoes.append(reacao)

    def fixar(self):
        self.fixada = True



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
        super().init__()
        self.nome = nome
        self.membros = []

    def add_membro(self, usuario):
        self.membros.append(usuario)

    def mencionar_todos(self):
        print("@todos", [u.email for u in self.membros])

class Enquete:
    def __init__(self, pergunta):
        self.pergunta = pergunta
        self.votos[usuario.email] = opcao

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



class Usuario: 
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.logado = False

    def __login__(self, email, senha):
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

    def __add_reacao__(self, reacao):
        self.reacoes.append(reacao)

    def fixar(self):
        self.fixada = True


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
        self.votos[usuario.email] = opcao

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

msg = Mensagem(u1, "tomara q funcione")
grupo.enviar_mensagem(msg)

grupo.listar_mensagens()
grupo.mencionar_todos()





