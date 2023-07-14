from FunctiiL11 import *
mod = True
while 1:

    print('C - Citire date de la tastatura\nF - Citire date dintr-un fisier\nA - Afisare matrice\n\
R - Rezolvare problema\nS - Mod afisare solutie in fisier\nX - Mod afisare solutie directa.\nI - Info Autor\nT - Termina programul')

    opt = (input('Dati optiunea: ')).upper()

    if opt == 'C':
        (n, Mat, Cale, x0, y0) = citMatTastatura()
        input('Matrice citita...')

    elif opt == 'F':
        (n, Mat, Cale, x0, y0) = citMatFisier(fisier=(str(input('Dati numele fisierului .txt: ')) + '.txt'))
        input('Fisier citit...')

    elif opt == 'A':
        afisMatrice(Mat)
        input('...')

    elif opt == 'R':
        Cale[x0] [y0] = 1
        cautaCale(2,x0, y0, mod)
        if mod:
            input('Solutiile au fost scrise in fisier...')
        else:
            input('...')

    elif opt == 'I':
        input('Nica Andrei \t 3211a \t AIA...')

    elif opt == 'T':
        exit('Iesire...')

    elif opt == 'S':
        mod = True
        input('Mod afisare fisier selectat...')

    elif opt == 'X':
        mod = False
        input('Mod afisare directa selectat...')

    else:
        input('Optiune invalida!')
