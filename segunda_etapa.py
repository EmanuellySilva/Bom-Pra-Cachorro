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
    
  def set_idade(self,NovaIdade):
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

  def inicio(self):
    print('******************* Bom Pra Cachorro *******************')
    print('1 - Cadastrar-se')
    print('2 - Logar')
    opcao = input('Digite a opção:')

    if opcao == '1':
      nome = input('Digite seu nome: ')
      sobrenome = input('Digite seu sobrenome: ')
      email = input('Digite seu e-mail: ')
      senha = input('Digite sua senha: ')

# não sei o que colocar aqui pra armazenar o usuario novo

    if opcao == '2':
      email = input('Digite seu e-mail: ')
      senha = input('Digite sua senha: ')
      Cadastro(self.logar(email, senha))

   
'''class Post:
  def __init__(self, privado):
    self.privado = privado
  
  def privadoGet(self):
    return self.__privado'''


class Cadastro:
  def __init__(self, nome, sobrenome, email, senha):
    self.nome = nome
    self.sobrenome = sobrenome
    self.email = email
    self.senha = senha
    
  def logar(self, email, senha):
    while email != self.email or senha != self.senha:
      print("E-mail ou senha incorretos. Por favor, tente novamente")
    print("Logado com sucesso!")
    
  
  
  
class Amigo:
  def __init__(self, nome, idade, email, profissao, senha):
    self.nome = nome
    self.idade = idade
    self.email = email
    self.profissao = profissao
    self.senha = senha
    
U = Usuario()
print(U.inicio())  
