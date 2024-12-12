from typing import List,Dict
personne = {
    "nom" : "toto",
    "age" : 25,
    "email" : "toto@gmail.com",
    "is_Logged" : False
}

print(personne["nom"])

personne["age"] += 1
print(personne)

del personne["is_Logged"]
print(personne)

personne["prénom"] = "Tata"
print(personne)

champ= input("Donner le champs à modifier: ")
print(champ)
for key, value in personne.items():
    # print(key,value,champ)
    if champ == key:
        personne[champ] = input("la nouvelle valeur est: ")
print(personne)