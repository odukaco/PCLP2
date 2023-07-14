from Functii import *

while 1:
    print('T. Citire Bancnote Tastatura\nF. Citire Bancnote Fisier\nA. Afisare bancomat\nR. Retragere bani\nI. Info Autor\nE. Iesire')
    opt = str(input('Alegeti optiunea: ')).lower()
    if opt == 't':
        bancnote = citireTastatura()
    elif opt == 'f':
        bancnote = citireFisier()
    elif opt == 'a':
        afisareBancomat(bancnote)
    elif opt == 'r':
        suma = int(input('Dati suma: '))
        retragere = bancomatLimitat(suma, bancnote, afis = False)
        print('Ati primit:', end = '')
        for i in range(len(retragere)):
            print(' ', retragere[i][1], end = '')
            print(' bancnote de ', end = '')
            print(retragere[i][0], end = ' ;')
        input()
    elif opt == 'i':
        print('')
    elif opt == 'e':
        exit('iesire')
    else:
        input('OPTIUNE INVALIDA.')