__author__ = 'Zanoni Devis'


def sort_list(lf):
    for x in range(1, len(lf)):
        j = x
        while j > 0 and lf[j][1] < lf[j-1][1]:
            lf[j], lf[j-1] = lf[j-1], lf[j]
            j -= 1
    return lf


def list_of_tuples(s):
    df = {}
    for i in s:
        if i in df:
            df[i] += 1
        else:
            df[i] = 1
    return [x for x in df.items()]


def merge_less_freqs(sl):
    diz_cod = {}
    while len(sl) > 1:
        low = sl.pop(0)
        high = sl.pop(0)
        
        for char in low[0]:
            diz_cod[char] = '0' + diz_cod.get(char, '')
        for char in high[0]:
            diz_cod[char] = '1' + diz_cod.get(char, '')
            
        sl.append((low[0] + high[0], low[1] + high[1]))
        
    return diz_cod


def print_codifica(d, c):
    print("codifica di " + d, end=": ")
    for x in d:
        print(c[x], end='')


def main():
    data = input("Inserisci la stringa: ")
    list_freqs = list_of_tuples(data)
    sorted_list = sort_list(list_freqs)
    print(sorted_list)
    cod = merge_less_freqs(sorted_list)
    print(cod)
    print_codifica(data, cod)      


main()
