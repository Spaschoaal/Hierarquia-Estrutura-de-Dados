class Array:
    def __init__(self, elements):
        self.elements = elements

    def __getter__(self, index):
        return self.elements[index]

    def __setter__(self, index, value):
        self.elements[index] = value

class Matriz:
    def __init__(self, nome, matriz):
        self.nome = nome
        self.matriz = matriz
        self.linhas = len(matriz)
        self.colunas = len(matriz[0])

    def __str__(self):
        return f"{self.nome} ({self.linhas}x{self.colunas})"

    def imprimir(self):
        print(f"Matriz {self.nome}:")
        for linha in self.matriz:
            print(" ".join(map(str, linha)))

    def transposta(self):
        transposta = [[self.matriz[j][i] for j in range(self.linhas)] for i in range(self.colunas)]
        return Matriz(f"{self.nome}^T", transposta)

class MatrizQuadrada(Matriz):
    def traco(self):
        if self.linhas != self.colunas:
            raise ValueError("A matriz não é quadrada.")
        traco = sum(self.matriz[i][i] for i in range(self.linhas))
        return traco

class MatrizTriangular(Matriz):
    def determinante(self):
        if self.linhas != self.colunas:
            raise ValueError("A matriz não é quadrada.")
        determinante = 1
        for i in range(self.linhas):
            determinante *= self.matriz[i][i]
        return determinante

class MatrizDiagonal(MatrizTriangular):
    def __init__(self, nome, matriz):
        super().__init__(nome, matriz)

class CalculadoraMatricial:
    def __init__(self):
        self.matrizes = []

    def tipo_das_matrizes(self):
        for matriz in self.matrizes:
            if isinstance(matriz, MatrizQuadrada):
                print(f"{matriz.nome} é uma matriz quadrada.")
            elif isinstance(matriz, MatrizTriangular):
                print(f"{matriz.nome} é uma matriz triangular.")
            elif isinstance(matriz, MatrizDiagonal):
                print(f"{matriz.nome} é uma matriz diagonal.")
            else:
                print(f"{matriz.nome} é uma matriz genérica.")

    def adicionar_matriz(self, nome, matriz):
        self.matrizes.append(Matriz(nome, matriz))

    def adicionar_matriz_identidade(self, n):
        identidade = [[0] * n for _ in range(n)]
        for i in range(n):
            identidade[i][i] = 1
        self.adicionar_matriz(f"Identidade{n}", identidade)

    def remover_matriz(self, nome):
        self.matrizes = [matriz for matriz in self.matrizes if matriz.nome != nome]

    def imprimir_matrizes(self):
        for matriz in self.matrizes:
            matriz.imprimir()

    def somar_matrizes(self, nome_a, nome_b):
        matriz_a = next(matriz for matriz in self.matrizes if matriz.nome == nome_a)
        matriz_b = next(matriz for matriz in self.matrizes if matriz.nome == nome_b)
        if matriz_a.linhas != matriz_b.linhas or matriz_a.colunas != matriz_b.colunas:
            raise ValueError("As matrizes devem ter a mesma forma para soma.")
        resultado = [[matriz_a.matriz[i][j] + matriz_b.matriz[i][j] for j in range(matriz_a.colunas)] for i in range(matriz_a.linhas)]
        self.adicionar_matriz(f"{nome_a} + {nome_b}", resultado)

    def subtrair_matrizes(self, nome_a, nome_b):
        matriz_a = next(matriz for matriz in self.matrizes if matriz.nome == nome_a)
        matriz_b = next(matriz for matriz in self.matrizes if matriz.nome == nome_b)
        if matriz_a.linhas != matriz_b.linhas or matriz_a.colunas != matriz_b.colunas:
            raise ValueError("As matrizes devem ter a mesma forma para subtração.")
        resultado = [[matriz_a.matriz[i][j] - matriz_b.matriz[i][j] for j in range(matriz_a.colunas)] for i in range(matriz_a.linhas)]
        self.adicionar_matriz(f"{nome_a} - {nome_b}", resultado)

    def multiplicar_por_escalar(self, nome, escalar):
        matriz = next(matriz for matriz in self.matrizes if matriz.nome == nome)
        resultado = [[escalar * matriz.matriz[i][j] for j in range(matriz.colunas)] for i in range(matriz.linhas)]
        self.adicionar_matriz(f"{escalar} * {nome}", resultado)

    def multiplicar_matrizes(self, nome_a, nome_b):
        matriz_a = next(matriz for matriz in self.matrizes if matriz.nome == nome_a)
        matriz_b = next(matriz for matriz in self.matrizes if matriz.nome == nome_b)
        if matriz_a.colunas != matriz_b.linhas:
            raise ValueError("O número de colunas da matriz A deve ser igual ao número de linhas da matriz B para multiplicação.")
        resultado = [[sum(matriz_a.matriz[i][k] * matriz_b.matriz[k][j] for k in range(matriz_a.colunas)) for j in range(matriz_b.colunas)] for i in range(matriz_a.linhas)]
        self.adicionar_matriz(f"{nome_a} x {nome_b}", resultado)

if __name__ == "__main__":
    calculadora = CalculadoraMatricial()

    while True:
        print("\nMenu:")
        print("1. Adicionar matriz")
        print("2. Adicionar matriz identidade")
        print("3. Remover matriz")
        print("4. Imprimir matrizes")
        print("5. Somar matrizes")
        print("6. Subtrair matrizes")
        print("7. Multiplicar matriz por escalar")
        print("8. Multiplicar matrizes")
        print("9. Tipo da Matriz")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            break
        elif escolha == "1":
            nome = input("Nome da matriz: ")
            linhas, colunas = map(int, input("Digite as dimensões da matriz (linhas colunas): ").split())
            elementos = []
            for i in range(linhas):
                linha = list(map(float, input(f"Digite os elementos da linha {i + 1}: ").split()))
                elementos.append(linha)
            matriz = elementos
            calculadora.adicionar_matriz(nome, matriz)
        elif escolha == "2":
            n = int(input("Digite a ordem da matriz identidade: "))
            calculadora.adicionar_matriz_identidade(n)
        elif escolha == "3":
            nome = input("Nome da matriz a ser removida: ")
            calculadora.remover_matriz(nome)
        elif escolha == "4":
            calculadora.imprimir_matrizes()
        elif escolha == "5":
            nome_a = input("Nome da primeira matriz: ")
            nome_b = input("Nome da segunda matriz: ")
            calculadora.somar_matrizes(nome_a, nome_b)
        elif escolha == "6":
            nome_a = input("Nome da primeira matriz: ")
            nome_b = input("Nome da segunda matriz: ")
            calculadora.subtrair_matrizes(nome_a, nome_b)
        elif escolha == "7":
            nome = input("Nome da matriz: ")
            escalar = float(input("Digite o escalar: "))
            calculadora.multiplicar_por_escalar(nome, escalar)
        elif escolha == "8":
            nome_a = input("Nome da primeira matriz: ")
            nome_b = input("Nome da segunda matriz: ")
            calculadora.multiplicar_matrizes(nome_a, nome_b)
        elif escolha == "9":
            calculadora.tipo_das_matrizes()

#TesteFuncionamento:
Menu:
1. Adicionar matriz
2. Adicionar matriz identidade
3. Remover matriz
4. Imprimir matrizes
5. Somar matrizes
6. Subtrair matrizes
7. Multiplicar matriz por escalar
8. Multiplicar matrizes
9. Tipo da Matriz
0. Sair
Escolha uma opção: 1
Nome da matriz: A
Digite as dimensões da matriz (linhas colunas): 3 3
Digite os elementos da linha 1: 35 10 1
Digite os elementos da linha 2: 69 120 5
Digite os elementos da linha 3: 4 69 10

Menu:
1. Adicionar matriz
2. Adicionar matriz identidade
3. Remover matriz
4. Imprimir matrizes
5. Somar matrizes
6. Subtrair matrizes
7. Multiplicar matriz por escalar
8. Multiplicar matrizes
9. Tipo da Matriz
0. Sair
Escolha uma opção: 1
Nome da matriz: B
Digite as dimensões da matriz (linhas colunas): 3 3
Digite os elementos da linha 1: 12 92 3
Digite os elementos da linha 2: 34 10 2
Digite os elementos da linha 3: 123 169 1

Menu:
1. Adicionar matriz
2. Adicionar matriz identidade
3. Remover matriz
4. Imprimir matrizes
5. Somar matrizes
6. Subtrair matrizes
7. Multiplicar matriz por escalar
8. Multiplicar matrizes
9. Tipo da Matriz
0. Sair
Escolha uma opção: 5
Nome da primeira matriz: A
Nome da segunda matriz: B

Menu:
1. Adicionar matriz
2. Adicionar matriz identidade
3. Remover matriz
4. Imprimir matrizes
5. Somar matrizes
6. Subtrair matrizes
7. Multiplicar matriz por escalar
8. Multiplicar matrizes
9. Tipo da Matriz
0. Sair
Escolha uma opção: 4
Matriz A:
35.0 10.0 1.0
69.0 120.0 5.0
4.0 69.0 10.0
Matriz B:
12.0 92.0 3.0
34.0 10.0 2.0
123.0 169.0 1.0
Matriz A + B:
47.0 102.0 4.0
103.0 130.0 7.0
127.0 238.0 11.0

Menu:
1. Adicionar matriz
2. Adicionar matriz identidade
3. Remover matriz
4. Imprimir matrizes
5. Somar matrizes
6. Subtrair matrizes
7. Multiplicar matriz por escalar
8. Multiplicar matrizes
9. Tipo da Matriz
0. Sair

