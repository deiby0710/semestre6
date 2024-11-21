class Nodo_listaSE:
    def __init__(self,dato):
        """Metodo constructor de un nodo para una lista simplemente enlazada.

        Parameters
        ----------
        dato : object
            El dato que se pasa al nodo.
        """        
        self.dato = dato
        self.sig = None
    def __str__(self):
        """Metodo que retorna una cadena con el dato del nodo

        Returns
        -------
        str
            Cadena a ser retornada por el nodo, que incluye el dato
        """
        return f'{self.dato}' # str(self.dato)