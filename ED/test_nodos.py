from bed.lineales.nodos import Nodo_listaSE

if __name__=='__main__':
    nodo1 = Nodo_listaSE(7)
    nodo2 = Nodo_listaSE(10)
    nodo1.sig = nodo2
    print(nodo1.sig.sig)