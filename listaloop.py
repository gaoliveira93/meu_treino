lista1 = [['Frutas', ['Limão', 'Abacate', 'Laranja', 'Mamão']],
          ['Legumes',['Cenoura', 'Tomate', 'Alface', 'Rúcula']]]

lista2 = [item for item in lista1 if 'Frutas' in item]

print(lista2)