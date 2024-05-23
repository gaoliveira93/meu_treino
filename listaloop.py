lista1 = [['Frutas', ['Limão', 'Abacate', 'Laranja', 'Mamão']],
          ['Legumes',['Cenoura', 'Tomate', 'Alface', 'Rúcula']]]

lista2 = [item for item in lista1 if 'Frutas' in item]

print(lista2)

valores = [x * 10 for x in range(6)]
print(valores)

#() Para utilizar Generator Expression e redução de consumo de memória