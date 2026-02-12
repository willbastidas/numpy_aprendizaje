#martices en 2d
import numpy as np

m2d = np.array([[1,2,3],[4,5,6]]) # matriz en 2d

print(m2d)

print(" ")

# convertir lista en matriz
list = [1,2,3,5,6] #crear lista
m1d = np.array(list) #covertir lista a array
print(m1d)

print(" ")

list2d = [[1,2,3],[4,5,6],[7,8,9]]
m2d = np.array(list2d)
print(m2d)

print(" ")


#matrices mas rapido en 2d
m = np.arange(15).reshape(3,5)
print(m)

# m2 = np.arange(20).reshape(3,5) #esto dara error porque la cantidad de numeros sobre pasa a las filas y las columnas
#en caso de querer que funcione busca dos numeros que multiplicados den 20


m2 = np.arange(20).reshape(4,5)
print(m2)
