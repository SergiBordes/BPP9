# =========================
# Sergi Bordes Lloria
# Actividad 04 - DEPURACIÓN Y REGLAS DE OPTIMIZACIÓN DE CÓDIGO
# =========================

import pdb

# 1.- Haciendo uso de comprensión de listas realice un programa que, dado una lista de 
# listas de números enteros, devuelva el máximo de cada lista

lista_de_listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]] #Creamos la lista de listas
#pdb.set_trace()
maximos = [max(lista) for lista in lista_de_listas]
print(maximos)


# 2.- Haga uso de la función filter para construir un programa que, dado una lista de n números 
# devuelva aquellos que son primos. Por ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el 
# programa que implemente debe devolver como resultado [3, 5, 5, 13]

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros = [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(es_primo, numeros))
print(primos)
