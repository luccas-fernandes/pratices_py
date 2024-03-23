# Calcule a média do aluno

nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))
nota3 = float(input('Qual foi a sua terceira nota? '))

media = (nota1 + nota2 + nota3) / 3

if media < 7:
    print(f'Sua média final foi:', media, '. Que pena, você reprovou.')

elif media >= 7 and media <= 10:
    print(f'Sua média final foi:', media, '. Parabéns, você foi aprovado.')

else:
    print('Você não digitou valores válidos ou sua média final excedeu 10. Tente novamente.')