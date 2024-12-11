def compter_lettre_a(chaine_de_carac : str):
    compteur = 0
    for i in range(len(chaine_de_carac)):
        if chaine_de_carac[i] == "a":
            compteur += 1
    return compteur


def compter_lettre_a_avec_count(chaine_de_carac : str):
    compteur = chaine_de_carac.count('a')
    return compteur


chaine = input("Veuillez saisir une chaine de carac: ")
nombre_a = compter_lettre_a(chaine)
if (nombre_a) == 0:
    print ("La chaine ne contient pas de 'a'")
else:
    print(f"La chaine de caractere contient {nombre_a} de lettre 'a'")

nombre_a_count = compter_lettre_a_avec_count(chaine)
if (nombre_a_count) == 0:
    print ("La chaine ne contient pas de 'a'")
else:
    print(f"La chaine de caractere contient {nombre_a_count} de lettre 'a'")
