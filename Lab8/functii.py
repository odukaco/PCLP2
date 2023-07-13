matrice = []

def citire_matrice_din_fisier(nume_fisier):
    matrice = []
    with open(nume_fisier, 'r') as fisier:
        linii = fisier.readlines()
        for linie in linii:
            elemente = list(map(int, linie.strip().split()))
            matrice.append(elemente)
    print("Matricea a fost citită din fișier cu succes.")
    return matrice

def afisare_matrice(matrice):
    print("Matricea este:")
    for linie in matrice:
        for element in linie:
            print(element, end=" ")
        print()

def calcul_sume_submatrici(matrice, m):
    rezultat = []
    n = len(matrice)
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            suma = 0
            for x in range(i, i + m):
                for y in range(j, j + m):
                    suma += matrice[x][y]
            rezultat.append(suma)
    return rezultat

def salvare_rezultat_in_fisier(rezultat, nume_fisier):
    with open(nume_fisier, 'w') as fisier:
        for suma in rezultat:
            fisier.write(str(suma) + '\n')
    print("Rezultatul a fost salvat în fișier cu succes.")

def afiseaza_meniu():
    print('''
        ===== MENIU =====
    1. Citire matrice din fișier
    2. Afișare matrice citită
    3. Calcul sume submatrici + salvare în fișier a rezultatului
    4. Info autor
    5. Exit
    ''')