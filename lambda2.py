def pessoa():
    nome = 'Guilherme'
    sobrenome = 'Oliveira'
    ano = int(1993)
    nome_completo = lambda nome,sobrenome: f"Este é meu nome completo: {nome}  {sobrenome}"
    idade = lambda ano: 2024 - ano
    print(nome_completo(nome, sobrenome))
    print(idade(ano))

pessoa = pessoa()