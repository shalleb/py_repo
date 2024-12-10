nb = int(input("Donnez un nombre:"))
if (nb < 0) :
    print("Votre nombre doit étre positif")
elif (nb % 3 == 0) :
    print("Le nombre est divsible par 3")
else :
    print(f"Le nombre n'est pas divsible par 3")