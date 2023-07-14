from operator import itemgetter
def citesteFisier():
    with open ('in.txt', 'rt') as f:
        global obiecte, V, n
        V = float(f.readline())
        n = int(f.readline())
        obiecte = []
        for i in range(n):
            obiecte.append([float(i) for i in f.readline().split()])
        print(V, n, obiecte)
citesteFisier()
def Greedy():
    global obiecte, n , V, sol
    for i in range(n):
        obiecte[i].append(obiecte[i][0] / obiecte[i][1])
    obiecte = sorted(obiecte, key=itemgetter(2), reverse=True)
    sol = [[0]] * n
    i = 0
    vt = pt = 0
    while vt < V and i <= n-1:
        if vt + obiecte[i][1] <= V:
            sol[i] = 1
            pt = pt + obiecte[i][0]
            vt = vt + obiecte[i][1]
        else:
            sol[i] = (V-vt)/obiecte[i][1]
            vt = V
            pt = pt + obiecte[i][0] * sol[i]
        i = i + 1
    print('Pretul total al obiectelor: ', pt, '\nVolumul ocupat: ', vt)
    print('In rucsac s-a introdus: ')
    for i in range(n):
        if sol[i] > 0:
            print('Obiectul', i+1, '(', obiecte[i][1]*sol[i], ',', obiecte[i][0], ')')
citesteFisier()
Greedy()
