while True:
    nb = int(input("Veuillez saisir un nombre entre 1 et 3: "))
    if nb not in [1,2,3]:
        print("Veuillez réessayer")
        continue
    else: 
        print ("BJ!")
        break
