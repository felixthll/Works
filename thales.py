
print("Avant de démarrer ce programme, assurez vous que deux des droites soit sécantes, et que deux autres sont parallèles,que toutes les grandeurs soit dans la même unitée, et que vous connaissiez au moins 3 longeurs.")

unitee = input("Veullez choisir l'unitée voulue : ")

sec1 = []
sec2 = []
sec3 = []
sec4 = []

sec1 = input("Indiquer quelles droites sont sécantes, la droite : ")


sec2 = input("et la droite :")


sec1 = str(sec1)
sec2 = str(sec2)
sec3 = str(sec3)
sec4 = str(sec4)

inter1 = input("Indiquer le point d'intersection : ")

inter1 = str(inter1)

sec3 = input("Indiquer quelles droites sont parallèles, la droite : ")


sec4 = input("et la droite :")

val11 = print("Saississez la longeur",sec1[0],sec2[0],"ou taper entrer si vous ne l'avez pas : ")
val11 = input()

val22 = print("Saississez la longeur",sec1[0],inter1,"ou taper entrer si vous ne l'avez pas : ")
val22 = input()

val33 = print("Saississez la longeur",sec2[0],inter1,"ou taper entrer si vous ne l'avez pas : ")
val33 = input()

val44 = print("Saississez la longeur",sec2[1],inter1,"ou taper entrer si vous ne l'avez pas : ")
val44 = input()

val55 = print("Saississez la longeur",sec1[1],inter1,"ou taper entrer si vous ne l'avez pas : ")
val55 = input()

val66 = print("Saississez la longeur",sec2[1],sec1[1],"ou taper entrer si vous ne l'avez pas : ")
val66 = input()

if val11 == "" : 
	val11 = "0"

if val22 == "" : 
	val22 = "0"

if val33 == "" : 
	val33 = "0"

if val44 == "" : 
	val44 = "0"

if val55 == "" : 
	val55 = "0"

if val66 == "" : 
	val66 = "0"

val11 = float(val11)
val22 = float(val22)
val33 = float(val33)
val44 = float(val44)
val55 = float(val55)
val66 = float(val66)

print("Voici le théorème de Thalès spécifique àvotre exercice : ")

print("Les droites",sec1[0],"et",sec1[1],"sont sécantes en",inter1)

print("Les droites",sec2[0],"et",sec2[1],"sont parallèles")

print("Je peux donc appliquer le théorème de Thalès :")

print(inter1,sec1[0],"/",inter1,sec1[1],"=",inter1,sec2[0],"/",inter1,sec2[1],"=",sec2[0],sec1[0],"/",sec2[1],sec1[1])

print("D'où, en remplaçant avec les données de la figure : ",val11,"/",val22,"=",val33,"/",val44,"=",val55,"/",val66)

calcul = False

if val11 == "" : 
	calcul == False

else : 
	calcul = True

if val11 == False :  
	val11 = val22*val33/val44 


if val22 == False : 
	val22 = val11*val44/val33



if val33 == False : 
	val33 = val11*val44/val22


if val44 == False :
	val44 = val22*val33/val11



if val55 == False : 
	val55 = val33*val66/val44



if val66 == False and val44 == True and val55 == True and val33 ==True : 
	val22 = val44*val55/val33
 
 
print("En utilisant le produit en croix, on obtient les résultats suivant : ",inter1,sec1[0]," = ",val11,unitee," ; ",inter1,sec1[1]," = ",val22,unitee," ; ",inter1,sec2[0]," = ",val33,unitee," ; ",inter1,sec2[1]," = ",val44,unitee," ; ",sec2[0],sec1," = ",val55,unitee," ; ",sec2[1],sec1[1]," = ",val66,unitee)


