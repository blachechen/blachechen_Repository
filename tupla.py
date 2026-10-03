dia_da_semana = ("terça", "sexta", "domingo")
print("Tupla:", dia_da_semana)
dias_list = list(dia_da_semana)
print("Lista de dias da semana inicial:", dias_list)
print("Dias na lista: ")
for dia_ in dias_list:
    print(dia_)
while True: #sequencia a seguir é um exemplo de adição à lista
    add = input("Digite um dia da semana para adicionar à tupla ou fim para sair: ")
    if add == "fim":
    #sequencia a seguir é um exemplo de remoção de um item da tupla
    #remover = input("\nDigite um dia para remover (ou 'fim' para encerrar): ")
    #if remover.lower() == "fim":
    #    break
    
    # Verifica se o item existe antes de remover
    #if remover in dias_list:
    #   dias_list.remove(remover)
    #    print(f"'{remover}' foi removido com sucesso!")
    #    print("Lista atual:", dias_list)
    #else:
    #    print(f"O dia '{remover}' não foi encontrado na lista.")   
       break  
    dias_list.append(add)
dia_da_semana = tuple(dias_list)
print("Lista de dias da semana atualizada:", dia_da_semana)
