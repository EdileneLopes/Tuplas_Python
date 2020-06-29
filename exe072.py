'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente
preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

#criar a tupla, com os números por extenso
num = ('zero', 'hum', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')
#pedir a entrada de um número.
while True:
    x = int(input('Digite um número entre 0 e 20: '))
    #se estiver fora do intervalo, solicitar o valor novamente.
    if x < 0 or x > 20:
        print('Valor inválido, tente novamente.', end=' ')
     #escreverá o número por extenso
    else:
        print(f'Você digitou o número: \033[33m{num[x]}\033[m')
    resp = ' '
    #pergunta se quer continuar, retira os espaços vazios, deixa maiúscula e pega somente a
    #primeira letra da resposta
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
