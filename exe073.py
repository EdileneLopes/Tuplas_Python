'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''


times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional',
         'Corinthians', 'Fortaleza', 'Goiás','Bahia','Vasco','Atlético-MG','Fluminense','Botafogo',
         'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense','Avaí')

print('-='*30)
print(f'Lista dos times do brasileirão 2019: {times}')
print('-='*30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*30)
print(f'Os 4 últimos são: {times[16:]}')
print('-='*30)
print(f'Lista em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f'O {times[18]} está na {times.index("Chapecoense")+1}ª posição.')
print('-='*30)
print('FIM DA EXECUÇÃO')