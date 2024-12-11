temp= float(input("Veuillez saisir la température de l'eau: "))
if temp < 0 :
    print("L'etat de l'eau est solide")
elif 0 <= temp <= 100 :
    print("L'etat de l'eau est liquide")
else :
    print("L'etat de l'eau est gazeux")