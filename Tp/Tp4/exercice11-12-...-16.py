#exercice11
#Creation d'un dictionnaire
Personne={"nom":"Coulibaly", "age":24, "ville":"Mohamedia"}
if Personne:
    print("11-'personne' créée.")
else:
    print("11-'Personne n'existe pas.'")

#exercice12
#Les valeurs d'un dictionnaire
print("12-Voici les valeurs de 'personne':\n", Personne.values())

#exercice13
#Modifier une valeur dans un dictionnaire
Personne["age"]=30
print("13-Mis à jour de personne:\n", Personne)

#exerice14
#ajouter une valeur dans un dictionnaire
Personne["email"]="Coul@mail"
print("14-'Personne' avec mail:\n", Personne)

#exerice15
#supprimer une valeur dans un dictionnaire
del Personne["ville"]
print("15-'Personne' sans ville:\n", Personne)

#exercice16
#verifier l'existence d'une clé dans un dictionnaire
if "nom" in Personne.keys():
    print("16-La clé 'nom' existe dans 'personne'.")
else:
    print("16-La clé 'nom' n'existe pas dans 'personne'.")

