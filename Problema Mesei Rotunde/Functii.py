def citireFisier(fisier='in.txt'):
    global n, concurente, asezat, sol, nsol
    nsol = 0
    with open(fisier, 'rt') as f:
        concurente = []
        n = int(f.readline())
        asezat = [False] * n
        sol = [[]] * n
        for i in range(n):
            concurente.append([int(j) for j in f.readline().split()])

def verifconcurenta(firma1, firma2):
    global concurente, asezat
    if concurente[firma1][firma2] > 0 or concurente[firma2][firma1] > 0:
        return True
    else:
        return False
def posibil(i, k):
    global concurente, n, sol
    if k > 0 and verifconcurenta(sol[k - 1], i):
        return False
    if k == n - 1 and verifconcurenta(sol[0], i):
        return False
    return True

def solutie():
    global nsol, sol, n
    print(f'Solutie {nsol}:', end = '\t')
    for i in range(n):
        print(sol[i], end = '\t')
    print()
    nsol += 1

def masaRotunda(k):
    global n, asezat, sol
    if k == n:
        solutie()
    else:
        for i in range(n):
            if not asezat[i] and posibil(i, k):
                asezat[i] = True
                sol[k] = i
                masaRotunda(k + 1)
                asezat[i] = False
