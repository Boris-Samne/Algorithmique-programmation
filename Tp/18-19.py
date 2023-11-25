#exerice18
#Liste avec doublons.
Liste= [1, 2, 2, 3,3, 3, 4, 4, 4, 4]
#Dictionnaire vide pour stocker les elements et leur nombre d'occurence.
Dict1={}
#boucle pour parcourir la liste.
#Verifier l'existence de l'element pour incrementer le nombre d'occurence à chaque fois.
#Ajouter l'élément dans le cas d'inexistence avec un nombre d'occurence égale à 1 init.
for e in Liste:
    if e in Dict1:
        Dict1[e]+=1
    else:
        Dict1[e]=1
print("18-Voici la Liste avec ses doublouns:\n", Liste)
print("Voici le dictionnaire (élement: nombre d'occurences):\n",Dict1)

#exercice19
#fusion de deux dictionnaires.
Dict2={"un":1,"deux":2,"trois":3,"quatres":4}
Dict_fusionne={**Dict1,**Dict2}
print("19-Voici le dictionnare de fusion:\n", Dict_fusionne)
