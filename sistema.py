from usuario import Usuario


class SistemaBomPraCachorro:
    def __init__(self):
        self.usuarios = list()

    def menu(self):
        opcao = 0

        while opcao != 3:
            print('****** Bom Pra Cachorro ******')
            print('1 - Cadastrar-se')
            print('2 - Logar')
            print('3 - Sair')
            opcao = int(input('Digite a opção:'))

            if opcao == 1:
                nome = input('Digite seu nome: ')
                sobrenome = input('Digite seu sobrenome: ')
                idade = int(input('Digite sua idade:'))
                email = input('Digite seu e-mail: ')
                profissao = input("informe sua profissao: ")
                senha = input('Digite sua senha: ')
                self.cadastrar_usuario(nome, sobrenome, idade, email, profissao, senha)

            if opcao == 2:
                email = input('Digite seu e-mail: ')
                senha = input('Digite sua senha: ')
                self.logar(email, senha)

            if opcao == 3:
                print("******Obrigado por usar nosso site!******")

    def cadastrar_usuario(self, nome, sobrenome, idade, email, profissao, senha):
        usuario = Usuario(nome, idade, sobrenome, email, profissao, senha)
        self.usuarios.append(usuario)

    def logar(self, email, senha):
        for usuario in self.usuarios:
            if email == usuario.email and senha == usuario.senha:
                usuario.menuUsuario()

            else:
                print("E-mail ou senha incorretos. Por favor, tente novamente")


