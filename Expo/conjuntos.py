class Nodo:
    """Nodo para la lista enlazada dentro de cada bucket"""
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class Conjunto:
    def __init__(self, tamanio=10):
        """Inicializa el conjunto con una tabla hash vacía"""
        self.tamanio = tamanio
        self.tabla_hash = [None] * tamanio  # Lista de "buckets", cada uno es una lista enlazada
    
    def _funcion_hash(self, elem):
        """Función hash simple que toma un elemento y devuelve su código hash"""
        return hash(elem) % self.tamanio  # Usamos el módulo para reducir el rango de los valores hash
    
    def agregar(self, elem):
        """Agrega un elemento al conjunto (sin duplicados)"""
        indice = self._funcion_hash(elem)
        # Si el bucket en el índice es vacío, se agrega un nodo con el valor
        if self.tabla_hash[indice] is None:
            self.tabla_hash[indice] = Nodo(elem)
        else:
            # Si no está vacío, buscamos si el elemento ya existe
            actual = self.tabla_hash[indice]
            while actual:
                if actual.dato == elem:
                    return  # El elemento ya está, no lo agregamos
                if actual.sig is None:  # Si llegamos al final de la lista enlazada
                    break
                actual = actual.sig
            # Si el elemento no se encontró, lo agregamos al final de la lista enlazada
            actual.sig = Nodo(elem)

    def eliminar(self, elem):
        """Elimina un elemento del conjunto"""
        indice = self._funcion_hash(elem)
        actual = self.tabla_hash[indice]
        anterior = None
        while actual:
            if actual.dato == elem:
                if anterior:  # Si no es el primer nodo
                    anterior.sig = actual.sig
                else:  # Si es el primer nodo
                    self.tabla_hash[indice] = actual.sig
                return
            anterior = actual
            actual = actual.sig

    def contiene(self, elem):
        """Verifica si el elemento está en el conjunto"""
        indice = self._funcion_hash(elem)
        actual = self.tabla_hash[indice]
        while actual:
            if actual.dato == elem:
                return True
            actual = actual.sig
        return False

    def union(self, otro_conjunto):
        """Realiza la unión de dos conjuntos"""
        conjunto_union = Conjunto(self.tamanio)
        # Agregar todos los elementos del primer conjunto
        for bucket in self.tabla_hash:
            actual = bucket
            while actual:
                conjunto_union.agregar(actual.dato)
                actual = actual.sig
        # Agregar todos los elementos del segundo conjunto
        for bucket in otro_conjunto.tabla_hash:
            actual = bucket
            while actual:
                conjunto_union.agregar(actual.dato)
                actual = actual.sig
        return conjunto_union

    def interseccion(self, otro_conjunto):
        """Realiza la intersección de dos conjuntos"""
        conjunto_interseccion = Conjunto(self.tamanio)
        # Recorremos el primer conjunto y agregamos a la intersección si existe en el segundo conjunto
        for bucket in self.tabla_hash:
            actual = bucket
            while actual:
                if otro_conjunto.contiene(actual.dato):
                    conjunto_interseccion.agregar(actual.dato)
                actual = actual.sig
        return conjunto_interseccion

    def diferencia(self, otro_conjunto):
        """Realiza la diferencia entre dos conjuntos"""
        conjunto_diferencia = Conjunto(self.tamanio)
        for bucket in self.tabla_hash:
            actual = bucket
            while actual:
                if not otro_conjunto.contiene(actual.dato):
                    conjunto_diferencia.agregar(actual.dato)
                actual = actual.sig
        return conjunto_diferencia

    def diferencia_simetrica(self, otro_conjunto):
        """Realiza la diferencia simétrica entre dos conjuntos"""
        conjunto_dif_simetrica = Conjunto(self.tamanio)
        # Elementos en el primer conjunto pero no en el segundo
        for bucket in self.tabla_hash:
            actual = bucket
            while actual:
                if not otro_conjunto.contiene(actual.dato):
                    conjunto_dif_simetrica.agregar(actual.dato)
                actual = actual.sig
        # Elementos en el segundo conjunto pero no en el primero
        for bucket in otro_conjunto.tabla_hash:
            actual = bucket
            while actual:
                if not self.contiene(actual.dato):
                    conjunto_dif_simetrica.agregar(actual.dato)
                actual = actual.sig
        return conjunto_dif_simetrica

    def __str__(self):
        """Retorna una representación del conjunto como una cadena"""
        elementos = []
        for bucket in self.tabla_hash:
            actual = bucket
            while actual:
                elementos.append(str(actual.dato))
                actual = actual.sig
        return "{" + ", ".join(elementos) + "}"

    def __len__(self):
        """Retorna la cantidad de elementos en el conjunto"""
        count = 0
        for bucket in self.tabla_hash:
            actual = bucket
            while actual:
                count += 1
                actual = actual.sig
        return count

    def __iter__(self):
        """Permite iterar sobre los elementos del conjunto"""
        for bucket in self.tabla_hash:
            actual = bucket
            while actual:
                yield actual.dato
                actual = actual.sig

    def __contains__(self, elem):
        """Permite usar el operador 'in' para verificar si un elemento está en el conjunto"""
        return self.contiene(elem)


# Crear conjuntos
conjunto1 = Conjunto()
conjunto2 = Conjunto()

# Agregar elementos
conjunto1.agregar('Hola')
conjunto1.agregar('Como ')
conjunto1.agregar('Estas')

conjunto2.agregar(2)
conjunto2.agregar(3)
conjunto2.agregar(4)

# Mostrar conjuntos
print("Conjunto 1:", conjunto1)  # {1, 2, 3}
print("Conjunto 2:", conjunto2)  # {2, 3, 4}

# Operaciones entre conjuntos
union = conjunto1.union(conjunto2)
print("Unión:", union)  # {1, 2, 3, 4}

interseccion = conjunto1.interseccion(conjunto2)
print("Intersección:", interseccion)  # {2, 3}

diferencia = conjunto1.diferencia(conjunto2)
print("Diferencia:", diferencia)  # {1}

dif_simetrica = conjunto1.diferencia_simetrica(conjunto2)
print("Diferencia simétrica:", dif_simetrica)  # {1, 4}

# Eliminar un elemento
conjunto1.eliminar(2)
print("Conjunto 1 después de eliminar 2:", conjunto1)  # {1, 3}

# Verificar si un elemento está en el conjunto
print(3 in conjunto1)  # True
print(2 in conjunto1)  # False