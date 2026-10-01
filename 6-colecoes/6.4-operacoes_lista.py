lista_inicial = ["João","Pamela","Dominique"]
print("Lista Inicial: ",lista_inicial)
print(90 * "-")
#======Acrescentando item na lista======
lista_inicial.append("Eduarda")
print("Após o append()", lista_inicial)
print(90 * "-")
#======Acrescentando item em posição expecífica======
lista_inicial.insert(2,"Matheus")
print("Após o insert()", lista_inicial)
print(90 * "-")
#======modificando item em indíce especifico======
lista_inicial[3] = "Rafael"
print("Após a modificação:  ",lista_inicial)
print(90 * "-")
#======apagando item em indíce especifico======
del lista_inicial[3]
print("Após del():  ",lista_inicial)
print(90 * "-")
#======apagando valor especifico======
lista_inicial.remove("Pamela")
print("Após remove(): ",lista_inicial)
print(90 * "-")
#======apagando e armazenando valor da lista======
removido = lista_inicial.pop(1)
print(f"Após pop, removido {removido}", lista_inicial)
print(90 * "-")
#======limpando completamente a lista======
lista_inicial.clear()
print("Após o clear(): ",lista_inicial)
print(90 * "-")