def menu():
        while True :
            print("                === MENU PRINCIPAL ===")
            print("                 1 - Voir les adresses")
            print("                 2 - Ajouter une adresse")
            print("                 3 - Editer une adresse")
            print("                 4 - Supprimer une adresse")
            print("                 5 - Quiter le programme")
            choix_Menu = input("Votre choix : ")
            match choix_Menu :
                case "1" :
                    visualisation()
                case "2" :
                    ajouter_adresse()
                case "3" :
                    editer_adresse()
                case "4" :
                    supprimer_adresse()
                case "5" :
                    break
                case _ :
                    print("***********Vérifiez votre choix!**********")
adresses = []
def ajouter_adresse():
    adresse = {
        "numéro de voie":int(input("Veuillez saisir le numero de voie: ")),
        "complément":input("Veuillez saisir le complement d'adresse: "),
        "intitulé de voie":input("Veuillez saisir l'intitulé de voie: "),
        "commune":input("Veuillez saisir la commune: "),
        "code postal":int(input("Veuillez saisir le code postal: "))}
    adresses.append(adresse)
    print("********Adresse ajoutée avec succées!**********")

def editer_adresse():
    try:
        while True:
            index_adresse = int(input("                 Veuillez donner le numero de l'adresse à modifier: "))
            if 0 <= index_adresse < len(adresses):
                while True :
                    print("            Pour modifier l'adresse, veuillez choisir le champs à modifier")
                    print("               Pour choisir le numéro de voie tapez 1")
                    print("               Pour choisir le complément d'adresse tapez 2")
                    print("               Pour choisir l'intitulé de voie' tapez 3")
                    print("               Pour choisir la commune tapez 4")
                    print("               Pour choisir le code postal tapez 5")
                    while True :
                        champs_a_modifier = int(input("Votre choix: "))
                        if 1 <= champs_a_modifier <= 5:
                            break
                        else : 
                            print("*********Vérifier votre choix!**********")
                            continue
                    match champs_a_modifier:
                        case 1 :
                            adresses[index_adresse]["numéro de voie"] = int(input("Veuillez saisir le numero de voie: "))
                        case 2 :
                            adresses[index_adresse]["complément"] = input("Veuillez saisir le complement d'adresse: ")
                        case 3 :
                            adresses[index_adresse]["intitulé de voie"] = input("Veuillez saisir l'intitulé de voie: ")
                        case 4 :
                            adresses[index_adresse]["commune"] = input("Veuillez saisir la commune: ")
                        case 5 :
                            adresses[index_adresse]["code postal"] = int(input("Veuillez saisir le code postal: ")) 
                    choix_continuer = input("*******Voulez vous changer un autre champs******** [oui/non]: ")
                    if choix_continuer == "oui":
                        continue
                    else : break
            else:
                print("********L'adresse n'existe pas******")
                continue
            break
    except ValueError :
        print("Veuillez saisir un numero")
  

def visualisation():
    if (len(adresses) == 0): 
        print("******Pas d'adresses à afficher*******")
    else: 
        for adresse in adresses :
            print(f"adresse n°{adresses.index(adresse)}")
            for key,value in adresse.items():
                print(f"     {key} : {value}")

def supprimer_adresse():
    if (len(adresses) == 0): 
        print("******Pas d'adresses à supprimer*******")
    else:
        while True:
            index_adresse = int(input("****Veuillez donner le numero de l'adresse à supprimer*****: "))
            if 0 <= index_adresse < len(adresses):
                del adresses[index_adresse]
                print("adresse supprimée avec succées!")
                visualisation()
                break
            else: 
                print("******adresse introuvable!******")
            continue

menu()