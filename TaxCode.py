'''
Zanoni Devis, 3EI, 29/11/16,
scrivere la funzione checkCF() che esegue il controllo formale di un
codice fiscale. la funzione restituisce false nei casi in cui la stringa
fornita non rispetti le regole stabilite per il Codice Fiscale.
'''

cd = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}

dd = {
    "0": 1,
    "1": 0,
    "2": 5,
    "3": 7,
    "4": 9,
    "5": 13,
    "6": 15,
    "7": 17,
    "8": 19,
    "9": 21,
    "A": 1,
    "B": 0,
    "C": 5,
    "D": 7,
    "E": 9,
    "F": 13,
    "G": 15,
    "H": 17,
    "I": 19,
    "J": 21,
    "K": 2,
    "L": 4,
    "M": 18,
    "N": 20,
    "O": 11,
    "P": 3,
    "Q": 6,
    "R": 8,
    "S": 12,
    "T": 14,
    "U": 16,
    "V": 10,
    "W": 22,
    "X": 25,
    "Y": 24,
    "Z": 23
}

ed = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z"
}

mesise = {
          'A': '/01/',
          'B': '/02/',
          'C': '/03/',
          'D': '/04/',
          'E': '/05/',
          'H': '/06/',
          'L': '/07/',
          'M': '/08/',
          'P': '/09/',
          'R': '/10/',
          'S': '/11/',
          'T': '/12/',
          'a': '/01/',
          'b': '/02/',
          'c': '/03/',
          'd': '/04/',
          'e': '/05/',
          'h': '/06/',
          'l': '/07/',
          'm': '/08/',
          'p': '/09/',
          'r': '/10/',
          's': '/11/',
          't': '/12/',
            }

male = ('0', '1', '2', '3')
female = ('4', '5', '6', '7')


def checkTC(male, female):
    global c
    c = str(input("Inserisci il codice fiscale: "))
    months = ('A', 'B', 'C', 'D', 'E', 'H', 'L', 'M', 'P',
              'R', 'S', 'T', 'a', 'b', 'c', 'd', 'e', 'h',
              'l', 'm', 'p', 'r', 's', 't')
    if not c[:6].isalpha():
        print("Errore nell' inserimento del nome"
              "(i primi 6 caratteri devono essere alfabetici)")
        return checkTC(male, female)
    elif not c[6:8].isnumeric() and int(c[6:8]) > 17:
        print("Inserimento errato dell' anno di nascita")
        return checkTC(male, female)
    elif not c[8].isalpha() and not c[8] in months:
        print("Inserimento errato del mese di nascita")
        return checkTC(male, female)
    elif not c[9] in male and not c[9] in female:
        print("Inserimento errato del giorno di nascita")
        return checkTC(male, female)
    elif not c[9:11].isnumeric():
        print("Inserimento errato del giorno di nascita")
        return checkTC(male, female)
    elif not c[11].isalpha():
        print("Il dodicesimo carattere deve essere alfabetico")
        return checkTC(male, female)
    elif not c[12:15].isnumeric():
        print("I caratteri numero 13, 14 e 15 devono essere numerici")
        return checkTC(male, female)
    elif not c[15].isalpha():
        print("Il carattere di controllo deve essere alfabetico")
        return checkTC(male, female)
    elif len(c) != 16:
        print("Il codice inserito non è di 16 caratteri")
        return checkTC(male, female)
    else:
        return c


def un_equal(c, cd, dd):
    equal = []
    unequal = []
    EQUAL = []
    UNEQUAL = []
    ev = 0
    uv = 0
    for i in c:
        equal.append(i)
    equal.remove(equal[15])
    for x in equal[::2]:
        unequal.append(x)
        equal.remove(x)
    for m in range(len(equal)):
        f = equal[m].upper()
        EQUAL.append(f)
    for n in range(len(unequal)):
        u = unequal[n].upper()
        UNEQUAL.append(u)
    for j in EQUAL:
        ev = ev + cd[j]
    for k in UNEQUAL:
        uv = uv + dd[k]
    sv = ev + uv
    return sv


def control_digit(c, ed, male, female, mesise):
    cdc = un_equal(c, cd, dd) % 26
    if c[15].upper() != ed[cdc]:
        print("Errore nella cifra di controllo", '\n')
        main()
    elif c[9] in male:
        print('')
        print("La cifra di controllo è:", ed[cdc])
        print("Sesso: maschio")
        print("Data di nascita:", end=' ')
        print(c[9:11], end='')
        print(mesise[c[8]], end='')
        if c[6] == '0' or c[6] == '1':
            print(20, end='')
            print(c[6:8])
        else:
            print(19, end='')
            print(c[6:8])
    elif c[9] in female:
        print('')
        print("La cifra di controllo è:", ed[cdc])
        print("Sesso: femmina")
        print("Data di nascita:", end=' ')
        print((int(c[9:11])-40), end='')
        print(mesise[c[8]], end='')
        print(c[6:8])

def main():
    checkTC(male, female)
    un_equal(c, cd, dd)
    control_digit(c, ed, male, female, mesise)


main()
