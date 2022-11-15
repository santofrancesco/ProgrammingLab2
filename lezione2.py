my_list = [1,2,3,4]

def sum_list(lista):
    somma = 0
    for item in lista:
        somma = somma + item
    return somma

risultato = sum_list(my_list)

print(risultato)