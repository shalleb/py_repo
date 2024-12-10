age = int(input("Votre âge : "))
# if age < 0 : 
#     print("l'age ne peut pas etre négatif")
# elif age > 18 :
#     print("T'es majeur")
# else: 
#     print("T'es mineur")   

# age >= 18 and print("T'es majeur") or age < 18 and print("T'es mineur") or age < 0 and print("l'age ne peut pas etre négatif")

if age >= 21 : 
    print("Majeur en USA")
elif age >= 18 :
    print("Majeur ailleurs")
else: 
    print("T'es mineur")  