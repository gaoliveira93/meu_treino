import random

# Variáveis 
pontos_user = 0
pontos_IA = 0

# Funções
def gerar_num(min, max):
    return random.randint(min, max)

def comparar(num_user, num_IA):
    if num_user > num_IA:
        print('Digite um número menor')
        return False
    elif num_user < num_IA:
        print('Digite um número maior')
        return False
    else:
        print('Acertou')
        return True

def somar_pontos(acertou):
    global pontos_user
    global pontos_IA

    if acertou:
        pontos_user += 1
    else:
        pontos_IA += 1

# Início do Programa
player = input('Qual o seu nome? ')
print(f'Beleza, {player}, vamos lá!')
jogar = True

while jogar:
    print(f'Seu placar é: {player} {pontos_user} x IA {pontos_IA}')
    resposta = input('Deseja jogar? 1(s) 2(n) ')

    if resposta == '1':
        print('Vamos jogar, vou gerar um número de 1 a 10, tente adivinhar')
        sorteado = gerar_num(1, 10)
        acertou = False

        while not acertou:
            try:
                num_user = int(input('Digite um número de 1 a 10: '))
                acertou = comparar(num_user, sorteado)
                somar_pontos(acertou)
                print(f'Seu placar é: {pontos_user} x {pontos_IA}')
            except ValueError:
                print('Número inválido, digite um número válido.')
        
    elif resposta == '2':
        print('Tchau')
        jogar = False
    else:
        print('Opção inválida, escolha 1 para jogar ou 2 para sair.')



