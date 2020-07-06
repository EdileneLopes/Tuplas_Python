'''Exercício Python 077: Crie um programa que tenha uma tupla com várias
 palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
  quais são as suas vogais.'''

#criar tupla
palavras =('aprender', 'estudar', 'emocional', 'foco','eu','determinaçao',
            'praticar', 'empenho', 'trabalhar', 'orar', 'futuro', 'curso', 'silencio',
           'codigo','python')

#percorrer cada item na tupla
for item in palavras:
    #o\n, é para quebra de linha, o .upper para deixar maiúsculo
    print(f'\nNa palavra {item.upper()} tem as vogais: ', end='')
    #percorrer cada letra da palavra
    for letra in item:
        #teste para saber se tem vogal
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
