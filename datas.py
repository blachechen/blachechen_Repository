from datetime import datetime
data_hoje = datetime.today().date()
data_nasc_str = input("Digite sua data de nascimento (somente os números): ")
data_formatada_str = f"{data_nasc_str[:2]}/{data_nasc_str[2:4]}/{data_nasc_str[4:]}"
data_nasc = datetime.strptime(data_formatada_str,"%d/%m/%Y").date()
print()
print(f"Você nasceu em {data_nasc.strftime('%d/%m/%Y')}")
total_idade = data_hoje - data_nasc
total_dias = total_idade.days
anos = data_hoje.year - data_nasc.year - ((data_hoje.month, data_hoje.day) < (data_nasc.month, data_nasc.day))
meses = (total_idade.days % 365) // 30
dias = (total_idade.days % 365) % 30
data_natal = datetime.strptime("25/12/2026", "%d/%m/%Y").date()
dias_para_natal = (data_natal - data_hoje).days

print()
print(f"Você tem {anos} anos.")
print()
print(f"Você tem {total_dias} dias.")
print()
print(f"Faltam {dias_para_natal} dias para o Natal de 2026!")
