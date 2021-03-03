print("Toutes les longeurs fournis devront être dabs la même unité.")

unitee = input("Saisissez l'unitée de longeur ou tapez simplement entrer : ")

listenb = []

nb = 0

while nb != "" :

	nb = input("Saisissez les longeurs de la figure et tapez enter quand vous avez terminé : ")

	if nb != "" :

		nb = float(nb)

		listenb.append(nb)

result = sum(listenb)

print("Le périmètre de la figure est de",result,unitee)

