from functii import *
from Lab9.functii import info_autor

while True:
    afiseaza_meniu()
    optiune = input("Alegeti o opțiune: ")
    optiune = optiune.upper()

    if optiune == 'CF':
        nume_fisier = input("Introduceți numele fișierului: ")
        spectacole = citire_date_fisier(nume_fisier)
    elif optiune == 'CT':
        spectacole = citire_date_tastatura()
    elif optiune == 'A':
        afisare_date(spectacole)
    elif optiune == 'AS':
        afisare_date_sortate(spectacole)
    elif optiune == 'R':
        rezolva_problema(spectacole)
    elif optiune == 'I':
        info_autor()
    elif optiune == 'X':
        print("Programul a fost încheiat.")
        break
    else:
        print("Opțiune invalidă. Reîncercați.")