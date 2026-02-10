# import array as arr
#
# matriz = arr.array('i',[1, 2, 3, 4, 5])
# print(matriz)
# for ar in matriz:
#     print(ar)


import numpy as np
matriz= np.array([1,2,3,4,5])
print(matriz)

lista = [1, 3, 5] #coleccion de datos independientes

lista.append(7) #agregar alementos a una coleccion

matriz2 = np.array([2,4,6]) #datos en conjunto

matriz2 = matriz2 + np.array([8]) #aqui en lugar de agregar estaria sumando matrices

print(lista)
print(matriz2)

#operacion aritmetica
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)

#operacion aritmetica con lista
a_list = [1,2,3]
b_list = [4,5,6]
print(a_list+b_list)
