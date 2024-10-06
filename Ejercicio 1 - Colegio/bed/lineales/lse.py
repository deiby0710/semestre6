# DEIBY ALEJANDRO DELGADO ESTRADA
# print("NAME:", __name__, "PAQUETE:", __package__)
if __name__ == "__main__" and __package__ is None:
    from nodos import Nodo_listaSE
else:
    # from .nodos import Nodo_listaSE
    from bed.lineales.nodos import Nodo_listaSE

class Lista_SE:
    """Clase que implementa el funcionamiento de una lista simplemente enlazada
    """

    # (1) Método Constructor
    def __init__(self):
        """Método que realiza la creación e inicialización de la
        Lista Simplemente Enlazada.
        """
        self.__cab = None        

    # (2) Método es_vacia
    def es_vacia(self):
        """Método que verifica si la lista se encuentra vacía.

        Returns
        -------
        bool
            Retorna True si la lista es vacia. False en caso contrario.
        """
        return self.__cab is None

    # (3.1) Método adicionar al final de la lista
    def adicionar(self, nuevo_dato):
        """ Método que adiciona un nuevo nodo al final de la lista.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.

        Returns
        -------
        bool
            True cuando el dato es añadido en la lista. False en caso
            contrario.
        """
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        if self.es_vacia():
            self.__cab = nuevo_nodo
        else:
            actual  = self.__cab
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo_nodo
        
    
    # (3.2) CONSULTAR: Método posicionar
    def posicionar(self, nuevo_dato, pos=0):
        """Método que inserta un nuevo nodo en cualquier posición de la
        lista. Si la lista está vacía la única posición válida será
        cero. Si la lista ya contiene datos, serán válidas posiciones
        intermedias o la posición inmediatemente superior a la del último dato.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.
        pos : int, optional
            Posición a insertar en la lista, por defecto 0.

        Returns
        -------
        bool
            True cuando el dato es insertado en la lista. False en caso
            contrario.
        """
        nodo = Nodo_listaSE(nuevo_dato)
        if self.es_vacia():
            if pos == 0:
                self.__cab = nodo
                return True
            return False
        nodo_actual = self.__cab
        indice = 0
        nodo_anterior = None
        if pos==0:
            nodo.sig = self.__cab
            self.__cab = nodo
            return True
        while nodo_actual and indice<pos:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig
            indice+=1
        if indice==pos:
            nodo_anterior.sig = nodo
            nodo.sig = nodo_actual
            return True
        else:
            return False

    # (4) Método recorrer una lista
    def recorrer(self):
        """Método que recorre la lista, imprimiendo cada uno de los datos que
        contenga, siempre y cuando no sea una lista vacía.
        """
        nodo_actual = self.__cab
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = nodo_actual.sig

    # (5.1) Método econtrar un dato en la lista por dato
    def encontrar(self, dato_buscar):
        """Método que realiza la búsqueda de un dato en la lista.

        Parameters
        ----------
        dato_buscar : object
            Corresponde al valor del dato a ser encontrado en la lista.

        Returns
        -------
        object|None
            object si se encuentra el dato en la lista, None en caso contrario.
        """
        nodo_actual = self.__cab
        while nodo_actual:
            if nodo_actual.dato==dato_buscar:
                return nodo_actual
            nodo_actual = nodo_actual.sig

    # (5.2) CONSULTA: Método ubicar un dato por posición en la lista
    def ubicar(self, pos):
        """Método que realiza la búsqueda de un dato en la lista dependiendo
        de la posición ingresada.

        Parameters
        ----------
        pos : int
            Corresponde a la posición en la lista a ubicar el dato.

        Returns
        -------
        object|None
            object si el dato es ubicado en la lista, None en caso contrario.
        """
        nodo_actual = self.__cab
        indice = 0
        while nodo_actual and indice<=pos:
            if indice==pos:
                return nodo_actual
            nodo_actual = nodo_actual.sig
            indice += 1

    # (6) Método remover por dato (* CONSULTA) o posición
    def remover(self, item, por_pos=True):
        """Método que permite remover un nodo de la lista ya sea por una
        posición o por el dato correspondiente. Si es por dato, deberá
        remover cada uno de los nodos que contenga dicho dato.

        Parameters
        ----------
        item : object|int
            Puede corresponder al valor del dato a ser removido de la lista
            o a la posición en la lista a remover el dato.
            En el caso de remover por dato, se buscará todas las coincidencias
            del dato a eliminar en la lista y serán quitadas.
        por_pos : bool, optional
            Si es True, el método intentará remover un dato por su posición,
            de lo contrario se intentará hacerlo por su valor, por defecto True.

        Returns
        -------
        bool
            True cuando el dato es removido de la lista. False en caso
            contrario.
        """
        if por_pos:
            return self.__remover_pos(item)
        else:
            # CONSULTA: remover por dato
            return self.__remover_dato(item)

    # (6.1) Método oculto remover por posición
    def __remover_pos(self, pos_elim):
        actual = self.__cab
        indice = 0 
        anterior = None
        if pos_elim>=0:
            while actual and indice<pos_elim:
                anterior = actual
                actual = actual.sig
                indice+=1
            if indice == 0 and actual:
                self.__cab = actual.sig
            elif actual:
                anterior.sig = actual.sig
        return True if actual and pos_elim==indice else False

    # (6.2) CONSULTAR: Método oculto remover por dato
    def __remover_dato(self, dato_eliminar):
        if isinstance(dato_eliminar,Nodo_listaSE):
            dato_eliminar = dato_eliminar.dato
        nodo_actual = self.__cab
        nodo_anterior = None
        while nodo_actual:
            if nodo_actual.dato==dato_eliminar:
                if nodo_anterior:
                    nodo_anterior.sig= nodo_actual.sig
                else:
                    self.__cab = nodo_actual.sig
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.sig

    # (7) CONSULTA: Método __str__
    def __str__(self):
        """Método que devuelve una cadena con los datos de la lista, o una
        cadena vacía en el caso de que la lista sea vacía.

        Returns
        -------
        str
            Si la lista no es vacía retornará una cadena en el foramato:
                "(dato_0) :>: (dato_1) :>: (dato_2) :>: ... :>: (dato_n)"
                "(7) :>: (8) :>: (5) :>: (5) :>: (9)"
            de lo contrario retornará una cadena vacía: ""
        """
        actual = self.__cab
        cadena = ''
        while actual:
            cadena += (f'({actual.dato})')
            if actual.sig:
                cadena += f' :>: '
            actual = actual.sig
        return cadena

    # (8) CONSULTAR: Sobre-escritura del método __len__
    def __len__(self):
        """Método que calcula el tamaño de la lista.

        Returns
        -------
        int
            El número de nodos que tiene la lista.
        """        
        actual = self.__cab
        i = 0
        while actual:
            i+=1
            actual = actual.sig
        return i
    
    # Método para hacer que la lista sea iterable
    def __iter__(self):
        self.actual = self.__cab
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration  # Termina la iteración
        else:
            valor = self.actual.dato
            self.actual = self.actual.sig
            return valor 


if __name__ == "__main__":
    list_num = Lista_SE()
    list_num.adicionar(7)
    list_num.adicionar(8)
    list_num.adicionar(10)
    list_num.adicionar(8)
    # list_num.posicionar(12,0)
    # list_num.posicionar(12,1)
    list_num.posicionar(12)
    # if list_num.encontrar(12):
    #     print(list_num.encontrar(1))
    # print(list_num.ubicar(1))
    # list_num.remover(0)
    # list_num.remover(12,False)
    # list_num.recorrer()
    print(list_num)
    # print(f'El numero de elementos es: {len(list_num)}')
    # for i in list_num:
    #     print(f'El dato del nodo es: {i}')
