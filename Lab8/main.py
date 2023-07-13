from functii import *
from Lab9.functii import info_autor

while True:
    afiseaza_meniu()
    optiune = input("Alegeți o opțiune: ")

    if optiune == '1':
        nume_fisier = input("Introduceți numele fișierului: ")
        matrice = citire_matrice_din_fisier(nume_fisier)
    elif optiune == '2':
        afisare_matrice(matrice)
    elif optiune == '3':
        m = int(input("Introduceți ordinul submatricilor (m): "))
        rezultat = calcul_sume_submatrici(matrice, m)
        nume_fisier_rezultat = input("Introduceți numele fișierului pentru salvarea rezultatului: ")
        salvare_rezultat_in_fisier(rezultat, nume_fisier_rezultat)
    elif optiune == '4':
        info_autor()
    elif optiune == '5':
        print("Programul a fost încheiat.")
        break
    else:
        print("Opțiune invalidă. Reîncercați.")