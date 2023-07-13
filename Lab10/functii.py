spectacole = []

def citire_date_fisier(nume_fisier):
    spectacole = []
    with open(nume_fisier, 'r') as fisier:
        linii = fisier.readlines()
        for linie in linii:
            interval = linie.strip().split()
            spectacole.append((int(interval[0]), int(interval[1])))
        print("Datele au fost citite din fișier cu succes.")

def citire_date_tastatura():
    spectacole = []
    n = int(input("Introduceți numărul de spectacole: "))
    for i in range(n):
        inceput = input(f"Introduceți ora și minutul de început pentru spectacolul {i+1} (ex. 10 30): ")
        sfarsit = input(f"Introduceți ora și minutul de sfârșit pentru spectacolul {i+1} (ex. 11 45): ")
        spectacole.append((int(inceput.split()[0]), int(sfarsit.split()[0])))
    return spectacole

def afisare_date(spectacole):
    print("Spectacolele sunt:")
    for i, spectacol in enumerate(spectacole):
        print(f"Spectacolul {i+1}: {spectacol[0]}:{spectacol[1]} - {spectacol[2]}:{spectacol[3]}")

def afisare_date_sortate(spectacole):
    spectacole_sortate = sorted(spectacole, key=lambda x: x[1])
    print("Spectacolele sortate după ora de sfârșit sunt:")
    for i, spectacol in enumerate(spectacole_sortate):
        print(f"Spectacolul {i+1}: {spectacol[0]}:{spectacol[1]} - {spectacol[2]}:{spectacol[3]}")

def rezolva_problema(spectacole):
    spectacole.sort(key=lambda x: x[1])
    numar_spectacole = 0
    ora_sfarsit = 0
    spectacole_selectate = []
    for spectacol in spectacole:
        if spectacol[0] >= ora_sfarsit:
            numar_spectacole += 1
            spectacole_selectate.append(spectacol)
            ora_sfarsit = spectacol[1]
    print(f"Numărul maxim de spectacole vizionate: {numar_spectacole}")
    print("Spectacolele selectate sunt:")
    for i, spectacol in enumerate(spectacole_selectate):
        print(f"Spectacolul {i+1}: {spectacol[0]}:{spectacol[1]} - {spectacol[2]}:{spectacol[3]}")

def afiseaza_meniu():
    print('''
        ===== MENIU =====
    CF. Citire date din fișier
    CT. Citire date de la tastatură
    A. Afișare date
    AS. Afișare date sortate
    R. Rezolvare problemă
    I. Info autor
    "X. Termina programul
    ''')
