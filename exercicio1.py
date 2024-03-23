"""
exercicio - calculadora básica (4 operações) em py.
"""
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número novamente: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 



print(f'Escolha uma operação entre: adição; subtração; divisão e multiplicação')
operacaoEscolhida = input('Qual operação você deseja? ')

if operacaoEscolhida == 'adição':
    print(f'O resultado é: ', soma)
# num1 and num2.isdigit()

elif operacaoEscolhida == 'subtração':
    print(f'O resultado é: ', subtracao)

elif operacaoEscolhida == 'divisão':
    print(f'O resultado é: ', divisao)

elif operacaoEscolhida == 'multiplicação':
    print(f'O resultado é: ', multiplicacao)

else:
    print('Você não escolheu uma operação válida.')

