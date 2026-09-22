# Coletando altura e idade do usuário
altura = float(input("Digite a sua altura: "))
idade = int(input("Digite a sua idade:  "))

# Validando altura e idade do usuário
acesso = (altura >= 1.40) and idade >= 12

# Apresentando resultado ao usuário
print("o usuário pode andar de montanha russa?", acesso)