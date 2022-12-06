class CSVFile():

    def __init__(self, name):
        self.name = name
        if(self.name == ''):
            raise Exception('Errore: file vuoto')
        if(type(name) != str):
            raise Exception('Errore: nome del file non è una stringa!')
        try:
            with open(self.name) as test1:
                test1.readlines()
        except:
            print('Errore: file inserito non valido')
            

    def get_data(self, start=None, end=None):

        #conto il numero di righe nel file
        numero_di_righe = 0;
        for row in open(self.name):
            numero_di_righe+=1
        
        #controllo start
        if(start == None ):
            start = 1
        elif(type(start)==int or type(start)==float):
            if(start <= 0):
                raise Exception('Errore: start è minore o uguale a zero')
            elif(start > numero_di_righe):
                raise Exception('Errore: start più grande del numero di righe')
        else:
            try:
                start = int(start)        
                
            except:
                print('Errore: start non è un valore numerico: {}'.format(start))
                
        #controllo end
        if(end==None):
            end = numero_di_righe
        elif(type(end)==(int or float)):
            if(end <= 0):
                raise Exception('Errore: end è minore o uguale a zero')
            elif(end > numero_di_righe):
                raise Exception('Errore: end più grande del numero di righe')
        else:
            try:
                end = int(end)

            except:
                print('Errore: end non è un valore numerico: {}'.format(end))

        #controllo se end è minore di start
        if((end!=start) and (end<start)):
            raise Exception('Errore: end è più piccolo di start (start={}, end={})'.format(start, end))

        #CUORE DEL PROGRAMMA
        risultato = []
        i = 0
        with open(self.name) as my_file:
            for line in my_file:
                if(i in range(start-1, end)):
                    elements = line.strip('\n').split(',')
                    if(elements == ''):
                        i+=1
                        continue                     
                    elif(elements[0] == 'Date'):
                        i+=1
                        continue
                    else:
                        risultato.append(elements)
                        i+=1
                else:
                    i+=1
                    continue
        return risultato


class NumericalCSVFile(CSVFile):

    def get_data(self, *args, **kwargs):
        tmp = super().get_data(*args, **kwargs)
        i = 0
        while (i < len(tmp)):
            if(tmp[0][0]=='Date' or tmp[0][1]=='Sales'):
                i += 1
                continue
            else:
                try:
                    j = 1
                    for item in tmp[i]:
                        try:
                            tmp[i][j] = float(tmp[i][j])
                            j += 1
                        except IndexError:
                            pass
                except:                   
                    print('Errore: non è stato possibile convertire "{}" a float'.format(tmp[i][j]))
                    tmp[i][j] = 0.0
            i += 1
        
        return tmp

        
'''shampoo1 = CSVFile('shampoo_sales.csv')
shampoo2 = NumericalCSVFile('shampoo_sales.csv')
print(shampoo1.get_data())
print('\n')
print(shampoo2.get_data())'''