from Sudoku import *

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogo = Sudoku(lista)
jogo.criar(3)
if jogo.valida_jogo():
    jogo.escoder()
    jogo.visualizar()