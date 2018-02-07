from usuario import Usuario
from sistemaDAO import SistemaDAO
from usuarioDAO import UsuarioDAO
from excecoes import *
import psycopg2


class SistemaBomPraCachorro:
    def __init__(self):
        conexao = psycopg2.connect(host="localhost", database="bom_pra_cachorro", user="postgres", password=1234)
        self.SistemaDAO = SistemaDAO(conexao)
        self.usuarioDAO = UsuarioDAO(conexao)

    def menu(self):
        opcao = 0

        while opcao != 4:
            print('****** Bom Pra Cachorro ******')
            print('1 - Cadastrar-se')
            print('2 - Logar')
            print('3 - Excluir uma conta')
            print('4 - Sair')
            opcao = int(input('Digite a opção:'))

            if opcao == 1:
                nome = input('Digite seu nome: ')
                sobrenome = input('Digite seu sobrenome: ')
                idade = input('Digite sua idade:')
                email = input('Digite seu e-mail: ')
                profissao = input("informe sua profissao: ")
                senha = input('Digite sua senha: ')
                try:
                    self.cadastrar_usuario(nome, sobrenome, idade, email, profissao, senha)
                except UsuarioMenorDeIdadeException as e:
                    print('O usuário não foi cadastrado. Erro: ', e)
                '''except UsuarioJaExisteException as a:
                    print('O usuário não foi cadastrado. Erro: ', a)'''




            if opcao == 2:
                email = input('Digite seu e-mail: ')
                senha = input('Digite sua senha: ')
                try:
                    self.logar(email, senha)
                except EmailOuSenhaIncorretoException as es:
                    print('O usuário não foi logado. Erro: ', es)
                self.logar(email, senha)

            if opcao == 3:
                email = input('Informe seu email: ')
                senha = input('Informe sua senha: ')
                try:
                    self.excluir_conta(email, senha)
                except EmailIncorretoException as ei:
                    print('O usuário não foi removido. Erro: ', ei)


            if opcao == 4:
                print("******Obrigado por usar nosso site!******")

    def cadastrar_usuario(self, nome, sobrenome, idade, email, profissao, senha):
        if int(idade) < 18:
            raise UsuarioMenorDeIdadeException('Não pode cadastrar conta com usuario menor de idade.')

        '''usuario_existe = self.buscar_usuario(email)
        if usuario_existe:
            raise UsuarioJaExisteException('Usuario ja existe.')'''

        usuario = Usuario(nome, sobrenome, idade, email, profissao, senha)
        self.SistemaDAO.inserir(usuario)

    def buscar_usuario(self, email):
        return self.SistemaDAO.buscar(email)

    def excluir_conta(self, email, senha):
        usuario = self.buscar_usuario(email)
        if email == usuario.email:
            if senha != usuario.senha:
                raise EmailIncorretoException('Email ou senha incorretos.')
        self.SistemaDAO.remover(email)

    def logar(self, email, senha):
        usuario = self.buscar_usuario(email)
        if email == usuario.email:
            if senha != usuario.senha:
                raise EmailOuSenhaIncorretoException('Email ou senha incorretos.')
        else:
            raise EmailOuSenhaIncorretoException('Email ou senha incorretos.')
        self.menuUsuario(email)

    def menuUsuario(self, email):
        self.email = email
        self.user = self.buscar_usuario(email)
        opcao = 0
        while opcao != 8:
            print('****** Feed Cachorro ******')
            print('1 - Adicionar Amigo')
            print('2 - Excluir Amigo')
            print('3 - Mostrar Amigos')
            print('4 - Mudar Nome')
            print('5 - Mudar Idade')
            print('6 - Mudar profissão')
            print('7 - Mudar Senha')
            print('8 - Sair')
            print('9 - Meu perfil')
            opcao = int(input('Digite a opção: '))

            if opcao == 1:
                email_amigo = input('Informe o email de seu amigo: ')
                self.adicionarAmigo(email_amigo)

            if opcao == 2:
                emailAmigo = input('Informe o email de seu amigo: ')
                self.excluirAmigo(emailAmigo)

            if opcao == 3:
                self.imprime_amigos()

            if opcao == 4:
                novoNome = input('Informe o novo nome: ')
                self.SistemaDAO.mudarNome(novoNome, self.user.email)

            if opcao == 5:
                NovaIdade = input('Informe a nova idade: ')
                self.SistemaDAO.mudarIdade(NovaIdade, self.user.email)

            if opcao == 6:
                NovaProfissao = input('Informe a nova profissão: ')
                self.SistemaDAO.mudarProfissao(NovaProfissao, self.user.email)

            if opcao == 7:
                NovaSenha = input('Informe a nova senha: ')
                self.SistemaDAO.mudarSenha(NovaSenha, self.user.email)

            if opcao == 8:
                print("******Até logo!******")

            if opcao == 9:
                print('****Meu perfil****')
                user = self.buscar_usuario(self.user.email)
                self.SistemaDAO.listar(user.email)
                print('E-mail:', self.user.email)
                print('Nome completo:', self.user.nome, self.user.sobrenome)
                print('Idade:', self.user.idade)
                print('Profissão:', self.user.profissao)




    def buscarAmigo(self, email):
        return self.SistemaDAO.buscar(email)

    def adicionarAmigo(self, NovoAmigo):
        user = self.buscarAmigo(NovoAmigo)
        if NovoAmigo == user.email:
            self.usuarioDAO.inserirAmigo(NovoAmigo, self.user.email)


    def excluirAmigo(self, email):
        user = self.buscarAmigo(email)
        if email == user.email:
            self.usuarioDAO.remover(email)

    def imprime_amigos(self):
        self.usuarioDAO.listar()





