import time, os
from operacoes import transferencia, saque, deposito, extrato, aguardarLimpar, limpar
from colorama import Fore, Style, init
init(autoreset=True)

def menuConta(nome, sobrenome, cpf, conta, senha, usuarios, transferencias):

    while True:
        try:
            if usuarios[conta]['contanova']:

                usuarios[conta]['saldo'] = 50
                usuarios[conta]['contanova'] = False

                print(Fore.GREEN + f'Olá, {nome}!\nVocê ganhou um bônus de R$50 em nosso aplicativo!\nO dinheiro já foi adicionado ao seu saldo e está disponível!')

                aguardarLimpar()
            else:
                print(f'Olá, {nome}\nSaldo: R${usuarios[conta]["saldo"]}\nEscolha uma opção para prosseguir:')
                opcao = int(input('[1] Transferência\n[2] Saque\n[3] Depósito\n[4] Extrato\n[5] Sair\n'))
                
                if opcao == 1:
                    limpar()
                    transferencia(usuarios, conta, transferencias)
                elif opcao == 2:
                    limpar()
                    saque(usuarios, conta)
                elif opcao == 3:
                    limpar()
                    deposito(usuarios, conta)
                elif opcao == 4:
                    limpar()
                    extrato(conta, transferencias)
                elif opcao == 5:
                    limpar()
                    break

        except ValueError:
            print('Insira um valor válido.')
            aguardarLimpar()
