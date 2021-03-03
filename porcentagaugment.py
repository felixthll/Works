nombre = input("Veulliez saisir le nombre de départ : ")
nombre = int(nombre)

reduc = input("Veulliez saisir l'augmentation : ")
reduc = int(reduc)

prix = (1+reduc/100)*nombre
prix = int(prix)

print("Le prix finale est de",prix,"euros")
