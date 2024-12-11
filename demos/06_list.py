ma_liste=[3,2,5,"test",True,["a", "b", "c"]]

print(ma_liste)
print(ma_liste[3])
print(ma_liste[5][2])

ma_liste.append("aaaa")
print(ma_liste)
ma_liste.insert(2,'aa')
print(ma_liste)
ma_liste.extend([{'bb':54,'98':654}])
print(ma_liste)
ma_liste.remove(5)
print(ma_liste)

for element in ma_liste:
    print(element)