# Solicitando os dados do paciente
nome = input("Digite o nome do paciente:  ")
peso = float(input("Digite o peso do paciente Kg:  "))
altura = float(input("Digite a sua altura do paciente m:  "))

# Caculando o IMC do paciente
imc = peso / altura ** 2

# Definindo o quadro segundo o IMC
if imc < 18.5:
    situacao = "abaixo do peso"
elif imc <= 24.9:
    situacao = "peso normal"
elif imc <= 29.9:
    situacao = "sobrepeso"
elif imc <= 34.9:
    situacao = "obesidade grau I"
elif imc <= 39.9:
    situacao = "obesidade grau II"
else:
    situacao = "obesidade grau III"

print(f"o paciente {nome}, que tem o imc de {imc} está {situacao} ")
