# Creacion de un conjunto por asignacion ----------------------------------------------------
# Creación de un conjunto vacío -------------------------------------------------------------
# conjunto_vacio = set()
# print(conjunto_vacio)  # output: set()

# Creación de un conjunto con elementos
# conjunto = {1, 2, 3, 4, 5}
# print(conjunto)  # output: {1, 2, 3, 4, 5}

# Añadir y eliminar elementos de un conjunto -------------------------------------------------
# conjunto = {1, 2, 3, 12}

# conjunto.add(4) # Agregar
# print(f'Agregamos el numero 4: {conjunto}')  # output: {1, 2, 3, 4}

# conjunto.remove(2) # Remover (Genera error)
# print(f'Removemos el numero 2: {conjunto}')  # output: {1, 3, 4}

# conjunto.discard(5)  # No genera ningún error
# print(f'Removemos el numero 5, sin errores: {conjunto}')  # output: {1, 3, 4}

# Operaciones con conjuntos ------------------------------------------------------------------

# conjunto1 = {1, 2, 3}
# conjunto2 = {3, 4, 5}
# print(f'''
# OPERACIONES CON CONJUNTOS
# Conjunto 1: {conjunto1}
# Conjunto 2: {conjunto2}
# -----------------------------------------
# ''')

# # Unión de conjuntos
# union = conjunto1.union(conjunto2)
# print(f'Union: {union}')  # output: {1, 2, 3, 4, 5}

# # Intersección de conjuntos
# interseccion = conjunto1.intersection(conjunto2)
# print(f'Interseccion: {interseccion}')  # output: {3}

# # Diferencia de conjuntos
# diferencia = conjunto1.difference(conjunto2)
# print(f'Diferencia: {diferencia}')  # output: {1, 2}

# # Comprobación de subconjunto
# es_subconjunto = conjunto1.issubset(conjunto2)
# print(es_subconjunto)  # output: False

# Convertir otro tipo de dato a un conjunto --------------------------------------------------
# Convertir una lista a conjunto
lista = [1, 2, 3, 3, 4, 5, 5]
conjunto = set(lista)
print(conjunto)  # output: {1, 2, 3, 4, 5}

# Convertir una cadena de caracteres a conjunto
cadena = "Hola mundo"
conjunto = set(cadena)
print(conjunto)  # output: {'o', 'H', ' ', 'l', 'm', 'n', 'a', 'u', 'd'}
