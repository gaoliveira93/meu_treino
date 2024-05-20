def pessoa():
    nome = 'Guilherme'
    sobrenome = 'Oliveira'
    ano = int(1993)
    nome_completo(nome,sobrenome)
    calc_idade(ano)

def nome_completo(nome, sobrenome):
    nome_completo = f"Este é meu nome completo: {nome}  {sobrenome}"
    print(nome_completo)

def calc_idade(ano):
    idade = int(2024 - ano)
    print(f"Idade: {idade}")

pessoa = pessoa()

    