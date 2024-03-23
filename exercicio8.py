"""
Um sistema de biblioteca precisa calcular a multa para
devolução de livros com base na quantidade de dias de
atraso. Faça um programa que solicite ao usuário o número
de dias de atraso na devolução do livro. O programa deve
então calcular a multa a ser paga, aplicando as seguintes
regras:
• Para atrasos de até 7 dias, a multa é de R$ 0,50 por dia.
• Para atrasos entre 8 e 14 dias, a multa é de R$ 1 por dia.
• Para atrasos acima de 14 dias, a multa é de R$ 2 por dia.
"""
print('Bom dia! Verifique a sua multa:')
dias = int(input('Informe-nos a quantidade de dias de atraso na devolução do livro: '))

if dias <= 7:
    multa = float(dias * 0.50)
    print(f'Sua multa é de R$ {multa}')
elif dias > 7 and dias <= 14:
    multa = float(dias * 1)
    print(f'Sua multa é de R$ {multa}')
else: 
    multa = float(dias * 2)
    print(f'Sua multa é de R$ {multa}')