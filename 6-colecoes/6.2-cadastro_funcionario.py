# Criando dicionário composto de cadastro de funcionário
funcionarios = {
    "44356":{
            "nome":"Vitor Davi",
            "telefone":"11912121315",
            "data_nascimento":"10/12/2010",
            "cargo":"jovem aprendiz",
            "habilidades":["front-end","java","python"]
    },
    "42568":{
            "nome":"Julio henrique",
            "telefone":"11457853588",
            "data_nascimento":"19/4/2007",
            "cargo":"jovem aprendiz",
            "habilidades":["front-end","Pacote office","python"]
    },
    "46697":{
            "nome":"Maria Luiza",
            "telefone":"11420893549",
            "data_nascimento":"26/7/1995",
            "cargo":"Gerente",
            "habilidades":["marketing,administração,front-end","java","python"]


    },

}

print(funcionarios["44356"]["habilidades"][1])
