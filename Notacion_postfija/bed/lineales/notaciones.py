# DEIBY ALEJANDRO DELGADO ESTRADA
# YOEL ALEJANDRO TORRES ARCINIEGAS
from pila import Pila
from lse import Lista_SE

class Postfija:
    def __init__(self, expresion_infija=str):
        """Método que inicializa una la clase Postfija.
        """
        self.expresion_infija = expresion_infija.replace(" ","")
    
    def infija(self) -> str:
        """Método que retorna la expresión Infija original, separando cada
        operando y cada operador, incluyendo los paréntesis, por un espacio
        en blanco.
        Returns
        -------
        str
            retorna la cadena de la expresion infija original
        """
        def recursion(i=0):
            if i == len(self.expresion_infija):
                return ""
            if self.expresion_infija[i].isdigit():
                num = self.expresion_infija[i]
                return num + recursion(i + 1) if i + 1 < len(self.expresion_infija) and self.expresion_infija[i + 1].isdigit() else num + " " + recursion(i + 1)
            return self.expresion_infija[i] + " " + recursion(i + 1)

        return recursion().strip()

    def postfija(self):
        """Método que convierte una expresión Infija a una expresión Postfija

        Returns
        -------
        str
            retorna la expresion postfija
        """
        operadores = {
            "^": (4, 3),  
            "*": (2, 2),  
            "/": (2, 2),
            "+": (1, 1),  
            "-": (1, 1),  
            "(": (5, 0)  
        }
        resultado = Lista_SE()
        pila_operadores = Pila()  
        expresion_lista = self.infija().split(" ")

        for token in expresion_lista:  
            if token == "(":  
                pila_operadores.apilar(token)  
            elif token == ")":  
                while not pila_operadores.es_vacia() and pila_operadores.cima() != "(":
                    resultado.adicionar(pila_operadores.desapilar())  
                pila_operadores.desapilar()
            elif token in operadores:  
                while (not pila_operadores.es_vacia() and  
                       operadores[token][0] <= operadores[pila_operadores.cima()][1]):  
                    resultado.adicionar(pila_operadores.desapilar())  
                pila_operadores.apilar(token)  
            else:  
                resultado.adicionar(token)

        while not pila_operadores.es_vacia():  
            resultado.adicionar(pila_operadores.desapilar())  
        
        a = ''
        for i in resultado:
            a += f'{i} '
        a = a.rstrip()

        return a

    def eval_expr_aritm(self) -> float:
        """Método que calcula el resultado de notacion postfija.

        Returns
        -------
        float
            Retorna el resultado de la operacion postfija
        """
        operadores = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y, '/': lambda x, y: x / y, 
                      '^': lambda x, y: x ** y}
        pila = Pila()

        for i in self.postfija().split():
            if i.isdigit():
                pila.apilar(float(i))
            else:
                operando_2, operando_1 = pila.desapilar(), pila.desapilar()
                pila.apilar(operadores[i](operando_1, operando_2))

        return pila.desapilar()
    