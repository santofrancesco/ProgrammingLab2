class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):

        if(type(data) != list):
            raise TypeError("Errore: l'input inserito non è una lista")
        
        prev_value = 0
        increment = 0
        prediction = None
        i=0
        for item in data:

            if(type(item) != (int or float)):
                raise TypeError('Errore: rilevato elemento non numerico dentro la lista: {}'.format(item))
            
            if(len(data)==1):
                raise Exception('Errore: la lista contiene un solo elemento')
            elif(i==0):
                prev_value = item
                i+=1
                continue
            else:   
                increment = increment + (item - prev_value) 
                prev_value = item
                i+=1

        prediction = data[-1] + (increment/(i-1))
        return prediction

'''test1 = IncrementModel()
print(test1.predict([50,52,60]))'''