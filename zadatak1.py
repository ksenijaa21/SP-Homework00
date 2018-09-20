lista = [12, 15, 19, 18, 5, 99, 3, 28]

min_lista = lista[0]
max_lista = lista[0]

for i in range(len(lista)-1):
    if min_lista > lista[i+1]:

        min_lista = lista[i+1]

    if max_lista < lista[i+1]:

        max_lista = lista[i+1]

print("Minimum niza je: " + str(min_lista))
print("Maksimum niza je: " + str(max_lista))