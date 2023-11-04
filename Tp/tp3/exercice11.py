liste=["compter","tous","les","mots","de","moins","de","six","caractères","ainsi","que","tous","les","mots","de","sept","et","plus","caracteres"]
liste_moins_six=[]
liste_plus_et_six=[]
for i in range(len(liste)):
    if len(liste[i])<6:
        liste_moins_six.append(liste[i])
    elif len(liste[i])>=6:
        liste_plus_et_six.append(liste[i])

print(liste)
print(liste_moins_six)
print(liste_plus_et_six)