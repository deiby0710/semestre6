class MyHashSet:
    def __init__(self):
        """Inicializa el conjunto como un diccionario vacío."""
        self.data = {}

    def add(self, value):
        """Agrega un elemento al conjunto usando su hash."""
        self.data[hash(value)] = value  # El hash como clave garantiza unicidad

    def remove(self, value):
        """Elimina un elemento del conjunto si está presente."""
        hashed_value = hash(value)
        if hashed_value in self.data:
            del self.data[hashed_value]
        else:
            raise ValueError(f"{value} no está en el conjunto.")

    def contains(self, value):
        """Verifica si un elemento está en el conjunto."""
        return hash(value) in self.data

    def union(self, other_set):
        """Devuelve un nuevo conjunto que es la unión con otro conjunto."""
        result = MyHashSet()
        result.data = {**self.data, **other_set.data}  # Combina los diccionarios
        return result

    def intersection(self, other_set):
        """Devuelve un nuevo conjunto que es la intersección con otro conjunto."""
        result = MyHashSet()
        for key, value in self.data.items():
            if key in other_set.data:
                result.add(value)
        return result

    def difference(self, other_set):
        """Devuelve un nuevo conjunto que es la diferencia con otro conjunto."""
        result = MyHashSet()
        for key, value in self.data.items():
            if key not in other_set.data:
                result.add(value)
        return result

    def __str__(self):
        """Devuelve una representación en cadena del conjunto."""
        return "{" + ", ".join(map(str, self.data.values())) + "}"


# Crear dos conjuntos
set1 = MyHashSet()
set2 = MyHashSet()

# Agregar elementos
set1.add(1)
set1.add(2)
set1.add(3)
set2.add(2)
set2.add(3)
set2.add(4)

print("Set 1:", set1)  # {1, 2, 3}
print("Set 2:", set2)  # {2, 3, 4}

print('Estructura ', set1[0])

# Operaciones
union_set = set1.union(set2)
print("Unión:", union_set)  # {1, 2, 3, 4}

intersection_set = set1.intersection(set2)
print("Intersección:", intersection_set)  # {2, 3}

difference_set = set1.difference(set2)
print("Diferencia (set1 - set2):", difference_set)  # {1}
