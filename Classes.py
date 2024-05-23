from datetime import datetime

class Funcionarios:
  def __init__(self,nome, sobrenome, ano):
    self.nome = nome
    self.sobrenome = sobrenome
    self.ano = int(ano)
    pass

  def nome_completo(self):
    return self.nome + ' ' + self.sobrenome
  
  def idade(self):
    ano_atual = datetime.now().year
    return ano_atual - self.ano

func1 = Funcionarios('Ana','Sobral','1993')
func2 = Funcionarios('Mario','Oliveira','1988')
func3 = Funcionarios('Oliver', 'Swartzmann','1945')

print(Funcionarios.nome_completo(func3))
print(Funcionarios.idade(func3))
