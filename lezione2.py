def sum_list(lista):
    if(len(lista) == 0):
        return None   
    else:
        somma = 0
        for item in lista:
            somma = somma + item
        return somma