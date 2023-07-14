from FunctiiL10 import *
while 1:
    print('C - Citire date tastatura\nF - Citire date fisier\nA - Afisare matrice poduri\nR - Rezolvare problema\
\nI - Info autor\nT - Termina program')
    opt = str(input('Alegeti optiunea: ')).strip().lower()
    if opt == 'c':
        n, start, podul = citireTastatura()
        dateeronate = False
        input('...')
    elif opt == 'f':
        n, start, podul, fisier, dateeronate = citireFisier(str(input('Dati fisierul: ')) + '.txt')
        input('Date citite din fisierul ' + fisier + '...')
    elif opt == 'a':
        if dateeronate:
            print('Fisierul contine date eronate.')
        else:
            afisarePoduri()
        input()
    elif opt == 'r':
        if dateeronate:
            print('\nFisierul contine date eronate.')
        else:
            resetSol()
            Plimbare(start)
            verificareFaraSolutii()
        input('\n...')
    elif opt == 'i':
        input('Nica Andrei / 3211a / AIA...')
    elif opt == 't':
        exit('Iesire...')
    else:
        input('Optiune invalida...')