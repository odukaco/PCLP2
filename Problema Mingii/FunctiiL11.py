nrsol = 0
dx = [1, 0, -1, 0, 1, -1, -1, 1]        # fiecare posibila miscare a mingii pe axele x si y (8 directii)
dy = [0, -1, 0, 1, 1, -1, 1, -1]

def citMatFisier(fisier='in.txt'):
    global n, Mat, x0, y0, Cale         # pentru a folosi valori din afara def(): pui global
    with open ('%s' % (fisier), 'rt') as f:     # citeste matricea din fisier
        n= int(f.readline())
        Mat = []
        Cale = [None] * n
        for j in range(n):
            Mat.append([int(i) for i in f.readline().split()])
            Cale[j] = [0] * n
        x0 = int(f.readline())      # pozitia initiala a mingii
        y0 = int(f.readline())
        return(n, Mat, Cale, x0, y0)

def citMatTastatura():
    global n, Mat, x0, y0, Cale
    n= int(input('Dati marimea matricei Mat n = '))
    Mat = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        Mat[i] = [int(x) for x in input('Dati elementele de pe linia ' + str(i) + ' : ').split()]
    Cale = [None] * n
    for i in range(n):
        Cale[i] = [0] * n
    x0 = int(input('Dati coordonata initiala a mingii pe axa x = '))
    y0 = int(input('Dati coordonata initiala a mingii pe axa y = '))
    return(n, Mat, Cale, x0, y0)

def peMargine(x, y):
    global n
    return x == 0 or x == n-1 or y == 0 or y == n-1

def inAfaraZonei(x, y):
    global n
    return x < 0 or x > n - 1 or y < 0 or y > n - 1

def afisSolutia():
    global Cale, nrsol
    nrsol += 1
    print('Solutia', nrsol, ':')
    afisMatrice(Cale)

fisiersters = False

def scrieSolutia(fisier):
    global Cale, nrsol, fisiersters
    nrsol += 1
    if not fisiersters:
        f = open ('%s' % (fisier), 'w')     # sterge continutul fisierului
        f.close()
        fisiersters = True
    with open ('%s' % (fisier), 'a') as f:      # a - append
        f.write('Solutia' + str(nrsol) + ':\n')
        n = len(Cale)
        for i in range(n):
            for j in range(n):
                f.write(str(Cale[i][j]) + '\t')
            f.write('\n')

def afisMatrice(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            print(str(mat[i][j]) + '\t', end='')
        print()

def posibil(x, y, xn, yn):
    global Mat, Cale
    return Mat[x][y] > Mat[xn][yn]

fisierales = False
fisier = ''

def cautaCale(k, x, y, mod):
    global n, Cale, fisierales, fisier
    if peMargine(x, y):
        if mod:
            if not fisierales:
                fisier = str(input('Dati fisierul .txt in care salvam solutiile: ') + '.txt')
                fisierales = True
            scrieSolutia(fisier)
        else:
            afisSolutia()
    for i in range(8):
        xn = x + dx[i]
        yn = y + dy[i]
        if not inAfaraZonei(xn, yn) and posibil(x, y, xn, yn):
            Cale[xn][yn] = k
            cautaCale(k+1,xn,yn, mod)
            Cale[xn][yn]= 0