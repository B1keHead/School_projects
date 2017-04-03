import time
'''
Author: me
'''
cc = 7
charlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Questo programma cripta del testo sueguendo una logicas fissa")


def crypt(cc, charlist):
    text = str(input("Inserisci il testo da criptare: "))
    print("Ecco il testo criptato: ", end='')
    for i in text:
        index = 0
        i.lower()
        if not i in charlist:
            print(i, end='')
        else:
            for x in charlist:
                if i == x:
                    print(charlist[index + cc], end='')
                else:
                    index += 1
                    while cc + index >= len(charlist):
                        cc -= 26
        cc += 3


def decrypt(cc, charlist):
    text = str(input("Inserisci il testo da decriptare: "))
    print("Ecco il testo decriptato: ", end='')
    for i in text:
        index = 0
        i.lower()
        if not i in charlist:
            print(i, end='')
        else:
            for x in charlist:
                if i == x:
                    while index - cc < 0:
                        index += 26
                    print(charlist[index - cc], end='')
                else:
                    index += 1
        cc += 3


def menu():
    print("Decidi cosa vuoi fare:", "\n", "1 - Cripta il testo",
          "\n", "2 - Decripta il testo", "\n", "3 - Spiegazione riguardo alla logica "
          "usata", "\n", "4 - Termina il programma")


def choice():
    c = str(input("Scelta: "))
    if c == '1':
        print('')
        crypt(cc, charlist)
        print('')
        print('')
        main()
    elif c == '2':
        print('')
        decrypt(cc, charlist)
        print('')
        print('')
        main()
    elif c == '3':
        print('')
        print("Non ho voglia di spiegare")
        print('')
        main()
    elif c == '4':
        print('')
        print("Il programma si sta chiudendo...")
        time.sleep(1.5)
    else:
        print("Scelta non valida, devi scegliere tra 1, 2, 3 e 4")
        choice()


def main():
    menu()
    choice()


main()