#exercice11
Personne={"nom":"Coulibaly", "age":24, "ville":"Mohamedia"}
if Personne:
    print("11-'personne' créée.")
else:
    print("11-'Personne n'existe pas.'")
#exercice12
print("12-Voici les valeurs de 'personne':\n", Personne.values())
#exercice13
Personne["age"]=30
print("13-Mis à jour de personne:\n", Personne)
#exerice14
Personne["email"]="Coul@mail"
print("14-'Personne' avec mail:\n", Personne)
#exerice15
del Personne["ville"]
print("15-'Personne' sans ville:\n", Personne)
#exercice16
if "nom" in Personne.keys():
    print("16-La clé 'nom' existe dans 'personne'.")
else:
    print("16-La clé 'nom' n'existe pas dans 'personne'.")

