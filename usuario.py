class Usuario:
    def _init_(self, nome, idade, email, profissao, senha):
        self.nome = nome
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
        for amigo in self.amigos:
            if amigo == email:
                return amigo
        return None

    def adicionarAmigo(self, NovoAmigo):
        self.amigos.append(NovoAmigo)

    def excluirAmigo(self, email):
        amigo = self.buscarAmigo(email)
        self.amigos.remove(email)
