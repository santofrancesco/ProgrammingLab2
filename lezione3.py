def sum_csv(file_name):
    somma = 0.0
    my_file = open(file_name, 'r')
    for line in my_file:
        elements = line.strip('\n').split(',')
        if elements[0] == 'Date':
            continue
        else:
            try:
                somma = somma + float(elements[1])
            except ValueError:
                print('Error: detected string value, expected int or float')
                
    if somma == 0.0:
        return None
    return somma

#test = sum_csv('shampoo_sales.csv')
#print(test)