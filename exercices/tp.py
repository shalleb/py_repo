import random
nb_mystere = random.randint(1,100)
nb_essai_max = 4

for i in range (nb_essai_max):
    nb_saisi=int(input("Veuillez saisir un nombre: "))
    if nb_saisi == nb_mystere:
        print("Bien joué!")
        break
    else:
        if (nb_saisi > nb_mystere) and i !=3:
            print("plus petit")  
            if (nb_saisi - nb_mystere < 10):
                print("Vous y etes presque")
            print(f"il vous reste {nb_essai_max-i-1} essai(s)" )
        elif (nb_saisi < nb_mystere) and i !=3:
            print("plus grand")
            if (nb_mystere - nb_saisi < 10):
                print("Vous y etes presque")
            print(f"il vous reste {nb_essai_max-i-1} essai(s)" )
print("Perdu! Le nombre mystere etait: ", nb_mystere)


        


