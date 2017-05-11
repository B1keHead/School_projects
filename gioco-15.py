from random import shuffle
from os import system

__author__ = 'Zanoni Devis'


def print_matrix(m):
    print()
    for x in m:
        for i in x:
            print(i, end='\t')
        print('\n')


def next_move():
    move = input("Scegli che numero spostare: ")
    if not move.isnumeric():
        print("Devi inserire un numero")
        return next_move()
    elif int(move) > 15 or int(move) < 1:
        print("Deve essere un numero da 1 a 15")
        return next_move()
    return int(move)


def swipe_items(m):
    while m != [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, " "]]:
        move = next_move()
        bi = find_index(m, " ")
        mi = find_index(m, move)

        # prima riga
        if bi[0] == 0:
            if 0 < bi[1] < 3:
                if m[bi[0]][bi[1]] == m[mi[0]-1][mi[1]] or m[bi[0]][bi[1]] == m[mi[0]][mi[1]-1] or m[bi[0]][bi[1]] == m[mi[0]][mi[1]+1]:
                    m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]

            elif bi[1] == 3:
                if m[bi[0]][bi[1]] == m[mi[0]-1][mi[1]] or m[bi[0]][bi[1]] == m[mi[0]][mi[1]+1]:
                    m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]

            elif bi[1] == 0:
                if m[bi[0]][bi[1]] == m[mi[0]-1][mi[1]] or m[bi[0]][bi[1]] == m[mi[0]][mi[1]-1]:
                    m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]

        # seconda e terza riga
        elif bi[0] == 1 or bi[0] == 2:
            if 0 < bi[1] < 3:
                if m[bi[0]][bi[1]] == m[mi[0]][mi[1]-1] or m[bi[0]][bi[1]] == m[mi[0]][mi[1]+1] or m[bi[0]][bi[1]] == m[mi[0]-1][mi[1]] or m[bi[0]][bi[1]] == m[mi[0]+1][mi[1]]:
                    m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]

            elif bi[1] == 3:
                if mi[1]+1 >= 4:
                    if m[bi[0]][bi[1]] == m[mi[0]-1][mi[1]]:
                        m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]
                # elif mi[0]+1 >= 4:
                    # dio porcooooooooooooo
                else:
                    if m[bi[0]][bi[1]] == m[mi[0]][mi[1]+1]:
                        m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]

            elif bi[1] == 0:
                if m[bi[0]][bi[1]] == m[mi[0]-1][mi[1]] or m[bi[0]][bi[1]] == m[mi[0]+1][mi[1]] or m[bi[0]][bi[1]] == m[mi[0]][mi[1]-1]:
                    m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]

        # quarta riga
        elif bi[0] == 3:
            if 0 < bi[1] < 3:
                if m[bi[0]][bi[1]] == m[mi[0]][mi[1]-1] or m[bi[0]][bi[1]] == m[mi[0]][mi[1]+1] or m[bi[0]][bi[1]] == m[mi[0]+1][mi[1]]:
                    m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]

            elif bi[1] == 3:
                if mi[1]+1 >= 4:
                    if m[bi[0]][bi[1]] == m[mi[0]+1][mi[1]]:
                        m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]
                else:
                    if m[bi[0]][bi[1]] == m[mi[0]][mi[1]+1]:
                        m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]

            elif bi[1] == 0:
                if m[bi[0]][bi[1]] == m[mi[0]][mi[1]-1] or m[bi[0]][bi[1]] == m[mi[0]+1][mi[1]]:
                    m[bi[0]][bi[1]], m[mi[0]][mi[1]] = m[mi[0]][mi[1]], m[bi[0]][bi[1]]

        # da finire con gli if >= 4 per evitare errori

        system("cls")
        print_matrix(m)

    print("Hai vinto!")


def find_index(m, val):
    counter = 0
    for x in m:
        for i in x:
            if i == val:
                return counter, x.index(i)
        counter += 1


def main():
    nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, " "]
    shuffle(nlist)
    matr = [nlist[i * len(nlist) // 4: (i+1) * len(nlist) // 4] for i in range(4)]
    print_matrix(matr)
    swipe_items(matr)


main()
