try:
    valor = int(input('Digite um número: '))
except ValueError:
    print('Valor incorreto, digite um número: ')
else:
    resultado = valor * 2
    print(resultado)