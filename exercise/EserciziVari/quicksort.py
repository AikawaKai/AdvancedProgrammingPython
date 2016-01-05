def quicksort(lista):
    if len(lista) == 0:
        return []
    else:
        return quicksort([x for x in lista[1:] if x < lista[0]]) + \
               [lista[0]] + \
               quicksort([x for x in lista[1:] if x >= lista[0]])


if __name__ == '__main__':
    print(quicksort([2, 1, 5, 3, 4, 7, 4]))
