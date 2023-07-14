from operator import itemgetter

def bancomatLimitat (suma, bancnote, afis=True):
    bancnote_sortate = dict(sorted(bancnote.items(), key = itemgetter(0), reverse=True))
    if afis:
        print('Suma = ', suma, 'Bancnote disponibile:', bancnote_sortate)
    rez = []
    keylist = list(bancnote_sortate.keys())
    while (suma > 0):
        if len(keylist) == 0:
            break
        if suma >= keylist[0] and bancnote_sortate.get(keylist[0]) > 0:
            nr_bancnote = 0
            while suma >= keylist[0] and bancnote_sortate.get(keylist[0]) > 0:
                suma -= keylist[0]
                nr_bancnote += 1
                bancnote_sortate[keylist[0]] -= 1
            rez.append([keylist[0], nr_bancnote])
        keylist.pop(0)
    else:
        return rez
    return []

def citireFisier(fisier='in.txt'):
    bancnote = {}
    with open (fisier, 'rt') as f:
        for line in f.readlines():
            splitlinie = line.split()
            n = int(splitlinie[0])
            m = int(splitlinie[1])
            bancnote[n] = m
    return bancnote

def citireTastatura():
    bancnote = {}
    while 1:
        introducere = input('Introduceti valoarea bancnotei si cate bancnote avem (sau 0 pentru terminare): ')
        if introducere == '0':
            break
        n, m = introducere.split()
        n, m = int(n), int(m)
        bancnote[n] = m
    return bancnote

def afisareBancomat(bancnote):
    bancnote_sortate = dict(sorted(bancnote.items(), key=itemgetter(0)))
    keylist = list(bancnote_sortate.keys())
    for i in range(len(keylist)):
        print(bancnote_sortate[keylist[i]], '\tbancnote de\t', keylist[i])