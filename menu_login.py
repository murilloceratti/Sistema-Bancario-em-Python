import random, time, os
from senha import hashSenha
from menu_conta import menuConta
from operacoes import limpar, aguardarLimpar
from colorama import Fore, Style, init
init(autoreset=True)


usuarios = {}
transferencias = {}

while True:
    try:
        escolha = int(input('Seja Bem-Vindo ao BankPy\nEscolha uma opção para prosseguir:\n[1] Acessar conta\n[2] Abrir conta\n'))

        if escolha == 1:
            limpar()
            conta = int(input('Insira o número da sua conta: '))

            if conta in usuarios:
                cpf = input('CPF: ')
                senha = input('Senha: ')

                hash_senha = hashSenha(senha)

                if usuarios[conta]['cpf'] == cpf and hash_senha == usuarios[conta]['senha']:
                    limpar()
                    menuConta(nome, sobrenome, cpf, conta, senha, usuarios, transferencias)
                else:
                    print('Dados incorretos.')
                    aguardarLimpar()
            else:
                print('Conta inexistente.')
                aguardarLimpar()


        elif escolha == 2:
            limpar()
            nome = input('Para abrir sua conta, iremos pedir alguns dados.\nNome: ')
            sobrenome = input('Sobrenome: ')
            cpf = input('CPF: ')
            senha = input('Senha: ')

            senha = hashSenha(senha)

            conta = random.randint(1000,9999)

            while conta in usuarios.keys():
                conta = random.randint(1000,9999)

            usuarios[conta] = {
                'nome' : nome,
                'sobrenome' : sobrenome,
                'cpf' : cpf,
                'senha' : senha,
                'saldo' : 0,
                'contanova' : True
            }

            limpar()

            print(f'Seja bem-vindo ao BankPy, {nome}\nO número da sua conta é: {conta}')
            print(Fore.RED + 'Anote o número da sua conta, ele será essencial para o Login.')
            time.sleep(5)
            limpar()
    except ValueError:
        print('Insira um valor válido')

