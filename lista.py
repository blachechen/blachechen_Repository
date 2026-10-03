frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print(frutas[4])
print("Lista de frutas:")
for fruta in frutas:
    print(fruta)
    add = input("Digite uma fruta para adicionar à lista: ")
    if add == "fim":
            break
    frutas.append(add)
print("Lista de frutas atualizada:", frutas)

