#exercice 1(creer une fonction pour afficher un dictionnaire)
livre= {"titre":"Mariane porte plainte", "Auteur":"Fatou Diome", "Année":2017, "genre":"narratif"}

def afficher_dict(dictionnaire: dict):
    print(f"1-exercice1: afficher le dictionnaire {dictionnaire}")
    for i,j in dictionnaire.items():
        print(f"{i}:{j}\n")

afficher_dict(livre)

#exercice 2 (une fonction qui renvoie l'intersection de deux ensembles en paramètres)
fruits={"tomates", "mangues", "oranges"}
legumes={"tomates", "aubergines", "oigons"}

def Intersection_ensembles( ensemble1:set, ensemle2:set)->set:
    print(f"2-exercice2 : intersection des ensembles {ensemble1} et {ensemle2}")
    return ensemble1&ensemle2

print(Intersection_ensembles(fruits,legumes),"\n")

#exercice3 (Liste de dictionnaire)
pers1={"nom":"SAMNE", "prenom":"BORIS", "age":20}
pers2={"nom":"COulibaly", "prenom":"Daouda", "age":23}
pers3={"nom":"SAMNE", "prenom":"COulibaly", "age":28}

Liste_dictionnaire=[pers1,pers2,pers3]

def oldests(liste_dictionnaire:list, age=20):
    print(f"3-exercice3- liste des noms des personnes dont l'age est sup ou = à {age}")
    liste_personnes_age=[p["nom"] for p in liste_dictionnaire if p["age"]>=age]
    return liste_personnes_age
            
print(oldests(Liste_dictionnaire, 23),"\n")

#exercice4 
nombres=(2, 3, 4)

def liste_carre_Tuples(nombres:tuple)->list:
    print(f"4-exercice4-Liste des carrées du tuple {nombres}")
    Liste=[nombre**2 for nombre in nombres]
    return Liste

print(liste_carre_Tuples(nombres),"\n")

#exercice5

classe={
        "Coulibaly":["SD","maths","pc"], 
        "Daouda":["Dp","maths","français"],
        "Boris":["Python", "anglais", "communication","SD","maths","Dp"],
        "Prince":["Python", "histoire","maths"]
        }

def uniqueFavoriteCorse(classe:dict)->set:
    print("5-exercice5 dictionnaires et liste")
    uniqueFavoriteCorses=set()
    for liste in classe.values():
        for element in liste:
            n=0
            for liste1 in classe.values():
                for element1 in liste1:
                    if liste!=liste1 and element==element1:
                        n+=1
            if n==0:
                uniqueFavoriteCorses.add(element)
    return uniqueFavoriteCorses

print(uniqueFavoriteCorse(classe), "\n")

#exercice6
nombres=[1,2,3,4,5,5,5]

def ensembleNombreUnique(nombres:list)->set:
    print("6-exercice6 (ensemble des nombres uniques dans une liste de nombre)" )
    nombresUniques={nombre for nombre in nombres}
    return nombresUniques

print(ensembleNombreUnique(nombres),"\n")

#exercice7

tuple1=("SAMNE",20)
tuple2=("COULIBALY", 24)
tuple3=("SAMCOULI", 23)
tuple4=("DADBOR",44)

liste_tuple=[tuple1,tuple2,tuple3,tuple4]

def Younger(Liste:list, age:int)->list:
    print("7-exercice7-liste de tuple")
    Youngers=[young[0] for young in Liste if young[1]<=age]
    return Youngers

print(Younger(liste_tuple,30), "\n")

#exercice8

panier={"pomme": 12,
        "banane":25,
        "orange":40}

def prixTotal(paniers: dict)->float:
    print("8-exercice8 dictionnaire et liste")
    return sum(paniers.values())

print("le prix total est", prixTotal(panier),"Dh","\n")

