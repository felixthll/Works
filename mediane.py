unitee = input("Choisissez l'unitée ou tapez simplement entrez si vous ne l'avez pas : ")

liste = []

nb = float(0)

while nb != "" :
	
	nb = input("Saisissez un à un les nombres de votre série : ")

	if nb != "" :

		nb = float(nb)

		liste.append(nb)

liste.sort()

if len(liste) % 2 == 0 :

	resultat = ((liste [ (len(liste) - 1) // 2 ] + liste [ len(liste) // 2 ]) / 2 )

else :

	resultat = liste [ len(liste) // 2 ]

print("La médiane de votre série est de",resultat,unitee)


