liste = [5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2]
liste_sans_doublon=[]
liste_sans_doublon.append(liste[0])
liste_triée=[]
n=0
for i in range(1,len(liste)):
    for j in range(len(liste_sans_doublon)):
        if liste_sans_doublon[j]==liste[i]:
            n+=1
    if n==0:
        liste_sans_doublon.append(liste[i])
    else: 
        n=0

print("La liste de depart\n",liste)
print("La liste sans doublon\n",liste_sans_doublon)
for i in range(len(liste_sans_doublon)):
    liste_triée.append(min(liste_sans_doublon))
    liste_sans_doublon.remove(min(liste_sans_doublon))


#print("La liste sans doublon\n",liste_sans_doublon)
print("La liste sans doublon triée\n",liste_triée)