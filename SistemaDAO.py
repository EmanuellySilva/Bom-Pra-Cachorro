
import psycopg2
import psycopg2.extras

from usuario import Usuario

class SistemaDAO():
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir(self, usuario):
        cursor = self.conexao.cursor()
        cursor.execute('INSERT INTO usuario(nome, sobrenome, idade, email, profissao, senha) VALUES (%s, %s, %s, %s,%s, %s)', (usuario.nome, usuario.sobrenome, usuario.idade, usuario.email, usuario.profissao, usuario.senha))
        cursor.close()
        self.conexao.commit()

    def buscar(self, email):
        # necessário cursor_factory=psycopg2.extras.DictCursor quando se quer trabalhar com a tupla em formato de dicionário.
        # Ex.: tupla['nm_conta']
        cursor = self.conexao.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM usuario WHERE email='"+ str(email)+ "'")
        usuario = self.__montar_objeto_usuario(cursor.fetchone())
        cursor.close()
        self.conexao.commit()
        return usuario

    def mudarNome(self, novoNome, email):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE usuario SET nome='"+ str(novoNome)+ "'" + "WHERE email='"+ str(email)+ "'")
        cursor.close()
        self.conexao.commit()

    def mudarIdade(self, novaIdade, email):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE usuario SET idade='"+ str(novaIdade)+ "'" + "WHERE email='"+ str(email)+ "'")
        cursor.close()
        self.conexao.commit()

    def mudarProfissao(self, novaProfissao, email):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE usuario SET profissao='"+ str(novaProfissao)+ "'" + "WHERE email='"+ str(email)+ "'")
        cursor.close()
        self.conexao.commit()

    def mudarSenha(self, novaSenha, email):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE usuario SET senha='"+ str(novaSenha)+ "'" + "WHERE email='"+ str(email)+ "'")
        cursor.close()
        self.conexao.commit()

    def listar(self, email):
        # necessário cursor_factory=psycopg2.extras.DictCursor quando se quer trabalhar com a tupla em formato de dicionário.
        # Ex.: tupla['nm_conta']
        cursor = self.conexao.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM usuario WHERE email='"+ str(email)+ "'")
        usuario = list()
        for tupla in cursor.fetchall():
            usuario.append(self.__montar_objeto_usuario(tupla))
        cursor.close()
        self.conexao.commit()
        return usuario

    def remover(self, email):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM usuario WHERE email='"+ str(email)+ "'")
        cursor.close()
        self.conexao.commit()

    def __montar_objeto_usuario(self, tupla):
        """Método para montar uma conta a partir da tupla retornada do banco"""
        return Usuario(tupla['nome'], tupla['sobrenome'], tupla['idade'], tupla['email'], tupla['profissao'],tupla['senha'])
