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

def suma():
    pass

def resta():
    pass

def multiplicacion():
    pass

def division():
    pass

def potenciacion():

    def primera():
        preguntapot = """
        ¿Qué número querés potenciar? (recomendado entre el 1 y el 10):
        """

        preguntalim = """
        ¿Cuál es el resultado máximo que te gustaría obtener? (el tope de carga, se recomienda número alto):
        """

        preguntacom = """
        ¿Desde qué potencia te gustaría comenzar? (se admiten negativos):
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


    def segunda():
        numero = "numero a potenciar: "
        x = int(input(numero))
        potencia = "potencia a la cual elevarlo: "
        y =int(input(potencia))

        print(str(x**y))
    
    decision = """
    Como te gustaria usar el programa de potencias? Inserte solamente un numero como respuesta.

    Opcion 1: - Calcular una serie de potencias de un numero especifico dentro de un rango determinado
    Opcion 2: - Calcular rapido una potencia tal de un numero dado
    """
    eleccion = input(decision)

    if eleccion == "1":
        primera()
    elif eleccion == "2":
        segunda()
    else:
        print("Respuesta errónea, escriba nuevamente")

def racionalizacion():
    pass

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
    if choose == "2":    
        resta()
    if choose == "3":
        multiplicacion()
    if choose == "4":
        division()
    if choose == "5":
        potenciacion()
    if choose == "6":
        racionalizacion()

if __name__ == "__main__":
    run()



