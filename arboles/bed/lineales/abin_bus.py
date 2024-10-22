from nodos import nodoArbol_Bin
from abin import ArbolBinario
from excepciones import DuplicatedKeyError
class ArbolBinario_Bus(ArbolBinario):
    def adicionar(self, nueva_clave):
        self.raiz = self.__adicionar(self.raiz, nueva_clave)
    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = nodoArbol_Bin(nueva_clave)
        elif sub_arbol.clave > nueva_clave: # Ubicar el nuevo nodo por izquierda
            sub_arbol.izq = self.__adicionar(sub_arbol.izq,nueva_clave)
        elif sub_arbol.clave < nueva_clave: # ubicar el nuevo nodo por derecha
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)
        else:
            raise DuplicatedKeyError(nueva_clave)
        return sub_arbol
    
    def encontrar(self, clave_encontrar):
        return self.__encontrar(self.raiz,clave_encontrar)
    def __encontrar(self, sub_arbol, clave_encontrar):
        if sub_arbol.clave==clave_encontrar:
            return sub_arbol.clave
        elif sub_arbol.clave > clave_encontrar:
            return self.__encontrar(sub_arbol.izq, clave_encontrar)
        else:
            return self.__encontrar(sub_arbol.der, clave_encontrar)
        return None