unitee = str(input("Choisissez l'unitée voulue ou tapez simplement entrer : "))

los = str(input("Saisissez le nom du losnage : "))

r = int(input("Si vous voulez calculez l'aire du losange à partir des diagonales, tapez 1, sinon, tapez 2 : "))

if r == "1" : 

	diago = float(input("Saisissez la longeur de la première diagonale : "))

	diago2 = float(input("Saisissez la longeur de la deuxième diagonale : "))

	print("Voici l'exercice résolu : ")

	print("Aire",los,"=",diago,"x",diago2,"/ 2 =",diago*diago2,"/ 2 =",diago*diago2/2)

	print("Donc, l'aire du losange est de",diago*diago2/2,unitee,"²")

if r !="1" :

	diago = float(input("Saisissez la longeur du côté du losange : "))

	diago2 = float(input("Saisissez la hauteure du losange : "))

	print("Voici l'exercice résolu : ")

	print("Aire",los,"=",diago,"x",diago2,"=",diago*diago2)

	print("Donc, l'aire du losange",los,"est de",diago*diago2,unitee,"²")




