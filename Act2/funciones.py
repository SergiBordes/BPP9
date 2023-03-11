# ==============================
# Sergi Bordes Lloria
# Actividad 02 - Tests
# Archivo funciones
# ==============================

#Vamos a crear las funciones típicas matemáticas

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multiplicacion(x,y):
    return x*y

def division(x, y):
    if y == 0:
        raise ValueError('No se puede dividir entre cero')
    return x / y

def potencia(x,y):
    return x**y
