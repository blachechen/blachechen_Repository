#módulo de funções para limpeza de texto
import re
from datetime import datetime

def so_digito(texto): #limpa tudo que não for dígito
    return re.sub(r"\D", "", texto) 



def normalizar_nome(nome): #limpa tudo que não for letra ou espaço
    return " ".join(nome.split()).title() 



def formatar_data(texto): #converte data para o formato YYYY-MM-DD'
    return datetime.strptime(texto, "%d/%m/%Y").strftime("%Y-%m-%d") 



if __name__ == "__main__": # Testando as funções
    
    print(so_digito("Telefone: (11) 91234-5678"))  # Saída: 11912345678
    print(normalizar_nome("   joão   da SILVA  "))  # Saída: João Da Silva
    print(formatar_data("25/12/2023"))              # Saída: 2023-12-25
    