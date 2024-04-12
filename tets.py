menu = '''
BANCO DIO.ME - ESCOLHA UMA OPÇÃO

[d] depositar
[s] saque
[e] extrato
[q] sair


'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
       valordeposito = float(input('Qual valor deseja depositar?'))
       if valordeposito > 0:
        saldo += valordeposito
        extrato += f'deposito feito no valor de {valordeposito} \n'
       else:
        print('Digite um valor inteiro.')
       
    elif opcao == 's':
        valorsaque = int(input('Qual valor deseja sacar?'))
        if valorsaque > limite or valorsaque > saldo:
            print('Saque não autorizado, tente outro valor.')
        
        if numero_saques < LIMITE_SAQUES:
            saldo -= valorsaque
            numero_saques += 1
            extrato += f'saque feito no valor de {valorsaque} \n'
        else:
          print('Limite de saque diário excedido')
        
    elif opcao == 'e':
        print(f'Extrato {extrato} \n')
        print(f'Seu saldo é de {saldo}')
    elif opcao == 'q':
        break
    else:
        print('Opcao Invalida. Selecione corretamente a opcao desejada.')

