def nom_prenom(prenom : str, nom : str) -> str:
    try:
        print(f"{prenom.capitalize()} {nom.capitalize()}")
    except Exception as e:
        print(e)


prenom = input("Veuillez saisir votre nom: ")
nom = input("Veuillez saisir votre nom: ")
nom_prenom(prenom,nom)



