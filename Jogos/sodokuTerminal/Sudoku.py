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
        if valor in [1, 2, 3, 4]:
            valor += 2
            return valor
        else:
            valor = 2
            return valor

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

    def valida_jogo(self):
        for linha in self.lista_jogo:
            for numero in range(1, 10):
                if linha.count(numero) > 1:
                    print("Jogo Invalido numero repetido.")
                    return False

        
        for coluna in range(9):
            lista = [self.lista_jogo[0][0],self.lista_jogo[1][0],self.lista_jogo[2][0],
                     self.lista_jogo[3][0],self.lista_jogo[4][0],self.lista_jogo[5][0],
                     self.lista_jogo[6][0],self.lista_jogo[7][0],self.lista_jogo[8][0],
            ]
            for numero in range(9):
                if lista.count(numero) > 1:
                    print("Jogo Invalido numero repetido.")
                    return False
            
        for quadrado in range(9):
            lista = [self.lista_jogo[0][0], self.lista_jogo[0][1], self.lista_jogo[0][2],
                     self.lista_jogo[0][3], self.lista_jogo[0][4], self.lista_jogo[0][5],
                     self.lista_jogo[0][6], self.lista_jogo[0][7], self.lista_jogo[0][8],
            ]
            for numero in range(9):
                if lista.count(numero) > 1:
                    print("Jogo Invalido numero repetido.")
                    return False
        return True
