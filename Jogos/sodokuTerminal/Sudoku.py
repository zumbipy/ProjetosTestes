import random


class Sudoku(object):

    def __init__(self, lista):
        self.lista = self.valida_lista(lista)
        self.algoritmo_sudoku = [
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

    def criar(self, nivel=0):
        self.nivel = self.valida_nivel(nivel)
        self.lista_jogo = []
        for linha in self.algoritmo_sudoku:
            self.lista_jogo.append([self.lista[x] for x in linha])
        return self.lista_jogo

    def valida_lista(self, lista):
        if len(lista) == 9:
            for valor in lista:
                if isinstance(valor, (float, str, list, dict)):
                    print("Lista só pode tem números.")
                    return False
        else:
            print("Lista Pequena.")
            return False
        for numero in lista:
            if numero not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Lista tem numero maior que 9 ou menor que 0.")
                return False
        return lista

    def valida_nivel(self, valor):
        if valor <= 1:
            return 3
        elif valor == 2:
            return 4
        elif valor == 3:
            return 5
        elif valor == 4:
            return 6
        else:
            return 1

    def trocar_lista(self, nova_lista):
        self.lista = nova_lista
        self.criar()

    def escoder(self):
        for valor in self.lista_jogo:
            lista_oculta = random.sample(self.lista, self.nivel)
            for oculta in lista_oculta:
                valor[oculta-1] = " "

    def mistura(self):
        random.shuffle(self.lista)
        self.criar()

    def visualizar(self):
        lista_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        print("+---+-----------------------+")
        print("|   | A B C | D E F | G H I |")
        print("|---+-----------------------+")
        for index, valor in enumerate(self.lista_jogo):
            a, b, c, d, e, f, g, h, i = valor
            print(
                f"| {lista_letras[index]} | {a} {b} {c} | {d} {e} {f} | {g} {h} {i} |")
            if index == 2 or index == 5:
                print("+---+-----------------------+")
        print("+---+-----------------------+")


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogo = Sudoku(lista)
jogo.criar(3)
jogo.escoder()
jogo.visualizar()
