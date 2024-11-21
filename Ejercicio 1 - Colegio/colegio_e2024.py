from bed.lineales.lse import Lista_SE

class Estudiante:
    """La clase Estudiante implementa un estudiante que posee código, nombre
    y una nota global
    """
    def __init__(self, codigo, nombre="", nota=0.0):
        """Constructor del Estudiante. El código del estudiante deben ser
        todos números y con un tamaño de 4 dígitos. La nota debe estar
        entre 0.0 y 5.0.

        Parameters
        ----------
        codigo : str
            código del estudiante
        nombre : str, optional
            nombre del estudiante, por defecto ""
        nota : int, optional
            nota del estudiante, por defecto 0.0
        """
        self.codigo = codigo
        self.nombre = nombre
        self.nota = nota

    @property
    def codigo(self):# Tiene que ser el mismo nombre del atributo
        return self.__codigo
    @codigo.setter
    def codigo(self,codigo_estu):
        if codigo_estu.isdigit() and len(codigo_estu)==4:
            self.__codigo = codigo_estu
        else:
            raise ValueError('El codigo debe contener 4 caracteres y debe ser numeros')
    
    @property
    def nota(self):# Tiene que ser el mismo nombre del atributo
        return self.__nota
    @nota.setter
    def nota(self,nota_estu):
            if 0<=nota_estu<=5:
                self.__nota = nota_estu
            else:
                raise ValueError('La nota debe estar entre 0 y 5')

    def __str__(self):
        """Método de presentación del Estudiante.

        Returns
        -------
        str
            cadena que representa al estudiante con el formato:
                        "código|nombre|nota"
        """
        return f'{self.codigo}|{self.nombre}|{self.nota}'

    def __eq__(self, otro_estudiante):
        """Método que compara si dos Estudiantes son iguales, teniendo en
        cuenta únicamente el código del estudiante.
        ------------------------------ TAREA ----------------------------
        Validar que el tipo de dato de otro_estudiante corresponda a
        Estudiante. Si no es un Estudiante, devolver False
        -----------------------------------------------------------------

        Parameters
        ----------
        otro_estudiante : Estudiante
            el otro estudiante con el cual se van ha realizar las
            comparaciones de igualdad

        Returns
        -------
        bool
            True si los dos estudiantes son el mismo. False en caso
            contrario
        """
        if isinstance(otro_estudiante,Estudiante):
            if self.codigo == otro_estudiante.codigo:
                return True
            return False
        else:
            return False


class Colegio:
    """La clase Colegio implementa el funcionamiento de un establecimiento
    educativo, el cual tiene un nombre y una lista de estudiantes matriculados
    """
    def __init__(self, nombre):
        """Constructor del Colegio. Aún no se han matriculado ningún
        estudiante al colegio

        Parameters
        ----------
        nombre : str
            nombre del colegio
        """
        self.nombre = nombre
        self.matriculados = Lista_SE()

    def matricular(self, nuevo_est, becado=False, pos_beca=0):
        """Método que realiza la matrícula de nuevos estudiantes al colegio.
        Validar que el estudiante no se encuentre ya matriculado en el colegio.
        En caso afirmativo, el nuevo estudiante no será matriculado

        Parameters
        ----------
        nuevo_est : Estudiante
            el nuevo estudiante a ser matriculado
        becado : bool, optional
            indica si un estudiante va a ser becado o no. En caso de ser
            becado, ubicarlo en una determinada posición de la lista., por
            defecto False
        pos_beca : int, optional
            posición a ocupar en la lista de estudiante, en el caso de que el
            estudiante fuese becado, por defecto 0

        Returns
        -------
        bool
            True si el estudiante es matriculado. False en caso contrario
        """
        b = False
        for estu in self.matriculados:
            if estu==nuevo_est:
                b = True
                break
        if b==False:
            if becado==True:
                self.matriculados.posicionar(nuevo_est,pos_beca)
            else:
                self.matriculados.adicionar(nuevo_est)
            return True

    @property
    def nuevo_est(self):# Tiene que ser el mismo nombre del atributo
        return self.__nuevo_est
    @nuevo_est.setter
    def nuevo_est(self,nuevo_estudiante):
        if isinstance(nuevo_estudiante,Estudiante):
            self.__nuevo_est = nuevo_estudiante
        else:
            raise ValueError('El estudiante tiene que ser una instancia de Estudiante')

    def expulsar(self, pos_est, por_estudiante=False):
        """Método que expulsa a un estudiante ya sea por estudiante o posición
        en la lista de estudiantes matriculados

        Parameters
        ----------
        pos_est : int|Estudiante
            representa la posición o el objeto de tipo estudiante a ser
            expulsado del colegio, siempre y cuando exista
        por_estudiante : bool, optional
            bandera que representa si se expulsa por estudiante (True) o por
            posición (False), por defecto False

        Returns
        -------
        bool
            True si el estudiante pudo ser expulsado. False en caso contrario
        """
        # if (isinstance(pos_est,int)|isinstance(pos_est,Estudiante)) and isinstance(por_estudiante,bool):
        if por_estudiante:
            return True if self.matriculados.remover(pos_est,False) else False
        else:
            pos_est = int(pos_est)
            return True if self.matriculados.remover(pos_est) else False

        # else:
            # raise ValueError('Error en los parametros dados')

    def ver_estudiantes(self):
        """Método que permite visualizar los estudiante matriculados en el
        colegio
        """
        self.matriculados.recorrer()

    def computar_nueva_nota(self, estud, nueva_nota):
        """Método que computa una nueva nota para un estudiante matriculado.
        Actualizar la nota, recalculando la nota del estudiante, promediando
        la nota que ya tiene con la nueva nota

        Parameters
        ----------
        estud : Estudiante
            el estudiante al cual se le va a calcular la nota
        nueva_nota : float
            nueva nota a ser registrada a un estudiante matriculado

        Returns
        -------
        bool
            True si se pudo asignar la nueva nota. False en caso contrario
        """
        estudiante = self.matriculados.encontrar(estud)
        if estudiante:
            new = (nueva_nota+estudiante.dato.nota)/2
            estudiante.dato.nota = new
            i = 0
            for estu in self.matriculados:
                if estu==estudiante.dato:
                    self.expulsar(estudiante,True)
                    self.matriculados.posicionar(estudiante,i)
                    break
                i+=1
            return True if estudiante.dato else False

    def ubicar_estudiante(self, pos_loc):
        """Método que permite ubicar un estudiante matriculado dada una
        posición.

        Parameters
        ----------
        pos_loc : int
            valor de la posición en la lista de estudiantes matriculados

        Returns
        -------
        Estudiante|None
            el estudiante si está matriculado. None en caso contrario
        """
        estudiante = self.matriculados.ubicar(pos_loc) 
        return estudiante.dato if estudiante else None
        

    def informe(self):
        """Método que genera una cadena a modo de Informe de todos los estudiantes
        matriculados en el colegio.

        Returns
        -------
        str
            cadena con el formato:
                "Informe del Colegio ABC / (estudiante_0) :>: (estudiante_1) :>: (estudiante_2) :>: (estudiante_n)"
        """
        estudiantes = self.matriculados.__str__()
        cadena = f'Informe del Colegio {self.nombre} / {estudiantes}'
        return cadena
        


    def promedio(self):
        """Método que calcula y retorna el promedio de todas las notas de los estudiantes
        actualmente matriculados

        Returns
        -------
        float
            promedio de todas las notas de los estudiantes matriculados en el colegio
        """
        i,s = 0,0
        for estu in self.matriculados:
            i+=1
            s+= float(estu.dato.nota)
        if i!=0:
            prom = s/i
            return prom
        return False


if __name__ == "__main__":
    school = Colegio("ABC")
    if school.matricular(Estudiante(codigo="1001", nombre="Pepito", nota=3.0)):
        print("Pepito fue matriculado!")

    cod = "1002"
    nomb = "María"
    if school.matricular(Estudiante(cod, nomb, 4.5)):
        print(f"{nomb} fue matriculad@!")

    cod = "1003"
    nomb = "Juanito Alimaña"
    try:
        school.matricular(Estudiante(cod, nomb, -1.0))
    except ValueError as e:
        print(f"Para el estudiante de código {cod} y nombre {nomb}: {e}")

    cod = "1004"
    nomb = "Pedro"
    if school.matricular(Estudiante(cod, nomb)):
        print(f"{nomb} fue matriculad@!")

    cod = "105"
    nomb = "Vanesa"
    try:
        school.matricular(Estudiante(cod, nomb))
    except ValueError as e:
        print(f"Para {nomb} con código {cod}: {e}")

    cod = "16X"
    nomb = "Carlos"
    try:
        school.matricular(Estudiante(cod, nomb, 2.5))
    except ValueError as e:
        print(f"Para {nomb} con código {cod}: {e}")

    cod = "1007"
    nomb = "Alejandra"
    if school.matricular(Estudiante(cod, nomb, 4.5)):
        print(f"{nomb} fue matriculad@!")

    print("\nVista de estudiantes matriculados:")
    print("-"*33)
    school.ver_estudiantes()

    info = school.informe()
    print(info)
    assert info == "Informe del Colegio ABC / (1001|Pepito|3.0) :>: "\
        "(1002|María|4.5) :>: (1004|Pedro|0.0) :>: (1007|Alejandra|4.5)",\
        "ERROR: Informe Incorrecto"

    # cod = input("Código del estudiante a expulsar:")
    # if school.expulsar(pos_est=Estudiante(cod), por_estudiante=True):
    #     print(f"El estudiante de código {cod} fue EXPULSADO del colegio")
    # else:
    #     print(f"El estudiante de código {cod} no pudo ser EXPULSADO del colegio")

    # print("\nVista de estudiantes matriculados:")
    # print("-"*33)
    # school.ver_estudiantes()

    # pos = int(input("Posición del estudiante a expulsar:"))
    # if school.expulsar(pos_est=pos):
    #     print(f"El estudiante de posición {pos} fue EXPULSADO del colegio")
    # else:
    #     print(f"El estudiante de posición {pos} no pudo ser EXPULSADO del colegio")

    # print("\nVista de estudiantes matriculados:")
    # print("-"*33)
    # school.ver_estudiantes()

    if school.computar_nueva_nota(Estudiante("1001"), nueva_nota=5.0):
        print("Actualización de notas EXITOSA!")
    else:
        print("NO pudo asignarse la nota!")
    print("\nVista de estudiantes matriculados:")
    print("-"*33)
    school.ver_estudiantes()

    if school.computar_nueva_nota(Estudiante("1007"), nueva_nota=1.5):
        print("Actualización de notas EXITOSA!")
    else:
        print("NO pudo asignarse la nota!")
    print("\nVista de estudiantes matriculados:")
    print("-"*33)
    school.ver_estudiantes()

    # pos = int(input("Posición del estudiante a ubicar:"))
    # estud = school.ubicar_estudiante(pos)
    # if estud:
    #     print("Estudiante localizado:")
    #     print(estud)
    # else:
    #     print(f"El estudiante en la posición {pos} no fue econtrado!")

    # for i in range(4):
    #     cod = input("Código del estudiante a calificar:")
    #     nota = float(input("Nueva nota:"))
    #     if school.computar_nueva_nota(Estudiante(cod), nueva_nota=nota):
    #         print("Actualización de notas EXITOSA!")
    #     else:
    #         print(f"El estudiante de código {cod} no pudo ser calificado!")

    # print("\nVista de estudiantes matriculados:")
    # print("-"*33)
    # school.ver_estudiantes()

    # print(school.informe())

    print(f"El promedio del Colegio es {school.promedio()}")

# -----------------------------------------------------------------------------------------------------
# estu1 = Estudiante('1241','Deiby Alejandro',3)
# # print(estu1)
# estu2 = Estudiante('1242','David Felipe',2.1)
# print(estu1==estu2)
# estu3 = Estudiante('1243','Juan Riascos',4.5)
# estu4 = Estudiante('1244','AndHack',4.5)
# estu5 = Estudiante('1245','Sara Estupinan',4.5)

# col = Colegio('IEM Colegio')
# col.matricular(estu1)
# col.matricular(estu2)
# col.matricular(estu3)
# col.matricular(estu4)
# col.matricular(estu5)

# col.ver_estudiantes()