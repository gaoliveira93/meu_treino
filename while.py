
venda = []

while True:
    produto = input('Digite o produto: ')
    if not produto:
        break
    qtd = input('Digite a quantidade: ')
    venda.append([produto, qtd])

print(venda)