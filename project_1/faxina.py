import csv
import re
from pathlib import Path

base_dir = Path(__file__).resolve().parent
arquivo_csv = base_dir / 'sujos.csv'

with open(arquivo_csv, newline='', encoding='utf-8') as lista_tel:
    for num_telefone in csv.DictReader(lista_tel):
        telefone = (num_telefone.get('telefone') or '').strip()
        so_numeros = re.sub(r'\D', '', telefone)
        valido = bool(re.fullmatch(r'\d{11}', so_numeros))

        if valido:
            print(f'Telefone válido: {so_numeros}')
        else:
            print(f'Telefone inválido: {so_numeros}')