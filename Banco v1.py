#!/usr/bin/env python
# coding: utf-8

# - depósito saque e extrato
# - os saques e depósitos tem que ser armazenados para serem exibidos como extrato
# - 3 saques diários com limite de 500 reais por saque, informar caso não haja saldo
# - Formato dos valores R$xxx,xx

# In[8]:


from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

menu = '''
Escolha a operação desejada: 

[s] -> Saque
[d] -> Depósito
[e] -> Extrato
[q] -> Sair

'''

LIMITE_SAQUES = 3
limite = 500
extrato = ''
saques = 0 
saldo = 0.00


print('BEM VINDO!')

while True:

    print(menu)
    user = str(input())

    if user == 'd' or user == 'D':
        deposito = float(input('Digite o valor do depósito\nPor favor, utilize o fomrato XXX.XX\n'))
        if deposito > 0:
            saldo += deposito

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            extrato += dt_string + ' DEPÓSITO: R$' + f'{deposito:.2f}' + '\n'
        else:
            print('Valor inválido para depósito.\n')

    elif user == 'e' or user == 'E':
        if extrato == '':
            print('Sem operações recentes\n')
        else:
            print('\nEXTRATO:\n\n'  + extrato + f'\nSALDO: R${saldo:.2f}' + '\n---------------\n')

    elif user == 's' or user == 'S':

        if saques >= LIMITE_SAQUES: 
            print('Limite de saques diários excedido.\n')

        else:
            saque = float(input('Digite o valor do saque\nPor favor, utilize o fomrato XXX.XX\n'))
            saque = float("{:.2f}".format(saque))

            if saque > limite: 
                print('Saque não realizado. Limite por saque é de R$500.00')
                extrato += dt_string + ' SAQUE NÃO EFETUADO: R$' + f'{saque:.2f}' + '\n'

            elif saque > saldo: 
                print(f'Saldo insuficiente. Seu saldo atual é R${saldo:.2f}\n')
                extrato += dt_string + ' SAQUE NÃO EFETUADO: R$' + f'{saque:.2f}' + '\n'

            else:
                saldo -= saque
                saques += 1

                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                extrato += dt_string + ' SAQUE: R$' + f'{saque:.2f}' + '\n'
                
    elif user == 'q' or user == 'Q':
        print('Obrigado por utilizar o sistema\nEncerrando...')
        break
        
    else: 
        print('Opção inválida. Por favor, escolha uma das opções listadas no Menu:\n')


# In[16]:





# In[ ]:




