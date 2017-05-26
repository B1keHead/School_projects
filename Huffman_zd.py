__author__ = 'Zanoni Devis'


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
    print("codifica", end=": ")
    final_cod = ''
    for x in d:
        final_cod += c[x]
    if (len(final_cod) % 8) != 0:
        for x in range(8 - len(final_cod) % 8):
            final_cod += '0'
    print(final_cod)


def main():
    d = open("Input.txt")
    data = d.read()
    d.close()
    list_freqs = list_of_tuples(data)
    sorted_list = sorted(list_freqs, key = lambda freq: freq[1])
    print(sorted_list)
    cod = merge_less_freqs(sorted_list)
    print(cod)
    print_codifica(data, cod)


main()
