import random, time, os
from senha import hashSenha, verificarSenha
from menu_conta import menuConta
from operacoes import limpar, aguardarLimpar
from colorama import Fore, Style, init
init(autoreset=True)


usuarios = {}
transferencias = {}

while True:
    try:
        print(Fore.LIGHTGREEN_EX + """ 
██████╗  █████╗ ███╗   ██╗██╗  ██╗   ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝   ██╔══██╗╚██╗ ██╔╝
██████╔╝███████║██╔██╗ ██║█████╔╝    ██████╔╝ ╚████╔╝ 
██╔══██╗██╔══██║██║╚██╗██║██╔═██╗    ██╔═══╝   ╚██╔╝  
██████╔╝██║  ██║██║ ╚████║██║  ██╗██╗██║        ██║   
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝ """)
        escolha = int(input('Escolha uma opção para prosseguir:\n[1] Acessar conta\n[2] Abrir conta\n'))

        if escolha == 1:
            limpar()
            loginEscolha = int(input('[1] Login\n[2] Esqueci minha senha\n'))
            if loginEscolha == 1:
                limpar()
                conta = int(input('Insira o número da sua conta: '))

                if conta in usuarios:
                    cpf = input('CPF: ')
                    senha = input('Senha: ')

                    if usuarios[conta]['cpf'] == cpf and verificarSenha(usuarios[conta]['senha'], senha): 
                        limpar()
                        menuConta(usuarios, conta, transferencias)
                    else:
                        print('Dados incorretos.')
                        aguardarLimpar()
                else:
                    print('Conta inexistente.')
                    aguardarLimpar()
            
            elif loginEscolha == 2:
                limpar()
                conta = int(input('Recuperação de senha\nConta: '))
                cpf = input('CPF: ')
                limpar()
                if conta in usuarios and usuarios[conta]['cpf'] == cpf:
                    while True:
                        senhaNova =  input('Insira uma nova senha: ')
                        senhaNova2 = input('Insira novamente: ')
                        if senhaNova == senhaNova2:
                            usuarios[conta]['senha'] = hashSenha(senhaNova)
                            print('Sua senha foi redefinida com sucesso.')
                            aguardarLimpar()
                            break
                        else:
                            print('Senhas diferentes.\nPor favor, tente novamente.')
                            aguardarLimpar()
                else:
                    print('Dados incorretos.')
                    aguardarLimpar()



        elif escolha == 2:
            limpar()
            nome = input('Para abrir sua conta, iremos pedir alguns dados.\nNome: ')
            sobrenome = input('Sobrenome: ')

            while True:

                cpf = input('CPF: ')

                cpfExiste = False

                for dadosCPF in usuarios.values():

                    if cpf == dadosCPF['cpf']:
                        cpfExiste = True
                        break

                if cpfExiste:
                    print('Esse CPF já foi cadastrado.')
                    aguardarLimpar()

                else:
                    break

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
                'contanova' : True,
                'chave' : ''
            }

            limpar()

            print(f'Seja bem-vindo ao BankPy, {nome}\nO número da sua conta é: {conta}')
            print(Fore.RED + 'Anote o número da sua conta, ele será essencial para o Login.')
            time.sleep(5)
            limpar()
    except ValueError:
        print('Insira um valor válido')

