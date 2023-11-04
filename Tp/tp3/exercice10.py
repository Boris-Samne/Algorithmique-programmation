liste=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
liste_paire=[]
liste_impaire=[]
for i in range(len(liste)):
    if liste[i]==0:
        liste_paire.append(liste[i])
        liste_impaire.append(liste[i])
    elif liste[i]%2==0:
        liste_paire.append(liste[i])
    else:
        liste_impaire.append(liste[i])

print(liste)
print(liste_paire)
print(liste_impaire)