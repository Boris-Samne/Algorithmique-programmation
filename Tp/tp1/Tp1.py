#exercice 1;
#from math import pi

#rayon= float(input("Entrer le rayon de la sphere en cm\n"))
#volume= (rayon**3*3*pi)/4
#print("le volume de la sphere est %.2f cm3" , % volume)


#exercice 2
#a=float(input("entrer le premier nombre"))
#b=float(input("entrer le deuxieme nombre"))
#c=float(input("entrer le troisieme nombre"))

#if a>b and a>c:
#    print("le max est ", a)
#elif b>a and b>c:
#    print("le maximun est ",b)
#else :
#   print("le maximun est ",c)

#exercice 3
#chiffre_texte= "42"
#chiffre= int(chiffre_texte)
#print("le chiffre est", chiffre," et son type est", type(chiffre))

#exercice 4
#n= int(input(" Entrer un nombre entier"))
#if n%2==0:
#    print("le nombre %d est paire"% n)
#else:
#    print("le nombre %d est impair"% n)

#exercice 5
#note= float(input("Entrer une note entre 0 et 20 \n"))
#while note<0 or note>20:
#   note= float(input("Entrer une note entre 0 et 20 \n "))

#if note>=16:
#    print("tres bien")
#elif note>=14 and 16>note:
#    print("bien")
#elif note>=12 and note <14:
#    print("Assez bien")
#elif note >=10 and note <12:
#    print("Passable")
#else :
#    print ("echec")

#exercice 6
#jr=float(input(" Entrer un nombre de jour de la semaine "))

#while jr!=1 and jr!=2 and jr!=3 and jr!=4 and jr!=5 and jr!=6 and jr!=7 :
#    jr=float(input(" Entrer un nombre de jour de la semaine "))

#if jr==1:
#    print("lundi")
#elif jr==2:
#    print("mardi")
#elif jr==3:
#    print("Mercredi")
#elif jr==4:
#    print("jeudi")
#elif jr==5:
#    print("Vendredi")
#elif jr==6:
#    print("Samedi")
#elif jr==6:
#    print("Samedi")
#else :
#    print("Dimanche")

#exercice 7
#p=float(input("Saisissez le poids du colis\n"))
#if p<=2 :
#    print("5 euros")
#elif p<=5 and p>=2:
#    print("20 euros")
#elif p>=5 and p<=10: 
#    print("10 euros")
#else : 
#    print("30 Euros") 

#exercice 8

#n=0
#nb= int(input(" Entrer un nombre \n"))
#for i in range( 1,nb):
#    if nb%i!=0 :
#        n+=1
#if n>2:
#    print("le nombre %d n'est pas premier " %nb)
#else:
#    print("le nombre %d est premier " % nb)

#exercice 9
#fact=1
#n= int(input("Entrer un nombre \n"))
#for i in range (1, n+1):
#    fact*=i

#print("le factoriel de ", n, " est " , fact)

#exercice 10
somme=0
n= int(input("Entrer un nombre n \n"))
for i in range(1, n+1):
    somme+=i**2

print("la somme des carrés des nombres de 1 à", n, "est :", somme )
