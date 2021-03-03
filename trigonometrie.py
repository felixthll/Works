import math

print("Avant de commencer, assurez vous que le triangle sur lequelle repose l'exercice est rectangle, et que vous connaissez soit un autre angle + une autre longueur, ou soit deux longeurs.")

unitee = str(input("Choisissez l'unité qui concerne toute les longuers du triangle : "))

triangle = str(input("Saisissez le nom du triangle : "))

droit = str(input("Saisissez le nom de l'angle droit : "))

angle = str(input("Saisissez le nom de l'angle sur lequel les côtés sont définis : "))

angle2 = str(input("Connaisez vous la mesure de cette angle ? : "))

if angle2 =="oui" :
	angle3 = float(input("Saisissez la mesure de cette angle : "))

nomcote = str(input("Saisissez le nom de l'hypoténuse : "))

cote = str(input("Connaisez vous la longeur de l'hypoténuse ? : "))

if cote == "oui" :
	cotee = float(input("Saisissez la longeur de l'hypoténuse : "))

nomcote2 = str(input("Saisissez le nom de l'adjacent : "))

cote2 = str(input("Connaisez vous la longeur de l'adjacent ? : "))

if cote2 == "oui" :
	cote22 = float(input("Saisissez la longeur de l'adjacent : "))

nomcote3 = str(input("Saisissez le nom de l'opposé : "))

cote3 = str(input("Connaisez vous la longeur de l'opposé ? : "))

if cote3 == "oui" :
	cote33 = float(input("Saisissez la longeur de l'opposé : "))

if angle2 == "non" :

	if cote =="oui" and cote2 == "oui" :
		print("Voici la trigonométrie spécifique à votre exercice : ")
		print("Le triangle",triangle,"est rectangle en",droit,",je peux donc appliquer la trigonométrie.")
		print("On utilise le cosinus : ")
		print("cos",angle," =  adjacent / hypoténuse = ",nomcote2,"/",nomcote)
		print("Donc, cos",angle," = ",cote22,"/",cotee)
		print("D'où",angle," =  cos-1(",cote22,"/",cotee,") = ",math.acos(cote22/cotee))

	if cote == "oui" and cote2 =="oui" and cote3 == "oui" :
		print("Voici la trigonométrie spécifique à votre exercice : ")
		print("Le triangle",triangle,"est rectangle en",droit,",je peux donc appliquer la trigonométrie.")
		print("On utilise le cosinus : ")
		print("cos",angle," =  adjacent / hypoténuse = ",nomcote2,"/",nomcote)
		print("Donc, cos",angle," = ",cote22,"/",cotee)
		print("D'où",angle," =  cos-1(",cote22,"/",cotee,") = ",math.acos(cote22/cotee))

	if cote2=="oui" and cote3 == "oui" :
		print("Voici la trigonométrie spécifique à votre exercice : ")
		print("Le triangle",triangle,"est rectangle en",droit,",je peux donc appliquer la trigonométrie.")
		print("On utilise la tangente : ")
		print("tan",angle," =  opposé / adjacent = ",nomcote3,"/",nomcote2)
		print("Donc, tan",angle," = ",cote33,"/",cote22)
		print("D'où",angle," =  tan-1(",cote33,"/",cote22,") = ",math.atan(cote33/cote22))

	if cote2=="oui" and cote3=="oui" and cote == "oui" :
		print("Voici la trigonométrie spécifique à votre exercice : ")
		print("Le triangle",triangle,"est rectangle en",droit,",je peux donc appliquer la trigonométrie.")
		print("On utilise la tangente : ")
		print("tan",angle," =  opposé / adjacent = ",nomcote3,"/",nomcote2)
		print("Donc, tan",angle," = ",cote33,"/",cote22)
		print("D'où",angle," =  tan-1(",cote33,"/",cote22,") = ",math.atan(cote33/cote22))


	if cote=="oui" and cote3 == "oui" :
		print("Voici la trigonométrie spécifique à votre exercice : ")
		print("Le triangle",triangle,"est rectangle en",droit,",je peux donc appliquer la trigonométrie.")
		print("On utilise le sinus : ")
		print("sin",angle," =  opposé / hypoténuse = ",nomcote3,"/",nomcote)
		print("Donc, sin",angle," = ",cote33,"/",cotee)
		print("D'où",angle," =  sin-1(",cote33,"/",cotee,") = ",math.asin(cote33/cotee))

	if cote =="oui" and cote3 == "oui" and cote2 == "oui" :
		print("Voici la trigonométrie spécifique à votre exercice : ")
		print("Le triangle",triangle,"est rectangle en",droit,",je peux donc appliquer la trigonométrie.")
		print("On utilise le sinus : ")
		print("sin",angle," =  opposé / hypoténuse = ",nomcote3,"/",nomcote)
		print("Donc, sin",angle," = ",cote33,"/",cotee)
		print("D'où",angle," =  sin-1(",cote33,"/",cotee,") = ",math.asin(cote33/cotee))


if angle2 == "oui" :

	cot = input("Choisissez la longeur que vous voulez calculé : ")

	if cote == "oui" and cot == "adjacent" or cot == "Adjacent" :
		print("Voici la trigonométrie spécifique à votre exercice : ")
		print("Le triangle",triangle,"est rectangle en",droit,",je peux donc appliquer la trigonométrie.")
		print("On utilise le cosinus : ")
		print("cos",angle," =  adjacent / hypoténuse = ",nomcote2,"/",nomcote)
		print("Donc, cos",angle3," = ",nomcote2,"/",cotee)
		print("D'où",nomcote2," =  ",cotee," x cos",angle3," = ",cotee*math.cos(angle3))

	if cote2  == "oui" and cot == "opposé" or cot == "Opposé" :
		print("Voici la trigonométrie spécifique à votre exercice : ")
		print("Le triangle",triangle,"est rectangle en",droit,",je peux donc appliquer la trigonométrie.")
		print("On utilise la tangente : ")
		print("tan",angle," =  opposé / adjacent = ",nomcote3,"/",nomcote2)
		print("Donc, tan",angle3," = ",nomcote3,"/",cote22)
		print("D'où",nomcote3," =  ",cote22," x tan",angle3," = ",cote22*math.tan(angle3))

	if cote3 == "oui" and cot == "hypoténuse" or cot == "Hypoténuse" :
		print("Voici la trigonométrie spécifique à votre exercice : ")
		print("Le triangle",triangle,"est rectangle en",droit,",je peux donc appliquer la trigonométrie.")
		print("On utilise le sinus : ")
		print("sin",angle," =  opposé / hypoténuse = ",nomcote3,"/",nomcote)
		print("Donc, sin",angle3," = ",cote33,"/",nomcote)
		print("D'où",nomcote," =  ",cote33," x sin",angle3," = ",cote33*math.sin(angle3))



