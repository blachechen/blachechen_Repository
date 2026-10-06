with open("diario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n Diário 1: aprendi a ler arquivo.")
    arquivo.write("\n Diário 2: aprendi a gravar arquivo.")
with open("diario.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
     print(linha.strip())