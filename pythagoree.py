from math import *

print("Toutes les longeurs données devront être dans la même unité, et le triangle doit être rectangle.")

unite = input("Choisissez l'untié de longeur : ")
unite = str(unite)

triangle = input("Veulliez saisir les 3 points qui forment le triangle : ")

angle = input("Veulliez saisir le point où figurent l'angle droit :  ")
angle = str(angle)

hypo = input("Connaisez vous l'hypoténuse ? : ")
hypo = str(hypo)

if hypo == "oui": 
	
	nomhypo = input("Veulliez saisir le nom de l'hypoténuse : ")
	nomhypo = str(nomhypo)

	hypo2 = input("Veulliez saisir la longueur de l'hypoténuse : ")
	hypo2 = float(hypo2)
	
	nomdeux = input("Veulliez saisir le nom du deuxième côté connu : ")
	nomdeux  = str(nomdeux)

	deux = input("Veulliez saisir la longueur du deuxième côté connu : ")
	deux = float(deux)

	nomtrois = input("Veullez saisir le nom du troisème côté inconnu : ")
	nomtrois = str(nomtrois)

	resultat = hypo2*hypo2-deux*deux
	resultat = float(resultat)
	resu = (sqrt(resultat))

	print("Voici le théorème de Pythadore spécifique à votre exercice : ")

	print("Je sais que le triangle",triangle,"est un triangle rectangle en",angle)
	print("Je peux donc appliquer le théorème de Pythagore : ")
	print(nomhypo,"² = ",nomdeux,"² + ",nomtrois,"²")
	print(hypo2,"² = ",deux,"² + ",nomtrois,"²")
	print(nomtrois,"² = ",hypo2,"² - ",deux,"²")
	print(nomtrois,"² = ",hypo2*hypo2,"-",deux*deux)
	print(nomtrois,"² = ",resultat)
	print(nomtrois," = √",resultat)
	print(nomtrois," = ",(sqrt(resultat)))

	print("Donc,",nomtrois," = ",resu, unite)

elif hypo == "non" :
	
	nomdeux2 = input("Saisissez le nom du premier côté connu : ")
	nomdeux2 = str(nomdeux2)

	deux2 = input("Saisissez la longueur du premier côté connu : ")
	deux2 = float(deux2)
	
	nomtrois3 = input("Saisissez le nom du deuxième côté connu : ")
	nomtrois3 = str(nomtrois3)

	trois3 = input("Saisissez la longueur du deuxième côté connu : ")
	trois3 = float(trois3)

	nomhypo1 = input("Saisissez le nom de l'hypoténuse : ")
	nomhypo1 = str(nomhypo1)

	resultat2 = deux2*deux2+trois3*trois3
	resultat2 = float(resultat2)
	resu2 = (sqrt(resultat2))

	print("Voici le théorème de Pythadore spécifique à votre exercice : ")

	print("Je sais que le triangle",triangle,"est un triangle rectangle en",angle)
	print("Je peux donc appliquer le théorème de Pythagore : ")
	print(nomhypo1,"² = ",nomdeux2,"² + ",nomtrois3,"²")
	print(nomhypo1,"² = ",deux2,"² + ",trois3,"²")
	print(nomhypo1,"² = ",deux2*deux2,"+",trois3*trois3)
	print(nomhypo1,"² = ",resultat2)
	print(nomhypo1," = √",resultat2)
	print(nomhypo1," = ",(sqrt(resultat2)))

	print("Donc,",nomhypo1," = ",resu2, unite)

else : 

	print("Vous n'avez pas répondu correctement, veulliez recharger la page et ressayer.")


	


