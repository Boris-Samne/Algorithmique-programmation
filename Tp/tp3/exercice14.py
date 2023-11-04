liste=[8, 3, 12.5, 45, 25.5, 52, 1]
liste_trié=[]
print("liste d'origine ",liste)
#print(liste_trié)
for i in range(len(liste)):
    liste_trié.append(min(liste))
    liste.remove(min(liste))

#print("liste d'origine ",liste)
print("liste trié ",liste_trié)