from usuario import Usuario
from post import Post
from mensagem import mensagem

usuario = Usuario()  # aui eu chamei ele globalmente pra poder chamar ele no def la em baixo


class SistemaBomPraCachorro:
    def _init_(self):
        self.usuarios = list()

    def menu(self):
        opcao = 0

        while opcao != 4:
            print('****** Bom Pra Cachorro ******')
            print('1 - Cadastrar-se')
            print('2 - Logar')
            # print('3 - Listar Usuarios')
            print('4 - Sair')
            opcao = int(input('Digite a opção:'))

            if opcao == 1:
                nome = input('Digite seu nome: ')
                sobrenome = input('Digite seu sobrenome: ')
                idade = int(input('Digite sua idade:'))
                email = input('Digite seu e-mail: ')
                profissao = input("informe sua profissao:")
                senha = input('Digite sua senha: ')
                self.cadastrar_usuario(nome, idade, email, profissao, senha)

            if opcao == 2:
                email = input('Digite seu e-mail: ')
                senha = input('Digite sua senha: ')
                self.logar(email, senha)

            if opcao == 3:
                self.imprime_cliente()

            if opcao == 4:
                print("******Obrigado por usar nosso site!******")

    def cadastrar_usuario(self, nome, idade, email, profissao, senha):
        usuario = Usuario(nome, idade, email, profissao, senha)
        self.usuarios.append(usuario)

    def logar(self, email, senha):
        while email != usuario.email and senha != usuario.senha:  # chamei ela aqui, tá tudo ok por enquanto
            print("E-mail ou senha incorretos. Por favor, tente novamente")
        print("Logado com sucesso!")

    def imprime_cliente(self):
        print(self.usuarios)