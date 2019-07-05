import random


class Sudoku(object):

    def __init__(self, lista):
        self.lista = self.validar_lista(lista)  # uma lista de 1 ao 0
        # Algoritmo que gera o sodoku
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
        self.nivel = self.validar_nivel(nivel)
        self.lista_jogo = []
        self.lista_vence = []
        # Gera a lista do jogo usando o algoritmo é a lista dado pelo o usuario.
        for linha in self.algoritmo_sudoku:
            self.lista_jogo.append([self.lista[x] for x in linha])
            self.lista_vence.append([self.lista[x] for x in linha])
        return self.lista_jogo

    def validar_lista(self, lista):
        # Verificando tamanho da lista.
        tamanho_lista = len(lista)
        if tamanho_lista < 9:
            print("Lista tem menos que 9 elementos")
            return False
        if tamanho_lista > 9:
            print("Lista tem menos que 9 elementos")
            return False

        # Verificando o Tipos dentro da lista.
        for elemento in lista:
            if not isinstance(elemento, int):
                print("Tipo dentro da lista diferente de int()")
                return False
        
        # Verificando os elemtos da lista
        for numero in lista:
            if numero not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Lista tem numero maior que 9 ou menor que 0.")
                return False
        return lista

    def validar_nivel(self, valor):
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

    def misturar(self):
        random.shuffle(self.lista)
        self.criar()

    def visualizar(self):
        lista_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        print("""
+---+-----------------------+
|   | A B C | D E F | G H I |
|---+-----------------------+""")
        for index, valor in enumerate(self.lista_jogo):
            a, b, c, d, e, f, g, h, i = valor
            print(f"| {lista_letras[index]} | {a} {b} {c} | {d} {e} {f} | {g} {h} {i} |")
            if index == 2 or index == 5:
                print("+---+-----------------------+")
        print("+---+-----------------------+")

    def validar_jogo(self):
        for linha in self.lista_jogo:
            for numero in range(1, 10):
                if linha.count(numero) > 1:
                    print("Jogo Invalido numero repetido.")
                    return False

        for coluna in range(9):
            lista = [self.lista_jogo[0][coluna], self.lista_jogo[1][coluna], self.lista_jogo[2][coluna],
                     self.lista_jogo[3][coluna], self.lista_jogo[4][coluna], self.lista_jogo[5][coluna],
                     self.lista_jogo[6][coluna], self.lista_jogo[7][coluna], self.lista_jogo[8][coluna],
                     ]
            for numero in range(9):
                if lista.count(numero) > 1:
                    print("Jogo Invalido numero repetido.")
                    return False

        linha, coluna = 0, 0
        for matrix in range(9):
            lista = [self.lista_jogo[linha][coluna], self.lista_jogo[linha][coluna+1], self.lista_jogo[linha][coluna+2],
                     self.lista_jogo[linha+1][coluna], self.lista_jogo[linha+1][coluna+1], self.lista_jogo[linha+1][coluna+2],
                     self.lista_jogo[linha+2][coluna], self.lista_jogo[linha+2][coluna+1], self.lista_jogo[linha+2][coluna+2],
                     ]
            for numero in range(9):
                if lista.count(numero) > 1:
                    print("Jogo Invalido numero repetido.")
                    return False
            coluna += 3
            if matrix == 2 or matrix == 5:
                coluna = 0
                linha += 3
        return True
