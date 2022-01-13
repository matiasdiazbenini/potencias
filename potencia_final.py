# CODIGO CON LIMITE DE POTENCIA

# X = NUMERO A ELEVAR
# LIMITE = LIMITE DE POTENCIADOR
# POTENCIADOR = NUMERO INICIAL

# def run():
#     LIMITE = 11
#     x = 6

#     potenciador = 0
#     potencia_x = x**potenciador
#     while potenciador < LIMITE:
#         print(str(x) + " elevado a  " + str(potenciador) + " es igual a: " + str(potencia_x))
#         potenciador = potenciador + 1
#         potencia_x = x**potenciador

# _________________________________________________________________

# CODIGO CON LIMITE DE RESULTADO

# X = NUMERO A ELEVAR
# LIMITE = LIMITE DE RESULTADO
# POTENCIADOR =  NUMERO INICIAL

import math

def suma():
    numero1 = """
    Introduzca el numero base
    """
    base = int(input(numero1))

    numero2 = """
    Introduzca el numero a sumar
    """
    sumando = int(input(numero2))

    resultado = base + sumando

    print(resultado)


def resta():
    numero1 = """
    Introduzca el numero base
    """
    base = int(input(numero1))

    numero2 = """
    Introduzca el numero a restar
    """
    sustraendo = int(input(numero2))

    resultado = base - sustraendo

    print(resultado)

def multiplicacion():
    numero1 = """
    Introduzca el numero base
    """
    base = int(input(numero1))

    numero2 = """
    Introduzca el multiplicador
    """
    multiplicador = int(input(numero2))

    resultado = base * multiplicador

    print(resultado)

def division():
    numero1 = """
    Introduzca el numero base
    """
    base = int(input(numero1))

    numero2 = """
    Introduzca el divisor
    """
    multiplicador = int(input(numero2))

    resultado = base / multiplicador

    print(resultado)

def potenciacion():

    def primera():
        numero = "numero a potenciar: "
        x = int(input(numero))
        potencia = "potencia a la cual elevarlo: "
        y = int(input(potencia))

        print(x**y)

    def segunda():
        preguntapot = """
        La serie de potencias de que numero te gustaria calcular? (recomendado entre el 1 y el 10):
        """

        preguntalim = """
        Cual es el tope de resultado que te gustaria obtener? (el tope de carga, se recomienda numero alto):
        """

        preguntacom = """
        Desde que potencia te gustaria arrancar la serie? (se admiten negativos):
        """

        opcionpot = int(input(preguntapot))
        opcionlim = int(input(preguntalim))
        opcioncom = int(input(preguntacom))

        LIMITE = opcionlim
        x = opcionpot

        potenciador = opcioncom
        potencia_x = x**potenciador
        while potencia_x < LIMITE:
            print(str(x) + " elevado a  " + str(potenciador) + " es igual a: " + str(potencia_x))
            potenciador = potenciador + 1
            potencia_x = x**potenciador
    
    decision = """
    Como te gustaria usar el programa de potencias? Inserte solamente un numero como respuesta.

    Opcion 1: - Calcular rapido una potencia tal de un numero dado
    Opcion 2: - Calcular una serie de potencias de un numero especifico dentro de un rango determinado
    """
    eleccion = input(decision)

    if eleccion == "1":
        primera()
    elif eleccion == "2":
        segunda()
    else:
        print("Respuesta erronea, escriba nuevamente")

def racionalizacion():
    raiz = """
    Por cual raiz le gustaria operar?: Insertar el numero
    Raiz de 2: (2)
    Raiz de 3: (3)
    Raiz de 4: (4)
    Raiz de 5: (5)
    Raiz personalizada: (0)
    """
    numero1 = """
    Introduzca el numero base
    """
    base = input(numero1)
    choice = input(raiz)

    def raiz2():
        racionalizador = 0.5
        resultado = int(base) ** racionalizador
        print(resultado)
    
    def raiz3():
        racionalizador = 0.33
        resultado = int(base) ** racionalizador
        print(resultado)

    def raiz4():
        racionalizador = 0.25
        resultado = int(base) ** racionalizador
        print(resultado)
    def raiz5():
        racionalizador = 0.20
        resultado = int(base) ** racionalizador
        print(resultado)
    def raiz0():
        personalizada = """"
        Que raiz quiere usar?:
        """
        eleccion = int(input(personalizada))

        racionalizador = 1 / eleccion
        resultado = int(base) ** racionalizador
        print(resultado)

    if choice == "2":
        raiz2()
    elif choice == "3":    
        raiz3()
    elif choice == "4":
        raiz4()
    elif choice == "5":
        raiz5()
    elif choice == "0":
        raiz0()


def run():
    programa = """
    Que programa le gustaria usar hoy?

    Opcion 1: - Suma
    Opcion 2: - Resta
    Opcion 3: - Multiplicacion
    Opcion 4: - Division
    Opcion 5: - Potenciacion
    Opcion 6: - Racionalizacion
    """
    choose = input(programa)

    if choose == "1":
        suma()
    elif choose == "2":    
        resta()
    elif choose == "3":
        multiplicacion()
    elif choose == "4":
        division()
    elif choose == "5":
        potenciacion()
    elif choose == "6":
        racionalizacion()
    else:
        print("Mal, elige de nuevo")

if __name__ == "__main__":
    run()