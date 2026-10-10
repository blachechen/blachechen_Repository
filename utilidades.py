def media_notas(nota):
    media = sum(nota)/len(nota)
    return media
notas = [8, 7, 9]
print(media_notas(notas))