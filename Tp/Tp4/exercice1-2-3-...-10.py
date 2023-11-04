#exerice1
#pour créer l'ensemble Fruits
Fruits = {"pomme", "banane", "orange"}
print("1-Création de fruits:\n", Fruits)

#exercie2
#ajouter des éléments à Fruits
Fruits.update({"mangue", "mandarine", "pastèque"})
print("2-Après ajout de mangue, mandarine et pasthèque:\n", Fruits)

#exercice3
#Supprimer un élément d'un ensemble(set())
Fruits.remove("orange")
print("3-Après suppression de l'orange:\n", Fruits)

#exercice4
#Vérifier l'existence d'un élément dans un ensemble
if "pomme" in Fruits:
    print("4-pomme se trouve dans Fruits.")
else:
    print("4-pomme de ne trouve pas dans Fruits.")

#exercice5
#Union de deux ensembles
Legumes={"carottes", "brocoli"}
Aliments=Fruits.union(Legumes)
print("5-Voici les aliments:\n", Aliments)

#exercice6
#Intersection de deux ensembles
Aliments_sains=Fruits.intersection(Legumes)
print("6-Les aliments sains sont:\n", Aliments_sains)

#execice7
#Différence entre deux ensembles
Fruits_uniquement=Fruits.difference(Legumes)
print("7-Les Fruits uniquement sont:\n", Fruits_uniquement)

#exercice8
#Intersection de deux ensembles
if Aliments.intersection(Fruits):
    print("8-Fruits est sous ensemble de Aliments.")
else:
    print("8-Fruits n'est pas un sous ensemble de Aliments.")

#exercice9
#suppresion d'un ensemble
Fruits.clear()
if Fruits:
    print("9-Voici Fruits:\n", Fruits)
else:
     print("9-Fruits a été supprimé.")

#exercice10
#Copie d'un ensemble
Legumes_copie=Legumes.copy()
Legumes_copie.add("épinard")
print("10-Voici la copie des legumes qui contient épinard:\n", Legumes_copie)