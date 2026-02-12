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

#funcion rque permite abarcar un rango para unos numeros en especifico
#solo con np.arange() coloca el rango que quieres pero en una dimension si quieres agregar dimensiones


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

#  valores para el eje y
doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

#Ponemos 11 porque el límite superior de arange es exclusivo.
one_to_ten = np.arange(1, 11)

#Cree un gráfico de dispersión con doubling_array como valores y
# y one_to_ten como valores x.
plt.scatter(one_to_ten, doubling_array)

#Mostrar el gráfico resultante
plt.show()