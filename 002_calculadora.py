# Calculadora em Python

print("\n----------- Calculadora ----------\n")

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

print('\nEscola qual operaçõa deseja realizar:\n')
print(' 1 - Soma ')
print(' 2 - Subtração ')
print(' 3 - Multiplicação ')
print(' 4 - Divisão ')

escolha = input('\nEscolha sua Opção (1/2/3/4): ')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if escolha == '1':
    print('\n')
    print(num1, "+", num2, "=", add(num1, num2))
    print('\n')

elif escolha == '2':
    print('\n')
    print(num1, "-", num2, "=", sub(num1, num2))
    print('\n')

elif escolha == '3':
    print('\n')
    print(num1, "*", num2, "=", mult(num1, num2))
    print('\n')

elif escolha == '4':
    print('\n')
    print(num1, "/", num2, "=", div(num1, num2))
    print('\n')

else:
    print('\nOperação Invalida')

