# Cálculo do IMC

print('Bom dia! Vamos calcular seu IMC?')
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / altura ** 2
print(f'Seu IMC (Índice de massa corporal) é: {imc:.1f}')