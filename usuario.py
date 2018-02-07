class Usuario:
    def __init__(self, nome, sobrenome, idade, email, profissao, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.email = email
        self.profissao = profissao
        self.senha = senha
        self.amigos = list()
        self.grupos = list()
        self.mensagens = list()

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_email(self):
        return self.email

    def get_profissao(self):
        return self.profissao

    def get_senha(self):
        return self.senha

    def set_nome(self, NovoNome):
        self.nome = NovoNome

    def set_idade(self, NovaIdade):
        self.idade = NovaIdade

    def set_profissao(self, NovaProfissao):
        self.profissao = NovaProfissao

    def set_senha(self, NovaSenha):
        self.senha = NovaSenha

    def buscarAmigo(self, email):
        return self.SistemaDAO.buscar(email)


    def adicionarAmigo(self, NovoAmigo):
        user = self.buscar_amigo(NovoAmigo)
        if NovoAmigo == user.email:
            self.UsuarioDAO.inserir(NovoAmigo)


    def excluirAmigo(self, email):
        user = self.buscar_amigo(email)
        if email == user.email:
            self.UsuarioDAO.remover(email)

    def buscar_amigo(self, email):
        return self.SistemaDAO.buscar(email)

    def imprime_amigos(self):
        amigos = self.UsuarioDAO.listar()
        for amigo in amigos:
            print('Nome:', amigo.nome, ' Sobrenome:', amigo.sobrenome)


