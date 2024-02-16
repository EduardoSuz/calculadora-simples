import time

print('''
===========================
=       calculadora       =
===========================
''')
time.sleep(0.8)

# operações a ser escolhidas
operacao = input('''
escolha uma das operações abaixo:

+ para adição
- para subtração
* para multiplicação
/ para divisão
''')
time.sleep(0.5)

# números para fazer os cálculos
num_um = int(input('Digite um número para calcular: \n'))
num_dois = int(input('Digite um número para calcular: \n'))
time.sleep(0.8)

# identificando operação e fazendo a conta logo depois
if operacao == '+':
    print(f'resultado: {num_um + num_dois}')

elif operacao == '-':
    print(f'resultado: {num_um - num_dois}')

elif operacao == '*':
    print(f'resultado: {num_um * num_dois}')

elif operacao == '/':
    print(f'resultado: {num_um / num_dois}')

else:
    print(f'Erro!! \n reinicie o código e escolha uma das operações citadas.')

