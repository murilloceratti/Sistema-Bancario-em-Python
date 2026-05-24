from datetime import datetime
import random, os, time
from colorama import Fore, Style, init
init(autoreset=True)

def gerarIdTransacao(transferencias):

    IdTransacao = random.randint(100000,999999)

    while IdTransacao in transferencias:
        IdTransacao = random.randint(100000,999999)

    return IdTransacao

def transferencia(usuarios,conta,transferencias):
    try:
        destinatario = int(input('Insira a conta do destinatário: '))

        if destinatario in usuarios:
            print(f'Nome: {usuarios[destinatario]["nome"]}\nCPF: {usuarios[destinatario]["cpf"]}')
            valor = int(input('Valor: '))

            if valor > 0:

                if valor <= usuarios[conta]['saldo']:

                    usuarios[conta]['saldo'] -= valor
                    usuarios[destinatario]['saldo'] += valor

                    idTransacao = gerarIdTransacao(transferencias)

                    if conta not in transferencias:
                        transferencias[conta] = {}

                    transferencias[conta][idTransacao] = {
                        'id' : idTransacao,
                        'remetente' : usuarios[conta]['nome'],
                        'destinatário': usuarios[destinatario]['nome'],
                        'valor' : valor,
                        'horário' : datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    }

                    print(Fore.GREEN + f'Transferência no valor de R${valor} para {usuarios[destinatario]["nome"]} realizada com sucesso!')
                    aguardarLimpar()
                else:
                    print('Saldo insuficiente.')
                    aguardarLimpar()
            else:
                print('O valor deve ser maior que 0.')
                aguardarLimpar()
        else:
            print('Usuário não encontrado')
            aguardarLimpar()

    except ValueError:
        print('Insira um valor válido')
        aguardarLimpar()

def saque(usuarios,conta):
    try:
        valor = int(input(f'Insira o valor que você deseja sacar: '))

        if valor > 0:

            if usuarios[conta]['saldo'] >= valor:

                usuarios[conta]['saldo'] -= valor
                print(f'Saque no valor de R${valor} realizado com sucesso.')
                aguardarLimpar()

            else:
                print('Você não possui saldo suficiente.')
                aguardarLimpar()
        else: 
            print('O valor deve ser maior que 0.')
            aguardarLimpar()
    except ValueError:
        print('Insira um valor válido.')
        aguardarLimpar()

def deposito(usuarios,conta):
    try:
        valor = int(input(f'Insira o valor que você deseja depositar: '))

        if valor > 0:

            usuarios[conta]['saldo'] += valor
            
            print(f'Depósito no valor de R${valor} realizado com sucesso.')
            aguardarLimpar()
        else:
            print('O valor deve ser maior que 0.')
            aguardarLimpar()
    except ValueError:
        print('Insira um valor válido.')
        aguardarLimpar()

def extrato(conta, transferencias):
    limpar()
    print('=== EXTRATO BANCÁRIO ===')
    if conta not in transferencias or not transferencias[conta]:
        print('Não há transações registradas nesta conta.')
        aguardarLimpar()
    else:
        for transacao in transferencias[conta].values():
            print(f'ID: {transacao["id"]}')
            print(f'Remetente: {transacao["remetente"]}')
            print(f'Destinatário: {transacao["destinatário"]}')
            print(f'Valor: R${transacao["valor"]}')
            print(f'Horário: {transacao["horário"]}')
            print('===================================')
        input('Pressione ENTER para retornar.')
        limpar()

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def aguardarLimpar():
    if os.name == 'nt':
        time.sleep(3)
        os.system('cls')
    else:
        time.sleep(3)
        os.system('clear')




