import numpy as np

# MATRICES EN 3D

#esto seria una matriz en 3d game_and_solution la cual esta computa por dos matrices
# de la misma dimensiones como se aprecia en el ejemplo

sudoku_game = np.arange(1,10).reshape(3,3)
sudoku_solution = np.arange(1,10).reshape(3,3)
game_and_solution = np.array([sudoku_game, sudoku_solution])

print(game_and_solution)
print("")

#MATRICES EN 4D
#funciona de igual manera que las 3d, tiene que estar compuesta por dos matrices 3d


new_sudoku_game = np.arange(1,10).reshape(3,3)
new_sudoku_solution = np.arange(1,10).reshape(3,3)
new_game_and_solution = np.array([sudoku_game, sudoku_solution])

game_4d = np.array([new_sudoku_game, new_sudoku_solution])

plana= np.array(new_game_and_solution).flatten()
print(plana)

print(game_4d.shape)