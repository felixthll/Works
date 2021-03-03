print("Avant de commencer, assurez vous de connaitre les 3 longeurs du triangle à traité. Toutes les longeurs doivent être dans la même unité.")

triangle = input("Saisissez le nom du triangle : ")
triangle = str(triangle)

angle = input("Indiquez l'angle qui semble être l'angle droit, si vous ne savez pas, n'écrivez rien : ")
angle = str(angle)

nomhypo = input("Saisissez le nom du plus grand côté du triangle : ")
nomhypo = str(nomhypo)

hypo = print("Saisissez la longeur de ",nomhypo," : ")
hypo = input()
hypo = float(hypo)

nomdeux = input("Saisissez le nom du deuxième côté du triangle : ")
nomdeux = str(nomdeux)

deux = print("Saisissez la longeur de",nomdeux," : ")
deux = input()
deux = float(deux)

nomtrois = input("Saisissez le nom du troisième côté du triangle : ")
nomtrois = str(nomtrois)

trois = print("Saisissez la longeur de",nomtrois," : ")
trois = input()
trois = float(trois)


resultat1 = hypo*hypo

resultat2 = deux*deux+trois*trois

if resultat1 == resultat2 : 

	print("Voici la réciproque du théorème de Pythagore spécifique à votre exercice : ")

	print(nomhypo,"est le plus long côté, c'est le seul qui pourrait être l'hypoténuse.")
	
	print("D'une part,",nomhypo,"² = ",hypo,"² = ",hypo*hypo)
	
	print("D'autre part,",nomdeux," + ",nomtrois," = ",deux,"² + ",trois,"² = ",deux*deux," + ",trois*trois," = ",deux*deux+trois*trois)

	print("On constate l'égalité : ",nomhypo,"² = ",nomdeux,"² + ",nomtrois,"²")

	print("La réciproque de Pythagore est vérifiée, donc",triangle,"est un triangle rectangle",angle,".")

if resultat1 != resultat2 : 

	print("Voici la réciproque du théorème de Pythagore spécifique à votre exercice : ")

	print(nomhypo,"est le plus long côté, c'est le seul qui pourrait être l'hypoténuse.")
	
	print("D'une part,",nomhypo,"² = ",hypo,"² = ",hypo*hypo)
	
	print("D'autre part,",nomdeux," + ",nomtrois," = ",deux,"² + ",trois,"² = ",deux*deux," + ",trois*trois," = ",deux*deux+trois*trois)

	print("On constate que ",nomhypo,"² ≠ ",nomdeux,"² + ",nomtrois,"²")

	print("La réciproque de Pythagore n'est pas vérifiée, donc",triangle,"n'est pas un triangle rectangle.")





