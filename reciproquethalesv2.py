print("Avant de commencer, assurez vous que toutes les longeurs saisies sont dans la même unité : ")

unitee = input("Choisissez l'unité voulue ou taper simplement entrer : ")

para = input("Saisissez la première droite que vous voulez tester :")

para2 = input("Saisissez la deuxième droite que vous voulez tester :")

sec1 = input("Saisissez les droites qui sont sécantes, la droite : ")

sec2 = input("est sécantes à la droite : ")

inter = input("Saisissez le point d'intersection : ")

lon = print("Saisissez la longeur",inter,sec1[1])

lon = float(input())

lon2 = print("Saisissez la longeur",inter,sec1[0])

lon2 = float(input())

lon3 = print("Saisissez la longeur",inter,sec2[0])

lon3 = float(input())

lon4= print("Saisissez la longeur",inter,sec2[1])

lon4 = float(input())

result1 = lon / lon2

result2 = lon3 / lon4

print("Voici la réciproque du théorème de Thalès spécifique à votre exercice : ")

print("Les droites (",sec1," ) et (",sec2," ) sont sécantes en",inter,".")

print("D'une part, les points ",sec1[0],",",inter,",",sec1[1]," et ",sec2[1],",",inter,",",sec2[0]," sont alignés dasn le même ordre.")

print("D'autre part, on a ",inter,sec1[1]," / ",inter,sec1[0]," = ",lon," / ",lon2," = ",result1," et ",inter,sec2[0]," / ",inter,sec2[1]," = ",lon3," / ",lon4," = ",result2)

if result1 == result2 :

	print("Puisque les deux rapports sont égaux, on peut appliquer la réciproque de la propriété de Thalès, et on en déduit que ( ",sec1[0],sec2[1]," ) est parallèle à ( ",sec2[0],sec2[1]," ).")

else : 

	print("Les deux rapports sont différents, donc, les droites ( ",para," ) et ( ",para2," ) ne sont pas parallèles.")
