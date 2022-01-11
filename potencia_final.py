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

preguntapot = """
Qué número querés potenciar?:
"""

preguntalim = """
Cuál es el resultado máximo que te gustaría obtener?:
"""

preguntacom = """
Desde qué potencia te gustaría comenzar? (se admiten negativos):
"""

opcionpot = int(input(preguntapot))
opcionlim = int(input(preguntalim))
opcioncom = int(input(preguntacom))

def run():
    LIMITE = opcionlim
    x = opcionpot

    potenciador = opcioncom
    potencia_x = x**potenciador
    while potencia_x < LIMITE:
        print(str(x) + " elevado a  " + str(potenciador) + " es igual a: " + str(potencia_x))
        potenciador = potenciador + 1
        potencia_x = x**potenciador

if __name__ == "__main__":
    run()


