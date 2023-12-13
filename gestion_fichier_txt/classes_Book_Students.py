import json

class book:
    def __init__(self,titre,auteur,datePub, quantite) -> None:
        self._titre=str(titre)
        self._auteur= str(auteur)
        self._datePub= str(datePub)
        self._quantite= int(quantite)

        livre = {"t":self._titre,"a":self._auteur,"d":self._datePub,"q":self._quantite}
         
        with open("gestion_fichier_txt/livres.txt", "a") as livres:
            if livres:
                livres.write(json.dumps(livre))
                print("nouveau livre créeé.\n")
            else:
                print("Base de données erronée.\n")
                

    @property
    def titre(self)->str:
        return self._titre
    
    def auteur(self)->str:
        return self._auteur
    
    def datePub(self)->str:
        return self._datePub
    
    def quantite(self)->str:
        return self._quantite
    
    @titre.setter
    def titre(self, newTitre):
        self._titre=str(newTitre)

    def auteur(self, newauteur):
        self._auteur=str(newauteur)

    def datePub(self, newdatePub):
        self._datePub=str(newdatePub)

    def quantite(self, quantite):
        self._quantite=str(quantite)

    @staticmethod
    def removeLivre(titre)->None:
        livres_modifies = []
        with open('mon_fichier.txt', 'r') as fichier:
            livres = [json.loads(ligne) for ligne in fichier]

        livres_modifies = [livre for livre in livres if livre['t'] != titre]

        with open("gestion_fichier_txt/livres.txt", "w") as livres:
            livres.write(json.dumps(livres_modifies) + '\n')

    def emprunter(titre)->None:
        with open("gestion_fichier_txt/livres.txt", "r") as fichier:
            livres=fichier.readlines() 
        livre_modifié= {livre for livre in livres if livre['t']==titre+' '}
        livre_modifié["q"]-=1
        livres_modifiés= [livre for livre in livres if livre['t']!=titre+' ']
        livres_modifiés.append(livre_modifié)

        with open("gestion_fichier_txt/livres.txt", "w") as livres:
            livres.writelines(livres_modifiés)
