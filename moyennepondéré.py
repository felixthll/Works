unitee = input("Sasissez une unité ou taper simplement entrer si vous ne l'avez pas : ")

listenb = []

listecoeff = []

liste2 = []

nb = 0

while nb != "" :

	nb = input("Saisissez les nombres qui constituent la moyenne et tapez enter quand vous avez terminé : ")

	if nb != "" :

		nb = float(nb)

		listenb.append(nb)

for i in range(len(listenb)) : 

	print("Saisissez l'effectif correspondant à la valeur : ",listenb[i])

	nb = int(input())

	listecoeff.append(nb)

for i in range(len(listenb)) : 

	liste2.append(listenb[i] * listecoeff[i])

resultat = sum(liste2) / sum(listecoeff)

print("La moyenne pondérée est de",resultat,unitee)
