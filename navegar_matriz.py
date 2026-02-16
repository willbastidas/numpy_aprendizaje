import numpy as np

tree_census = np.random.randint(0, 101, size=(105, 105))
print(tree_census)
print("")


# 1. NAVEGACIÓN BÁSICA: Selección de una columna completa
# Seleccionamos todas las filas (:) de la segunda columna (índice 1)
block_ids = tree_census[:, 1]
print(block_ids)
print("")



# 2. SLICING EN 1D: Primeros elementos y rangos específicos
# Primeros cinco block_ids
first_five = block_ids[:5]

print(first_five)
print("")

# El décimo elemento (índice 9)
tenth_block_id = block_ids[9]
print(tenth_block_id)
print("")

# Cinco bloques consecutivos empezando por el décimo
block_id_slice = block_ids[9:14]
print(block_id_slice)
print("")

# 3. NAVEGACIÓN EN 2D: Selección con rangos y saltos (Steps)
# Los primeros 100 diámetros de la tercera columna (índice 2)
hundred_diameters = tree_census[:100, 2]
print(hundred_diameters)
print("")

# Diámetros de filas pares del 50 al 100 inclusive
# [inicio:fin:paso , columna]
every_other_diameter = tree_census[50:101:2, 2]
print(every_other_diameter)
print("")

# 4. PROCESAMIENTO: Ordenar los datos
# Extraer la columna de diámetros y ordenarla de menor a mayor
sorted_trunk_diameters = np.sort(tree_census[:, 2])

# Imprimimos resultados para verificar
print(f"Décimo ID: {tenth_block_id}")

print(f"Diámetros ordenados: {sorted_trunk_diameters}")