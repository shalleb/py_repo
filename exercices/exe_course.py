
def panne_moteur(liste):
    liste.append(liste.pop((0)))
    return liste

def passe_en_tete(liste):
    if len(liste) > 2:
        liste[0],liste[1] = liste[1],liste[0]
        return liste
    else : return print("La liste doit contenir au minimum 2 elements")

def sauve_honneur(liste):
    if len(liste) > 2 :
        liste[len(liste) - 1],liste[len(liste) - 2] = liste[len(liste) - 2], liste[len(liste) - 1]
        return liste
    else : return print("La liste doit contenir au minimum 2 elements")

def tir_blaster (liste):
    liste.pop(0)
    return liste

def retour_inattendu (liste):
    nouveau_concurant = input("Ajouter un concurant: ")
    liste.append(nouveau_concurant)
    return liste


ma_liste=["conc1","conc2","conc3","conc4","conc5"]
print(panne_moteur(ma_liste))
print(passe_en_tete(ma_liste))
print(sauve_honneur(ma_liste))
print(tir_blaster(ma_liste))
print(retour_inattendu(ma_liste))
