#exercice1
#ch=str(input("Entrer une chaine de caractere\n"))
#nbv=0
#v=('a','e','i','o','u','y')
#for c in ch:
#    if c in v:
#        nbv+=1

#print("le nombre de voyelles de votre chaine est ", nbv)

#exercice2
#condition=""
#while condition!="stop":
#    chai= str(input("Entrez une chaine de caractere svp\n"))
#    car=str(input("Entrer le caractere à remplacer\n"))
#    car_rem=str(input("Entrer un caractere de remplacement\n"))
#    chai_mo= chai.replace(car,car_rem)

#    print("votre nouvelle chaine est " + chai_mo)
#    condition=str(input("Voulez vous continuer?\n"))


#exercice3

#chaine=str(input("Entrer une nouvelle chaine\n"))
#print(chaine[::-1])

#exercice 4
#chaine=str(input("Entrer une chaine de caracteres\n"))
#nbmots=0
#for c in  chaine:
#    if c==" ":
#        nbmots+=1

#print("le nombre de mots est ", nbmots+1)

#exercice 5
#chaine= str(input("Entrer une chaine de caractere svp\n"))
#nba=0
#nbd=0
#nbs=0

#for c in chaine:
#    if c.isalpha():
#        nba+=1
#    elif c.isdigit():
#        nbd+=1
#    else:
#        nbs+=1

#print("le nombre de lettres est ", nba)
#print("le nombre de chiffre est ", nbd)
#print("le nombre de caracteres speciaux est ", nbs)

#exercice 6

#chaine=str(input("Entrez une chaine de cracteres svp\n"))
#car=str(input("Entrer un  caractere svp\n"))
#nbOcc=0
#for c in chaine :
#    if c==car:
#        nbOcc+=1
#print("le nombre d'occurence du caractere "+car+" dans la chaine "+ chaine +" est ", nbOcc)

#exercice7
#chaine= str(input("Entrer une phrase svp \n"))
#ch_t= chaine.split()
#for i in range(len(ch_t)) :
#    ch_t[i]=ch_t[i][0].upper() + ch_t[i][1:]

#chaine_trans= ' '.join(ch_t)

#print(chaine_trans)

#exercice 7

#chaine= str(input("Entrer une phrase svp\n"))
#chaine_trans= ' '.join( word.capitalize() for word in chaine.split())
#print(chaine_trans)

#exercice 8
#chaine= str(input("Entrer une phrase svp\n"))
#word= str(input("Enrer le mot à chercher\n"))
#pos=0
#chaine1= chaine.split()
#chaine_inv=chaine1[::-1]

#for mot in chaine_inv:
#    pos+=1
#    if mot==word:
#        break

#print(" Votre mot se trouve à la position n°", len(chaine1)-pos+1, " de votre phrase")
