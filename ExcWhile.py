MAX_LINES = 3
MAX_BET = 30
MIN_BET = 1

def deposit():
    while True:
        amount = input('Digite o valor do seu depósito: R$ ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Digite um valor acima de 0!')
        else:
            print('Digite um valor válido')
            
    return amount


def get_number_lines():
    while True:
        lines = input('Digite o número de linhas para apostar: (1-'+ str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Digite um número entre 1 e 3!')
        else:
            print('Digite um número de linhas válido')
    
    return lines

def get_bet():
    while True:
        amount = input('Digite o valor para apostar em cada linha: R$ ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Digite um número entre R${MIN_BET} e R${MAX_BET}!')
        else:
            print('Digite um número válido')
    
    return amount


def main():
    balance = deposit()
    lines = get_number_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f'Sua aposta é de {bet} em {lines} linhas dando o total de {total_bet}')

main()