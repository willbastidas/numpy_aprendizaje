import numpy as np
# pip install numpy
import matplotlib.pyplot as plt # importancion para graficar
#pip install matplotlib

#funcion np.zeros te permite crear una matriz solo con 0

zeros_array = np.zeros((3,3))
print(zeros_array)
print(zeros_array.shape)

# la funcion .shape se utiliza en el print para saber cuantas filas y columnas tiene
# lo que se esta imprimiendo el array



#funcion random te permite crear una matriz con numeros random
#siempre seran decimales

random_array = np.random.random((3,3))
print(random_array)
print("")

#esta es la manera que se tiene para crear un array random con numeros enteros en este caso
#randint te permite elegir el valor mas bajo y el valor mas alto posible debido a que en este caso se quieren numeros enteros se puso el 0 al 1000
#y lo que esta al lado dentro parentesis ,(4,4) es las dimensiones que se le quiere dar a la matriz
random_array1 = np.random.randint(0,1000,(3,3))
print(random_array1)
print("")

random_array2 = np.random.randint(0,1000,(3,3))
print(random_array2)
print("")


#concatenar . concatenar sirve para juntar dos arrays de la misma dimension ya sea que sean iguales en el eje x o en el eje y
array_concatenate_2_3_axis_1 = np.concatenate((random_array1, random_array2), axis=1)
print(array_concatenate_2_3_axis_1)
print("")

array_concatenate_2_3_axis_0 = np.concatenate((random_array1, random_array2), axis=0)
print(array_concatenate_2_3_axis_0)
print("")

#funcion que permite abarcar un rango para unos numeros en especifico
#solo con np.arange() coloca el rango que quieres pero en una dimension si quieres agregar dimensiones
arange_array1 = np.arange(10)
print(arange_array1)
print("")

#debes colocar .reshape(()) para agregar las dimensiones para que no de error debes colocar que la fila y la columna multiplicados uno por el otro
# den el digito que esta dentro del rango como lo muestra el ejemplo

arange_array = np.arange(10).reshape((2,5))

print(arange_array)
print("")

#en caso de ser como este rango que comienza en 1 (no toma el 0 como valor)
# y termina en 11 no incluye el 11 como valor, se resta el el valor mayor menos el valor menor
#en este caso 11-1=10 el resultado es de donde buscaras dos numeros multiplicados que den ese resultado
arange_array2 = np.arange(1, 11).reshape((2,5))

print(arange_array2)
print("")

#la funcion dtype funciona para poder saber el tipo de valor que es la matriz
#tambien funciona para cambiar el tipo de valor

zeros_array2 = np.zeros((3,3))
print(zeros_array2.dtype)
print("")

zeros_array2_int = np.zeros((3,3), dtype='int64')
print(zeros_array2_int.dtype)
print("")



#  valores para el eje y
doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

#Ponemos 11 porque el límite superior de arange es exclusivo.
one_to_ten = np.arange(1, 11)

#Cree un gráfico de dispersión con doubling_array como valores y
# y one_to_ten como valores x.
plt.scatter(one_to_ten, doubling_array)

#Mostrar el gráfico resultante
plt.show()
