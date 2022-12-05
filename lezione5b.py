class CSVFile():

    def __init__(self, name):
        self.name = name
        try:
            with open(self.name) as test1:
                test1.readlines()
        except:
            print('Errore: file inserito non valido')
            

    def get_data(self):

        risultato = []
        with open(self.name) as my_file:
            for line in my_file:
                elements = line.strip('\n').split(',')
                if elements[0] != 'Date':
                    risultato.append(elements)
        return risultato



class NumericalCSVFile(CSVFile):

    def get_data(self):
        tmp = super().get_data()
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

        
shampoo1 = CSVFile('shampoo_sales.csv')
shampoo2 = NumericalCSVFile('shampoo_sales.csv')
print(shampoo1.get_data())
print(shampoo2.get_data())