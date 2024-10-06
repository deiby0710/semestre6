from bed.lineales.lse import Lista_SE
class Carro:
    """Implementa el funcionamiento de un carro que tiene placa,marca y modelo
    teniendo en cuenta lo siguiente:
    - La placa debera tener un formato que sera el siguiente: 'LLLNNN', donde L es letra
    y N es numero
    - El modelo minimo valido sera el año 2000. Tambien el año 2000 sera el valor por defecto
    cuando no se pase el modelo
    """
    def __init__(self,placa,marca,modelo=2000):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo # self.modelo llama al setter
    

    @property
    def modelo(self):# Tiene que ser el mismo nombre del atributo
        return self.__modelo
    @modelo.setter
    def modelo(self,año_modelo):
        if año_modelo>=2000:
            self.__modelo = año_modelo
        else:
            raise ValueError('El modelo supera el año 2000')
    
    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self,placa_asignada):
        letras = placa_asignada[:3]
        numeros = placa_asignada[4:7]
        if letras.isalpha():
            if numeros.isdigit():
                self.__placa = placa_asignada
                return True
        raise ValueError('La placa debe tener el siguiente formato: LLL NNN')


    def __str__(self):
        return f"{self.placa}/{self.marca}/{self.modelo}"
    def __eq__(self,otro_carro):
        # if self.placa==otro_carro.placa and self.marca==otro_carro.marca:
        #     return True   
        # return False
        if isinstance(otro_carro,Carro):
            return True if self.placa==otro_carro.placa and self.marca==otro_carro.marca else False
        return False


class CarroPirata:
    def __init__(self,placa,marca,modelo=2000):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

if __name__=='__main__':
    lst_cars = Lista_SE()
    car1 = Carro('ABC 123', "Renault",2015)
    lst_cars.adicionar(car1)
    lst_cars.adicionar(Carro("RTY 789","Mazda",2010))
    lst_cars.adicionar(Carro("QWE 192","Toyota",2002))
    lst_cars.adicionar(Carro("PQE 852","NISSAN",2000))
    lst_cars.recorrer()
    print("Buscar: ", lst_cars.encontrar(car1)) # Lo encuentra porque es el mismo objeto de memoria
    print("Buscar: ", lst_cars.encontrar(Carro("PQE 852","NISSAN",2000)))# NO lo encuentra porque no esta en la misma referencia de la memoria. Lo resolvemos con __eq__
    # car2 = Carro("ABC 123","Renault",2001)
    car2 = CarroPirata("ABC 123","Renault",2001) # Desde que tengan los mismos atributos, py compara 
    print(car1==car2) # car1.__eq__(car2)
    # car2 = Carro("ABC 123","Renault",1999) # Lanza error
    car2 = Carro("ABC 123","Renault") # Lanza error
    car2.modelo = 2000 # Para solucionar esto usamos los getter and setter pero en py no existe 
    print(car2)
    car3 = Carro('AGS 21','Lamborgini',2020)
    print(car3)
