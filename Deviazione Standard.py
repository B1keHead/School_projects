from math import sqrt
author = 'Zanoni Devis'


def get_list(n, numbers_list):
    print("Inserisci i numeri che vuoi (uno alla volta)."
          " Quando hai finito inserisci 'e'." + '\n'
          + "Se inserisci 'e' senza aver messo numeri"
          " ti appare un bell' errore di" + '\n'
          + "divisione con zero", '\n')
    while True:
        n = input("Inserisci numero: ")
        if "." in n or n.isnumeric():
            numbers_list.append(float(n))
        elif n == 'e':
            break
        else:
            print("Devi inserire solo numeri")
    numbers_list.sort()
    print("La lista dei numeri è:", numbers_list)
    return numbers_list


def calculate(n, numbers_list):
    l = get_list(n, numbers_list)

    # media
    media = sum(l)/len(l)
    print("Media:", media)

    # mediana
    if len(l) % 2 == 0:
        print("Mediana:", (l[len(l)//2] + l[len(l)//2-1])/2)
    else:
        print("Mediana:", l[len(l)//2])

    # errore massimo
    mmm = (l[len(l)-1]-l[0])/2
    print("Errore massimo:", mmm)

    # deviazione standard
    sommatoria = 0
    for i in l:
        sommatoria += (media - i)**2
    std_dev = sqrt(sommatoria/len(l))
    print("Deviazione standard:", std_dev)

    # errore relativo percentuale
    rel_err = (std_dev/media)*100
    print("Errore relativo percentuale:", str(rel_err) + "%")


def main():
    n = ''
    numbers_list = []
    calculate(n, numbers_list)


if __name__ == '__main__':
    main()
