class Usuario:
    def __init__(self, nome, idade, email, profissao, senha):
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

    def logar(self, email, senha):
        if self.email == email and self.senha == senha:
            print('Logado com sucesso!')
            print(self.menuUsuario())

    def menuUsuario(self):
        opcao = 0
        while opcao != 'x':
            print('****** Bom Pra Cachorro ******')
            print('1 - Adicionar Amigo')
            print('2 - Excluir Amigo')
            print('3 - Mostrar Amigos')
            print('4 - Mudar Nome')
            print('5 - Mudar Idade')
            print('6 - Mudar profissão')
            print('7 - Mudar Senha')
            print('x - Sair')
            opcao = int(input('Digite a opção:'))

            if opcao == 1:
                email_amigo = input('Informe o email de seu amigo')
                self.adicionarAmigo(email_amigo)

            if opcao == 2:
                emailAmigo = input('Informe o email de seu amigo')
                self.excluirAmigo(emailAmigo)

            if opcao == 3:
                self.imprime_amigos()

            if opcao == 4:
                NovoNome = input('Informe o novo nome')
                self.set_nome(NovoNome)

            if opcao == 5:
                NovaIdade = input('Informe o nova idade')
                self.set_nome(NovaIdade)

            if opcao == 6:
                NovaProfissao = input('Informe o nova profissão')
                self.set_nome(NovaProfissao)

            if opcao == 7:
                NovaSenha = input('Informe o novoa senha')
                self.set_nome(NovaSenha)

            if opcao == 'x':
                print("******Obrigado por usar nosso site!******")

    def adicionarAmigo(self, NovoAmigo):
        self.amigos.append(NovoAmigo)

    def excluirAmigo(self, email):
        amigo = self.buscarAmigo(email)
        self.amigos.remove(email)

    def imprime_amigos(self):
        print(self.amigos)