table = float(input("Saisissez la table de division à exécuter : "))

multi = float(input("Saisissez jusqu'à quelle diviseur vous voulez allez : "))

nb = 1

while nb <= multi :

	print(table," / ",nb," = ",table/nb)

	nb = nb + 1
	