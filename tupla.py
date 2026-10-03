dia_da_semana = ("terça", "sexta", "domingo")
print("Tupla:", dia_da_semana)
dias_list = list(dia_da_semana)
print("Lista de dias da semana inicial:", dias_list)
print("Dias na lista: ")
for dia_ in dias_list:
    print(dia_)
while True:
    add = input("Digite um dia da semana para adicionar à tupla ou fim para sair: ")
    if add == "fim":
       break  
    dias_list.append(add)
dia_da_semana = tuple(dias_list)
print("Lista de dias da semana atualizada:", dia_da_semana)
