# DEIBY ALEJANDRO DELGADO ESTRADA
# YOEL ALEJANDRO TORRES ARCINIEGAS
from bed.jerarquicas.abin import ArbolBinario
from bed.jerarquicas.nodos import NodoArbol_Bin
from bed.jerarquicas.excepciones import DuplicatedKeyError
from bed.jerarquicas.excepciones import HomogeneityError

class ArbolBinario_Bus(ArbolBinario):
    r"""Es un árbol binario ordenado, donde los nodos de menor valor van siempre
    por la rama izquierda, y los nodos de mayor valor se ubican siempre por la
    rama derecha, respecto a un nodo o sub-arbol.
    ATENCIÓN: Un árbol binario de búsqueda NO acepta valores DUPLICADOS.
             ____50___ <--raiz
            /         \
        ____40        _60______
       /     \      /         \
    _30___   41   55       ____75___
   /     \              /        \
  25    _35            65       _86
       /                   /     \
     32                   68     77
    """
    def adicionar(self, nueva_clave):
        """Método que permite agregar un nuevo nodo al árbol binario de
        búsqueda.

        ATENCIÓN: Validar la HOMOGENEIDAD de las claves. En el caso que
        nueva_clave no sea HOMOGENEA, crear una nueva excepción llamada
        HomogeneityError y lanzarla pasándole como argumento la nueva clave
        (crear un mensaje apropiado para informar al usuario lo que
        está sucediendo):
        HomogeneityError(nueva_clave}

        Parameters
        ----------
        nueva_clave : object
            Es la nueva clave a ser adicionada al árbol binario de búsqueda.
        """
        if self.raiz and not isinstance(nueva_clave,type(self.raiz.clave)):
            raise HomogeneityError(nueva_clave)
        self.raiz = self.__adicionar(self.raiz, nueva_clave)
    
    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbol_Bin(nueva_clave)
        elif nueva_clave < sub_arbol.clave:
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        elif nueva_clave > sub_arbol.clave:
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
        else:
            raise DuplicatedKeyError(nueva_clave)
        return sub_arbol
    def encontrar(self, clave_buscar):
        """Método que realiza la búsqueda de una clave en el árbol binario de
        búsqueda.

        Parameters
        ----------
        clave_buscar : object
        La clave a ser buscada en el árbol binario de búsqueda.

        Returns
        -------
        object|None
            object si se encuentra la clave en el árbol binario de búsqueda.
            None en caso contrario.
        """
        if not isinstance(clave_buscar,type(self.raiz.clave)):
            raise HomogeneityError(clave_buscar)
        return self.__encontrar(self.raiz, clave_buscar)
    
    def __encontrar(self, sub_arbol, clave_buscar):
        if sub_arbol:
            if sub_arbol.clave == clave_buscar:
                return sub_arbol.clave
            elif clave_buscar < sub_arbol.clave: # 🔎 por izquierda
                return self.__encontrar(sub_arbol.izq, clave_buscar)
            else: # 🔎 por dereecha
                return self.__encontrar(sub_arbol.der, clave_buscar)
        return None
    # CONSULTA #1
    def encontrar_minimo(self):
        """Método que busca y retorna la clave con menor valor del árbol
        binario de búsqueda, o retorna None cuando el árbol binario de
        búsqueda está vacío.

        Returns
        -------
        object|None
            object si se encuentra la clave con el menor valor del árbol
            binario de búsqueda. None en caso contrario.
        """
        if self.raiz is None:
            return None
        return self.__encontrar_minimo(self.raiz)
    
    def __encontrar_minimo(self, sub_arbol):
        if sub_arbol.izq:
            return self.__encontrar_minimo(sub_arbol.izq)
        return sub_arbol.clave
    
    # CONSULTA #2
    def encontrar_maximo(self):
        """Método que busca y retorna la clave con mayor valor del árbol
        binario de búsqueda, o retorna None cuando el árbol binario de
        búsqueda está vacío.

        Returns
        -------
        object|None
            object si se encuentra la clave con el mayor valor del árbol
            binario de búsqueda. None en caso contrario.
        """
        if self.raiz is None:
            return None
        return self.__encontrar_maximo(self.raiz)
    
    def __encontrar_maximo(self, sub_arbol):
        if sub_arbol.der:
            return self.__encontrar_maximo(sub_arbol.der)
        return sub_arbol.clave
    
    # CONSULTA #3
    def remover(self, clave_remover, mayor=True):
        r"""Método que remueve un nodo del árbol binario de búsqueda cuando la
        clave a remover existe.

        Parameters
        ----------
        clave_remover : object
            La clave a remover del árbol binario de búsqueda.
        mayor : bool, optional
            Valor que determina la forma de remover un nodo cuando éste
            contiene la clave a buscar y posee dos hijos directos. Por defecto
            True.
            1) si 'mayor' es True: se busca y reemplaza el nodo a remover por el
            MAYOR de sus hijos menores.

            Borrando... 40
                  ____50___<--raiz
                 /         \
            ____35         _60______
           /      \       /       \
          30       41    55    ____75___
         /  \                 /         \
       25   32              65           86
                              \         /
                               68      77
                         
            2) si 'mayor' es False: se busca y reemplaza el nodo a remover por el
            MENOR de sus hijos mayores.

            Borrando... 60
                  ____50___<--raiz
                 /         \
            ____35         _65___
           /      \       /     \
          30       41    55    _75___
         /  \                 /       \
       25   32               68        86
                                      /
                                    77
        """
        self.raiz = self.__remover(self.raiz, clave_remover, mayor)

    def __remover(self, sub_arbol, clave_remover, mayor):
        if sub_arbol is None:
            return sub_arbol
        if clave_remover < sub_arbol.clave:
            sub_arbol.izq = self.__remover(sub_arbol.izq, clave_remover, mayor)
        elif clave_remover > sub_arbol.clave:
            sub_arbol.der = self.__remover(sub_arbol.der, clave_remover, mayor)
        else:
            if not sub_arbol.izq:
                return sub_arbol.der
            elif not sub_arbol.der:
                return sub_arbol.izq
            
            if mayor:
                nuevo_nodo = self.__encontrar_maximo(sub_arbol.izq)
                sub_arbol.clave = nuevo_nodo
                sub_arbol.izq = self.__remover(sub_arbol.izq, nuevo_nodo, mayor)
            else:
                nuevo_nodo = self.__encontrar_minimo(sub_arbol.der)
                sub_arbol.clave = nuevo_nodo
                sub_arbol.der = self.__remover(sub_arbol.der, nuevo_nodo, mayor)
        return sub_arbol