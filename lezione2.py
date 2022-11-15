def sum_list(lista):
    somma = 0
    for item in lista:
        somma = somma + item
    if(len(lista) == 0):
        return None
    else:
        return somma