from nodos import Nodo_listaSE

class Lista_CSE:
    """Clase que implementa el funcionamiento de una lista Circular 
    Simplemente Enlazada.
    """
    
    def __init__(self):
        """Método que realiza la creación e inicialización de la 
        Lista Circular Simplemente Enlazada.
        """
        self.primero = None
        self.ultimo = None

    def es_vacia(self):
        """Método que comprueba si la lista se encuentra vacía.

        Returns
        -------
        bool
            Retorna True si la lista es vacía 
            False en caso contrario.
        """
        return self.primero == None
    
    def adicionar(self, nuevo_dato):
        """Método que adiciona un nuevo nodo al final de la lista.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.

        Returns
        -------
        bool
            True si el dato es añadido en la lista, False en caso contrario.
        """
        if self.es_vacia():
            nuevo_nodo = Nodo_listaSE(nuevo_dato)
            self.primero = self.ultimo = nuevo_nodo
        else:
            aux = self.ultimo
            self.ultimo = aux.sig = Nodo_listaSE(nuevo_dato)
            self.ultimo.sig = self.primero
        return True

    def posicionar(self, nuevo_dato, pos_rel=0):
        """Método que inserta un nuevo nodo en cualquier posición de la
        lista. Si la lista está vacía la única posición válida será
        cero. Si la lista ya contiene datos, serán válidas posiciones
        intermedias o la posición inmediatamente superior a la del último dato.             

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.
        pos_rel : int, optional
            Posición a insertar en la lista, por defecto será 0
        """
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        if pos_rel == 0:
            nuevo_nodo.sig = self.primero
            self.primero = nuevo_nodo
            self.ultimo.sig = self.primero
        else:
            contador = 0
            nodo_posicion = self.primero
            while contador < pos_rel:
                contador += 1
                nodo_posicion = nodo_posicion.sig
            nuevo_nodo.sig = nodo_posicion.sig
            nodo_posicion.sig = nuevo_nodo
        
    def remover(self, item, por_pos=True):
        """Método que remueve un nodo de la lista ya sea por posición
        o por  dato. Si es por dato se deberá  remover cada una de las
        coincidencias existentes en otro nodos.

        Parameters
        ----------
        item : object|int
            Corresponede al valor del dato a ser removido de la lista
            o la posición en la lista a remover el dato.
            
        por_pos : bool, optional
            Si es True, se removera un dato por su posición,  de lo
            contrario se removera por su valor, por defecto True.

        Returns
        -------
        bool
            True cuando el dato es removido de la lista, False en caso
            contrario.
        """
        if por_pos:
            return self.__remover_pos(item)
        else:
            return self.__remover_dato(item)
    
    def __remover_pos(self, pos_elim):
        """Método que permite eliminar un nodo por posición.

        Parameters
        ----------
        pos_elim : int
            posición del nodo a eliminar.

        Returns
        -------
        bool
            Retorna True si el nodo es eliminado con éxito, False en 
            caso contrario.
        """
        if self.es_vacia():
            return False
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
            return True
        elif pos_elim == 0:
                self.ultimo.sig = self.primero.sig
                self.primero = self.ultimo.sig
                return True
        else:
            aux = self.primero
            counter = 0
        
            while counter < pos_elim - 1:
                aux = aux.sig
                counter += 1
            
            aux.sig = aux.sig.sig

            if aux.sig == self.primero:
                self.ultimo = aux
            return True
    
    def __remover_dato(self, dato_eliminar):
        """Método que permite eliminar un nodo en referencia a un dato.

        Parameters
        ----------
        dato_eliminar : object
            Dato que contiene el nodo a ser eliminado.

        Returns
        -------
        bool
            Retorna True si el dato fue eliminado con éxito, False en
            caso contrario.
        """
        if self.es_vacia():
            return False
        
        aux = self.primero
        anterior = None

        if aux.dato == dato_eliminar:
            if self.primero == self.ultimo:
                self.primero = None
                self.ultimo = None
            else:
                self.ultimo.sig = self.primero.sig
                self.primero = self.primero.sig
            return True

        while aux.sig != self.primero:
            if aux.dato == dato_eliminar:
                break
            anterior = aux
            aux = aux.sig

        if aux.dato != dato_eliminar:
            return False

        anterior.sig = aux.sig

        if aux == self.ultimo:
            self.ultimo = anterior

        return True
        
        
    def encontrar(self, dato_buscar):
        """Método que realiza la búsqueda de un dato en la lista.

        Parameters
        ----------
        dato_buscar : object
            Corresponde al valor del dato a ser encontrado en la lista.

        Returns
        -------
        object|None
            object si se encuentra el dato en la lista, None en caso contrario
        """
        if dato_buscar == self.primero.dato:
            return self.primero.dato
        elif dato_buscar == self.ultimo.dato:
            return self.ultimo.dato
        else:
            aux1 = self.primero.sig
            while aux1 != self.primero and aux1 != self.ultimo:
                if aux1.dato == dato_buscar:
                    return aux1.dato
                aux1 = aux1.sig
            return None


    def encontrar_cuantos(self, dato_buscar):
        """Método que permite encontrar cuántas veces está un dato
        dentro de la lista.

        Parameters
        ----------
        dato_buscar : object
            Corresponde al valor del dato a buscar en la lista.

        Returns
        -------
        int
            Retornará el número de veces que se encuentra el dato en la
            lista.
        """
        if self.es_vacia():
            return 0
        
        aux = self.primero
        counter = 0

        while True:
            if aux.dato == dato_buscar:
                counter += 1
            aux = aux.sig
            if aux == self.primero:
                break
        return counter
    

    def ruleta(self, pos_rel):
        """Método que permite por medio de una posición el dato que
        contiene al nodo correspondiente.

        Parameters
        ----------
        pos_rel : int
            Hace referencia al valor con el que se recorrerá la lista.

        Returns
        -------
        object
            Retornará el dato correspondiente al nodo por posición.
        """
        if self.es_vacia():
            return False
        
        aux = self.primero
        counter = 0
        while counter < pos_rel:
            aux = aux.sig    
            counter += 1
        return aux.dato
    
    def __str__(self):
        """Método que devuelve una cadena con los datos de la lista, 
        o una cadena vacía en el caso de que la lista esté vacía.

        Returns
        -------
        str
            Se retornará una cadena en el formato:
            "> |dato_0| > |dato_1| > ... > |dato_n| > "
            caso contrario si se encuentra vacía retornara: "" .
        """
        if self.es_vacia():
            return ""
        actual = self.primero
        resultado = []
        
        while True:
            resultado.append(f"|{actual.dato}|")
            actual = actual.sig
            if actual == self.primero:
                break
        
        return "> "+" > ".join(resultado) + " > "
    
    def __len__ (self):
        """Método que calcula el tamaño de la lista.

        Returns
        -------
        int
            El número de nodos que contiene la lista.
        """
        actual = self.primero
        counter = 0

        while actual:
            counter +=1
            actual = actual.sig 
            if actual == self.primero:
                break
        
        return counter
    
    def __iter__(self):
        """Método que permite iterar sobre la lista circular 
        simplemente enlazada.

        Returns
        -------
        None
            Si el actual no existe, osea, la lista está vacía.

        Yields
        ------
        int
            Corresponde a cada uno de los nodos de la lista en orden.
        """
        actual = self.primero
        if actual is None:
            return None
        while True:
            yield actual.dato 
            actual = actual.sig

            if actual == self.primero:
                break
    
