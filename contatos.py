import re
import csv
with open('contatos.csv', newline="", encoding="utf-8") as lista_tel:
    for num_telefone in csv.DictReader(lista_tel):
        nova_lista = num_telefone['telefone'].strip()
        so_numeros = re.sub(r'\D', '', nova_lista)
        num_sujo = r'(\(\d{2}\)|\d{2})\s?\d\s?\d{4}-?\d{4}'
        valido = re.fullmatch(num_sujo, nova_lista)
        if valido:
            print(f"Telefone válido: {so_numeros}")
        else:
            print(f"Telefone inválido: {so_numeros}")