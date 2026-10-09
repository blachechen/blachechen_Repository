from datetime import datetime
data_hoje = datetime.today().strftime("%d/%m/%Y")
data_nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")
total_idade = (datetime.today().strptime(data_hoje, "%d/%m/%Y") - datetime.today().strptime(data_nasc, "%d/%m/%Y"))
print(f"Você tem {total_idade//365} anos.")
total_dias = total_idade.days
print(f"Você tem {total_dias} dias.")
