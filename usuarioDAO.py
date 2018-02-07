import psycopg2
import psycopg2.extras

from usuario import Usuario

class UsuarioDAO():
    def __init__(self, conexao):
        self.conexao = conexao

    def inserirAmigo(self, email):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE usuario SET amigos='"+ str(email)+ "'" )
        cursor.close()
        self.conexao.commit()

    def listar(self):
        # necessário cursor_factory=psycopg2.extras.DictCursor quando se quer trabalhar com a tupla em formato de dicionário.
        # Ex.: tupla['nm_conta']
        cursor = self.conexao.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute('SELECT amigos FROM usuario')
        amigos = list()
        for tupla in cursor.fetchall():
            amigos.append(self.__montar_objeto_conta(tupla))
        cursor.close()
        self.conexao.commit()
        return amigos

    def remover(self, email):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM usuario WHERE amigos='"+ str(email)+ "'" )
        cursor.close()
        self.conexao.commit()

    def __montar_objeto_conta(self, tupla):
        """Método para montar uma conta a partir da tupla retornada do banco"""
        return Usuario(tupla['nome'])
