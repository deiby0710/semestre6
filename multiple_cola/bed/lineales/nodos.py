#Listas Simplemente Enlazadas

class Nodo_listaSE:
    """Clase que modela un nodo para el tipo de estructa Lista Simplemte 
    Enlazada.
    """
    def __init__(self,dato):
        """Método Constructor de un nodo para una lista simplemente enlazada.

        Parameters
        ----------
        dato : object
            El dato que se pasa al nodo 
        """
        self.dato = dato
        self.sig = None 
    
    def __str__(self): #metodo magico para convertir nodos a cadenas
        """Método que retorna una cadena con el dato de  del nodo.

        Returns
        -------
        str             
            la cadena a ser retornada por el nodo.
        """
        return f"{self.dato}"