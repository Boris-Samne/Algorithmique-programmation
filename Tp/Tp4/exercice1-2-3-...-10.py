#exerice1
Fruits = {"pomme", "banane", "orange"}
print("1-Création de fruits:\n", Fruits)
#exercie2
Fruits.update({"mangue", "mandarine", "pastèque"})
print("2-Après ajout de mangue, mandarine et pasthèque:\n", Fruits)
#exercice3
Fruits.remove("orange")
print("3-Après suppression de l'orange:\n", Fruits)
#exercice4
if "pomme" in Fruits:
    print("4-pomme se trouve dans Fruits.")
else:
    print("4-pomme de ne trouve pas dans Fruits.")
#exercice5
Legumes={"carottes", "brocoli"}
Aliments=Fruits.union(Legumes)
print("5-Voici les aliments:\n", Aliments)
#exercice6
Aliments_sains=Fruits.intersection(Legumes)
print("6-Les aliments sains sont:\n", Aliments_sains)
#execice7
Fruits_uniquement=Fruits.difference(Legumes)
print("7-Les Fruits uniquement sont:\n", Fruits_uniquement)
#exercice8
if Aliments.intersection(Fruits):
    print("8-Fruits est sous ensemble de Aliments.")
else:
    print("8-Fruits n'est pas un sous ensemble de Aliments.")
#exercice9
Fruits.clear()
if Fruits:
    print("9-Voici Fruits:\n", Fruits)
else:
     print("9-Fruits a été supprimé.")
#exercice10
Legumes_copie=Legumes.copy()
Legumes_copie.add("épinard")
print("10-Voici la copie des legumes qui contient épinard:\n", Legumes_copie)