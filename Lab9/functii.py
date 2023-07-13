grad = []
coeficienti = []

def citeste_din_fisier():
    with open('polinom.txt', 'r') as fisier:
        linii = fisier.readlines()
        grad = list(map(int, linii[0].split()))
        coeficienti = list(map(int, linii[1].split()))
    return grad, coeficienti

def afiseaza_polinom(grad, coeficienti):
    polinom = "P(x) = "
    for i in range(len(grad)):
       polinom += f"{coeficienti[i]}X^{grad[i]}+"
    print(polinom)

def calculeaza_valoare(grad, coeficienti, x):
    valoare = 0
    for i in range(len(grad)):
        valoare += coeficienti[i] * (x ** grad[i])
    print(f"Valoarea polinomului în punctul {x} este: {valoare}")

def modifica_monom(grad, coeficienti, index, grad_nou, coeficient_nou):
    if index < 0 or index >= len(grad):
        print("Indexul monomului este invalid.")
        return
    grad[index] = grad_nou
    coeficienti[index] = coeficient_nou
    print("Monomul a fost modificat cu succes.")


def info_autor():
    print("Programul a fost realizat de Radu Adrian-Claudiu.")

def afiseaza_meniu():
    print('''
    ===== MENIU =====
    1. Citirea polinomului din fișier
    2. Afișarea polinomului citit
    3. Calculul valorii polinomului în punctul X
    4. Modificarea unui monom din polinom
    5. Info autor
    6. Termina program
    ''')