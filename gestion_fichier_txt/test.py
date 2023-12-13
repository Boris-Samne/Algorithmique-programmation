import json

# Exemple de dictionnaire
nouvelle_ligne = {"cle1": "valeur1", "cle2": "valeur2", "cle3": "valeur3"}

# Ouverture du fichier en mode ajout ("a" pour append)
with open('mon_fichier.txt', 'a') as fichier:
    # Conversion du dictionnaire en format JSON et écriture dans le fichier
    fichier.write(json.dumps(nouvelle_ligne) + '\n')

with open('mon_fichier.txt', 'r') as fichier:
    for ligne in fichier:
        # Conversion de la ligne JSON en dictionnaire
        dictionnaire = json.loads(ligne)
        print(dictionnaire)
