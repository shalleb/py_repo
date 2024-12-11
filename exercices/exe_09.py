age = int(input("Veuillez saisir l'âge de votre candidat : "))
salaire = float(input("Veuillez saisir le salaire souhaité : "))
nb_experience = float(input("Veuillez saisir le nombre d'années d'experience : "))
if (age < 30):
    msg = "L'âge minimum pour le poste est 30 ans"
elif (salaire >= 40000):
    msg = "Le salaire maximum possible est 40 000 euros"
elif (nb_experience <= 5):
    msg = "Le nombre d'années d'expérience minimum est de 5 ans"
else :
    msg = "Le profil est valable"

print(msg)