#EJERCICIO1
'''
Operaciones Matemáticas

Metodos
----------
suma_resta:
    Devuelve la suma y la resta de los operandos valor1 y valor2
multiplicacion:
    Devuelve la multiplicación de los operandos numero1 y numero2

'''

def suma_resta(valor1,valor2):
    """
    Suma y resta de los operandos valor1 y valor2
    """
    try:
        suma = valor1 + valor2
        resta = valor1 - valor2
        if type(valor1) ==  int and type(valor2) == int:
            print("El resultado de la suma es :", suma)
            print("El resultado de la resta es:", resta)
    except TypeError:
            print("Error en el tipo de alguno de los datos")

#EJERCICIO2
def multiplicacion(numero1,numero2):
    """
    Multiplicación de los operandos numero 1 y numero 2
    """
    mult = numero1 * numero2
    print("El resultado de la multiplicación es:",mult)