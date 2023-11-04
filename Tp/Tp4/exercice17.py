#exercice17
#Parcourir un dictionnaire
Livres={"Sous l'orage":"Seydou badian", 
        "Le Parachutage":"Norbert Zongo", 
        "De purs hommes":"Mohamed Mbougar Sarr"}
print("Affichage des livres dans la logique(Titre,Auteur):")
for titre in Livres:
    print(f"-({titre}, {Livres[titre]})")