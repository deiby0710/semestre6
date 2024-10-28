def pre_ordern(arbol_binario):
    __pre_orden(arbol_binario.raiz)

def __pre_orden(sub_arbol):
    if sub_arbol:
        print(sub_arbol)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)


# Para probarlo
abb = ArbolBinario_Bus()
abb.adicionar(15)
abb.adicionar(20)
abb.adicionar(16)
abb.adicionar(10)
pre_ordern(abb)