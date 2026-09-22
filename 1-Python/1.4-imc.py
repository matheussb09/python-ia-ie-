# Solicitando peso altura ao usuário
peso = float(input("Digite o seu peso (Kg): "))
altura = float(input("Digite a sua altura (m): "))

# realizando o cálculo do IMC
imc = peso / altura**2

# apresentando o resultado do IMC ao usuário
print("O seu IMC é ", imc)
