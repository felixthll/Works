unitee = input("Sasissez une unité ou appuyer sur entrée : ")

liste = []

nb = 0

while nb != "" :

	nb = input("Sasissez les nombres qui constituent votre moyenne, et taper entrer quand vous avez terminé : ")

	if nb != "" :

		nb = float(nb)

		liste.append(nb)

resultat = sum(liste) / len(liste)

print("La moyenne de votre série est de",resultat,unitee)

