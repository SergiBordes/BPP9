# ================================================
#  Sergi Bordes Lloria 
#  Actividad 01 - Control de errores, pruebas y validación de datos 
# ================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def is_numeric(val): #Creamos una funcion para comprobar que el dato pasado es numerico
    try:
        float(val)
        return True
    except ValueError:
        return False

try:
    # lee el archivo CSV
    df = pd.read_csv('finanzas2020[1].csv', sep='\t', header=0)
    
    
    
    # Comprobar si todas las columnas tienen contenido
    if df.isnull().any().any():
        raise Exception('Hay columnas vacías en el archivo.')
    
    # Itera sobre todas las columnas del dataframe y convierte los valores no numéricos a NaN
    for col in df.columns:
        df[col] = df[col].apply(lambda x: pd.to_numeric(x, errors='coerce') if is_numeric(x) else np.nan)
        
    # verifica si el número de columnas es igual a 12
    # cuenta el número de columnas
    num_cols = len(df.columns)
    if num_cols != 12:
        raise Exception("El archivo CSV debe tener exactamente 12 columnas")
    
    print("Todos los datos son correctos") #Si todo está bien, continúa con el código

    
except Exception as e:
    print("Error:", e)
    
    
try: #Creamos un csv nuevo con todo arreglado
    df.to_csv('finanzas.csv', sep=';', decimal='.', index=False, encoding='utf-8')
except Exception as e:
    print(f'Error: {e}')
        
df_corregido = pd.read_csv('finanzas.csv', sep=';') #Leemos el nuevo df
print(df_corregido)

# ============
# A partir de aqui ya podemos operar con los valores y hacer el primer apartado
# ============

#Sumamos lo de cada mes para saber ganancias/pérdidas mensuales
print(df_corregido.sum(numeric_only=True))

#Hacemos la media mensual
print(df_corregido.mean(numeric_only=True))

#Para saber el gasto total en el año, vamos a sumar el total de cada columna
df_suma = df_corregido.sum(numeric_only=True)
# Recorremos los valores de la Serie y sumamos solo los negativos
gasto = 0
for index, value in df_suma.items():
    if value < 0:
        gasto = gasto + value
        
print("El total de gasto ha sido de --> " + str(gasto))


#Para saber el benificio total en el año, hacemos lo mismo pero para > 0
# Recorremos los valores de la Serie y sumamos solo los positivos
beneficios = 0
for index, value in df_suma.items():
    if value > 0:
        beneficios = beneficios + value
        
print("El total de beneficio ha sido de --> " + str(beneficios))


#Graficamos el resultado (Esto lo he podido ver desde el Jupyter Notebook)
plt.plot(df_suma)