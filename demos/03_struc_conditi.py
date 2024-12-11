print("----- MENU -----")
print("1-une action 1")
print("2-une action 2")

choix = input("Veuillez faire votre choix: ")
match choix:
    case "1":
        print("Choix 1")
    case "2": 
        print("Choix 2")
    case _:
        print("erreur de choix")
