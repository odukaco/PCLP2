def citireFisier(fisier='in.txt'):
    with open ('in.txt', 'rt') as f:
        global nrpoduri, podul, sol
        nrpoduri = int(f.readline())
        start = str(f.readline().strip())
        podul = [f.readline().strip().split() for i in range(nrpoduri)]
        sol = [None] * nrpoduri
        for j in range(nrpoduri):
            for i in podul:
                if i == []:
                    podul.remove(i)
        if len(podul) < nrpoduri:
            print('Fisierul contine date eronate.')
            dateeronate = True
        else:
            dateeronate = False
    return nrpoduri, start, podul, fisier, dateeronate

def Posibil(i, counter, ins_crt):
    for j in range(counter):
        if sol[j] == i:
            return False
    return podul[i][0] == ins_crt or podul[i][1] == ins_crt

nrsol = 0

def resetSol():
    global nrsol
    nrsol = 0

def afisSol(nrpoduri, sol):
    global nrsol
    nrsol += 1
    print('\nSolutia ' + str(nrsol) + ' :')
    for i in range(nrpoduri-1):     # -2
        print(sol[i], end = '  >  ')
    print(sol[nrpoduri-1])      # -1
def verificareFaraSolutii():
    global nrsol
    if nrsol < 1:
        print('\nNu au fost gasite solutii pentru problema.')

def Plimbare(ins_crt, counter=0):
    if counter == nrpoduri:
        afisSol(nrpoduri, sol)
    else:
        for i in range(nrpoduri):
             if Posibil(i, counter, ins_crt):
                 sol[counter] = i
                 if ins_crt == podul[i][0]:
                     ins = podul[i][1]
                 elif ins_crt == podul[i][1]:
                     ins = podul[i][0]
                 Plimbare(ins, counter+1)

def citireTastatura():
    global nrpoduri, podul, sol
    nrpoduri = int(input('Dati numarul de poduri: '))
    start = int(input('Dati insula de inceput: '))
    podul = [None] * nrpoduri
    for i in range(nrpoduri):
        podul[i] = [int(x) for x in input('Dati insulele conectate de podul ' + str(i+1) + ' : ').split()]
    sol = [None] * nrpoduri
    return (nrpoduri, start, podul)
def afisarePoduri():
    global nrpoduri, podul
    for i in range(nrpoduri):
        for j in range(2):
            print('\t' + str(podul[i][j]), end = '\t')
        print()