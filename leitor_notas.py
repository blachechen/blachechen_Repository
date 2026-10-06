import csv
with open("notas.csv", newline="", encoding="utf-8") as ff:
    leitor = csv.reader(ff, delimiter=";")
    for linha in leitor:
        print(linha)

resultado = []
with open("notas.csv", newline="", encoding="utf-8") as ff:
    for aluno in csv.DictReader(ff):
        media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
        print(aluno["nome"], media)
        resultado.append({
        "nome": aluno["nome"],
        "media": round(media, 2)})
       

with open("media.csv", "w", newline="", encoding="utf-8") as ff:
    escritor = csv.DictWriter(ff, fieldnames=["nome", "media"])
    escritor.writeheader()
    escritor.writerows(resultado)
