from operator import itemgetter
def citesteFisier(fisier='in.txt'):
    activitati = []
    with open(fisier, 'rt') as f:
        for linie in f.readlines():
            n, m = linie.split()
            n, m = int(n), int(m)
            activitati.append([n, m])
    return activitati

def citesteTastatura():
    activitati = []
    while 1:
        alegere = input('Dati ora de inceput si sfarsit a activitatii sau 0 pentru iesire: ')
        if int(alegere[0]) == 0:
            break
        else:
            n, m = alegere.split()
            n, m = int(n), int(m)
            activitati.append([n,m])
    return activitati

def afisareActivitati(activitati):
    for i in range(len(activitati)):
        print('Activitatea %-4s : %+4s - %+4s' % (i, activitati[i][0], activitati[i][1]))
    if len(activitati) <= 0:
        print('Nu avem activitati.')

def calendar(activitati):
    activitati.sort(key=itemgetter(1))
    rez = []
    rez.append(activitati[0])
    for i in range(len(activitati)):
        if rez[len(rez)-1][1] <= activitati[i][0]:
            rez.append(activitati[i])
    return rez