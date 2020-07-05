''' Exercício Python 075: Desenvolva um programa que leia quatro valores pelo
teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. '''

#solicita ao usuário os 4 valores
num = (int(input('Digite um valor: ')), int(input('Digite mais um valor: ')),
    int(input('Digite outro valor: ')), int(input('Digite o último valor: ')))
print(f'Você digitou os seguintes valores: {num}')

#usar a função count, para ver se tem o 9
print(f'O número nove, aparece {num.count(9)} vezes ')

#teste se tem 3, usa o index para ver a posição
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares são: ', end=' ')
#percorre a lista e testa se é par
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
