from bed.lineales.lse import Lista_SE

if __name__ == '__main__':
    # Creamos una lista simplemente enlazada
    lista_num = Lista_SE()
    print('Metodo es vacia:')
    print(f'La lista es vacia? {lista_num.es_vacia()}')
    print(f'Adicionamos elementos:')
    lista_num.adicionar(7)
    lista_num.adicionar(5)
    lista_num.adicionar(9)
    print(f'La lista es vacia? {lista_num.es_vacia()}')
    
    # lista_num.adicionar("UDENAR") # Validar solo se adicionen dadtos homogeneos, cuando no sea del mimo tipo tiene que devolver False y cuando si se adicione imprime un True
    print('Recorremos la lista ----------')
    lista_num.recorrer()
    print('Encontrar dato 5: ')
    lista_num.encontrar(5)
    print('Dato no encontrado 51:')
    lista_num.encontrar(51)
    print('Remover el dato 10:')
    print(lista_num.remover(10))
    print('Remover el dato en pos 1:')
    print(lista_num.remover(1))
    lista_num.recorrer()