unitee = str(input("Choisissez l'unitée voulue ou tapez simplement entrer : "))

trap = str(input("Saisissez le nom du trapèze : "))

mesure = float(input("Saisissez la longeur de la grande base : "))

mesure1 = float(input("Saisissez la longeur de la petite base : "))

mesure2 = float(input("Saisissez la longeur de la hauteur : "))

print("Voici l'exercice résolu : ")

print("Air",trap," = (grande base + petite base) x hauteur / 2 = (",mesure,"+",mesure1,") x",mesure2,"/ 2 =",mesure+mesure1," x",mesure2,"/ 2 =",(mesure+mesure1)*mesure2,"/ 2 =",(mesure+mesure1)*mesure2/2)

print("Donc , l'air du trapèze",trap,"est de",(mesure+mesure1)*mesure2/2,unitee,"²")

