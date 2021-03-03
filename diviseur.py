print("Info : les résultats à virgule qui peuvent suivre ne sont pas des diviseur. ")

nb = float(input("Choisissez le nombre de départ : "))

k = float(input("Combien de diviseur souhaitez vous afficher : "))

m = 1

while m < k : 

	print("Voici un diviseur de",nb," : ",nb/m)

	m = m + 1

