'''
Name: Ronald Alberto Carrillo Garvin
Date: 09-07-2022
Description: Program that calculates the means and standard deviation of a series of data stored in a flat file.
'''

import math
datos1 = list()
datos2 = list()

try:
  archivo = open('datos.txt', mode='r', encoding='utf-8-sig')
  
  sumatoria = 0.0
  sumatoria2 = 0.0
  for linea in archivo:#Recorrido de cada uno de las listas

    fila = linea.split(" ")
    datos1.append(float(fila[0]))
    datos2.append(float(fila[1]))
    
    sumatoria += float(fila[0])
    sumatoria2 += float(fila[1])
    
  archivo.close()
  
  promedio = sumatoria / len(datos1)
  promedio2 = sumatoria2 / len(datos2)
  
  varianza = 0.0
  for i in range(len(datos1)):
    varianza += ((datos1[i]-promedio) * (datos1[i]-promedio))
  
  varianza2 = 0.0
  for i in range(len(datos1)):
    varianza2 += ((datos2[i]-promedio2) * (datos2[i]-promedio2))
  
  desviacion = math.sqrt(varianza/(len(datos1)-1))
  desviacion2 = math.sqrt(varianza2/(len(datos2)-1))
  
  print("--------------")
  print("Mean - Std. Dev")
  print(f"{round(promedio,2)}  {round(desviacion,2)}")
  print(f"{round(promedio2,2)}  {round(desviacion2,2)}")

except ValueError:
  print("Error, ingresó un valor no numérico.")
except FileNotFoundError:
  print("Error, el archivo de datos no está disponible.")
except ZeroDivisionError:
  print("Error, division por cero.")
except TypeError:
  print("Error en el tipo de dato.")
except IndexError:
  print("Falta una columna para realizar los calculos.")
