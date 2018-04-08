import random


def criar(lista, nivel=0):
    lista_ordem = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8], 
    [3, 4, 5, 6, 7, 8, 0, 1, 2],
    [6, 7, 8, 0, 1, 2, 3, 4, 5],
    [5, 6, 7, 8, 0, 1, 2, 3, 4],
    [2, 3, 4, 5, 6, 7, 8, 0, 1],
    [8, 0, 1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7, 8, 0],
    [4, 5, 6, 7, 8, 0, 1, 2, 3],
    [7, 8, 0, 1, 2, 3, 4, 5, 6]
]
    print("+-----------------------+")
    contador = 0
    for l in lista_ordem:
        l_escodido = [lista[i] for i in l]
        escode(l_escodido, nivel)        
        a, b, c, d, e, f, g, h, i = l_escodido 
        print(f"| {a} {b} {c} | {d} {e} {f} | {g} {h} {i} |")
        if contador == 2 or contador == 5:
            print("+-------+-------+-------+")
        contador += 1
    print("+-----------------------+")

def escode(lista, nivel):
    if nivel == 0:
        nivel = 3
    elif nivel == 1:
        nivel = 4
    elif nivel == 3:
        nivel = 5
    elif nivel == 4:
        nivel = 6
    
    
    lista_escode_numero = random.sample(lista, nivel)
    for intem in lista_escode_numero:
        lista[intem - 1] = " "


a = [1,2,3,4,5,6,7,8,9]
criar(a)

"""
  | A B C | D E F | G H I |
--+-----------------------+
A | 1 2 3 | 4 5   | 7     |
B |   5 6 | 7 8   | 1   3 |
C |   8   | 1 2 3 | 4 5   |
--+-------+-------+-------+
D | 6 7 8 | 9 1   |   4   |
E | 3 4 5 | 6     | 9 1   |
F |   1 2 | 3   5 | 6   8 |
--+-------+-------+-------+
G |   3   | 5 6 7 | 8 9   |
H | 5 6   |   9 1 | 2 3   |
I | 8   1 | 2   4 |   6 7 |
--+-----------------------+
"""
