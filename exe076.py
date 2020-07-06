'''Exercício Python 076: Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

print('-='*20)
print(f'{"LISTAGEM DE PREÇOS":^38}')
print('-='*20)

#criando a tupla
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno',15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 125.45,
            'Canetinhas', 22.30,
            'Livro', 34.90)

#percorrendo a tupla até o tamanho da listagem(len)
for pos in range(0,(len(listagem))):
    if pos % 2 == 0:
        #se é par, ou seja, é nome do produto, printar com espaço de 30 caracteres
        #alinhado à esquerda, e para completar os 30, usei o pontinho
        print(f'{listagem[pos]:.<30}', end='')
    else:
        #se é o preço, printar alinhado à direita com 7 caracteres,
        #e duas casas decimais
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
