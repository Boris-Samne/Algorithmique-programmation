#exerice18
Liste= [1, 2, 2, 3,3, 3, 4, 4, 4, 4]
Dict1={}
for e in Liste:
    if e in Dict1:
        Dict1[e]+=1
    else:
        Dict1[e]=1
print("18-Voici la Liste avec ses doublouns:\n", Liste)
print("Voici le dictionnaire (élement: nombre d'occurences):\n",Dict1)
#exercice19
Dict2={"un":1,"deux":2,"trois":3,"quatres":4}
Dict_fusionne={**Dict1,**Dict2}
print("19-Voici le dictionnare de fusion:\n", Dict_fusionne)
