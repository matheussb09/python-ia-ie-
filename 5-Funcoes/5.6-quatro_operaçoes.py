# Criando funções de calculo

def somar(a1,a2):
    soma = a1 + a2
    return soma

def subtrair(a1,a2):
    subtração = a1 - a2
    return subtração

def multiplicar(a1,a2):
    multiplicação = a1 * a2
    return multiplicação

def dividir(a1,a2):
    divisão = a1 / a2
    return divisão

# Solicitando dois números ao usuário
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))

# Chamando as funções de calculo
resultado_1 = somar(numero_1,numero_2)
resultado_2 = subtrair(numero_1,numero_2)
resultado_3 = multiplicar(numero_1,numero_2)
resultado_4 = dividir(numero_1,numero_2)

# Apresentando o resultado ao usuário
print(f"O resultado da soma é {resultado_1}")
print(f"O resultado da subtração é {resultado_2}")
print(f"O resultado da multiplicação é {resultado_3}")
print(f"O resultado da divisão é {resultado_4}")