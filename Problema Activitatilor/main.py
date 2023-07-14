from Functii import *
activitati = []
while 1:
    print('\t\tMeniu\nC. Citire Tastatura\nF. Citire Fisier\nA. Afisare Activitati\nR. Rezolvare Problema\nI. Info Autor\nE. Iesire')
    optiune = input('Dati optiunea: ').lower()
    if optiune == 'c':
        activitati = citesteTastatura()
        input('Date citite.')
    elif optiune == 'f':
        activitati = citesteFisier()
        input('Fisier citit.')
    elif optiune == 'a':
        afisareActivitati(activitati)
        input()
    elif optiune == 'r':
        rezolvare = calendar(activitati)
        print('Am selectat activitatile in urmatoarea ordine: ')
        afisareActivitati(rezolvare)
        input()
    elif optiune == 'i':
        input('Nica Andrei\t3211a\tAIA')
    elif optiune == 'e':
        exit('iesire...')
    else:
        input('OPTIUNE INVALIDA!')