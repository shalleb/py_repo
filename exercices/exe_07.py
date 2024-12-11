age = int(input("L'âge de votre enfant : "))
if  age < 0 :
    print("L'âge doit être positif")
elif 0 <= age <3 :
    print("L'âge minimal est de 3 ans")
elif 3 <= age <= 6:
    print("Vous avez une licence Baby")
elif 7 <= age <= 8:
    print("Vous avez une licence Poussin")
elif 9 <= age <= 10:
    print("Vous avez une licence Pupille")
elif 11 <= age <= 12:
    print("Vous avez une licence Minime")
else:
    print("Vous avez une licence Cadet")