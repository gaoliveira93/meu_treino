try:
    valor = int(input('Digite um número: '))
    print(valor)
except ValueError:
    print('Valor incorreto, digite um número: ')