person = int(input('Digite quantas pessoas:'))
persons = []

for p in range(person):
    nome = input('Digite o nome: ')
    cpf = input('Digite o CPF: ')
    hospede = [nome, 'CPF:' + cpf]
    persons.append(hospede)
    
print(persons)
