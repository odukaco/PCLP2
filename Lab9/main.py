from functii import *


while True:
    afiseaza_meniu()
    optiune = input("Alege o opțiune: ")

    if optiune == '1':
        grad, coeficienti = citeste_din_fisier()
    elif optiune == '2':
        afiseaza_polinom(grad, coeficienti)
    elif optiune == '3':
        x = int(input("X: "))
        calculeaza_valoare(grad, coeficienti, x)
    elif optiune == '4':
        index = int(input("Introduceți indexul monomului: "))
        grad_nou = int(input("Introduceți noul grad: "))
        coeficient_nou = int(input("Introduceți noul coeficient: "))
        modifica_monom(grad, coeficienti, index, grad_nou, coeficient_nou)
    elif optiune == '5':
        info_autor()
    elif optiune == '6':
        print("Programul a fost încheiat.")
        break
    else:
        print("Opțiune invalidă. Reîncercați.")
