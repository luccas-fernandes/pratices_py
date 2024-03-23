"""
Uma empresa de entrega deseja calcular o custo do frete
com base na distância da entrega e no peso da encomenda.
Crie um programa que solicite ao usuário a distância da
entrega em quilômetros e o peso da encomenda em
quilogramas. O programa deve então calcular o custo do
frete, aplicando as seguintes regras:
• Para distâncias acima de 100 km, o custo do frete é de
R$ 2 por quilômetro.
• Para distâncias menores ou iguais a 100 km, o custo do
frete é de R$ 1,50 por quilômetro.
• Além disso, para encomendas com peso superior a 10
kg, há uma taxa extra de R$ 5.

"""

print('Olá! Vamos calcular seu frete.')

distancia = float(input('Informe-nos a distancia para sua casa: '))
peso = float(input('Infomrme o peso da sua encomenda: '))


if peso > 10:
    taxaExtra = 5
else:
    taxaExtra = 0
if distancia > 100:
    frete = distancia * 2 + taxaExtra
    print(f'Você pagará R$ {frete} de frete.')
elif distancia <= 100:
    frete = distancia * 1.5 + taxaExtra
    print(f'Você pagará R$ {frete} de frete.')


