class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaCircularEncadeada:
    def __init__(self, tamanho=0, dado_inicial=None):
        self.tamanho = tamanho
        self.head = None

        if dado_inicial:
            self.criar_de_dado(dado_inicial)

    def comprimento(self):
        return self.tamanho

    def ta_vazia(self):
        return self.tamanho == 0

    def inserir_na_posicao(self, dado, posicao):
        if posicao < 0 or posicao > self.tamanho:
            raise ValueError("Posição Inválida")

        novo_no = No(dado)
        if posicao == 0:
            if not self.head:
                novo_no.proximo = novo_no  
            else:
                novo_no.proximo = self.head.proximo
                self.head.proximo = novo_no
            self.head = novo_no
        else:
            atual = self.head
            for _ in range(posicao - 1):
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

        self.tamanho += 1

    def remover_na_posicao(self, posicao):
        if self.ta_vazia() or posicao < 0 or posicao >= self.tamanho:
            raise ValueError("Posição Inválida")

        if posicao == 0:
            if self.tamanho == 1:
                self.head = None
            else:
                self.head.proximo = self.head.proximo.proximo
        else:
            atual = self.head
            for _ in range(posicao - 1):
                atual = atual.proximo
            atual.proximo = atual.proximo.proximo

        self.tamanho -= 1

    def pegar_na_posicao(self, posicao):
        if self.ta_vazia() or posicao < 0 or posicao >= self.tamanho:
            raise ValueError("Posição Inválida")

        atual = self.head
        for _ in range(posicao):
            atual = atual.proximo

        return atual.dado

    def swap_posicao(self, posicao):
        if self.ta_vazia() or posicao < 0 or posicao >= self.tamanho - 1:
            raise ValueError("Posição Inválida")

        atual = self.head
        for _ in range(posicao - 1):
            atual = atual.proximo

        temp = atual.proximo
        atual.proximo = temp.proximo
        temp.proximo = temp.proximo.proximo
        atual.proximo.proximo = temp

    def bubble_sort(self):
        if self.tamanho <= 1:
            return

        for i in range(self.tamanho):
            atual = self.head
            for j in range(self.tamanho - i - 1):
                if atual.dado > atual.proximo.dado:
                    temp = atual.dado
                    atual.dado = atual.proximo.dado
                    atual.proximo.dado = temp
                atual = atual.proximo

    def criar_de_dado(self, dado):
        for item in dado:
            self.inserir_na_posicao(item, self.tamanho)

#uso para armazenar figuras geométricas
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class FigGeometrica:
    def __init__(self, vertices):
        self.vertices = vertices

    def adicionar_vertice(self, x, y):
        novo_ponto = Ponto(x, y)
        self.vertices.append(novo_ponto)

    def exibir_vertices(self):
        return [(ponto.x, ponto.y) for ponto in self.vertices]

    def percorrer(self):
        return iter(self.vertices)

    def __lt__(self, other):
        return len(self.vertices) < len(other.vertices)

      
# Exemplo de uso
figuras_iniciais = [
    FigGeometrica([Ponto(0, 0), Ponto(1, 0), Ponto(1, 1)]),
    FigGeometrica([Ponto(2, 2), Ponto(3, 2), Ponto(3, 3)])
]

lista_circular = ListaCircularEncadeada(dado_inicial=figuras_iniciais)

# Operações na lista circular
lista_circular.inserir_na_posicao(FigGeometrica([Ponto(4, 4), Ponto(5, 4), Ponto(5, 5)]), 1)
lista_circular.remover_na_posicao(0)

# Operações de ordenação
lista_circular.bubble_sort()

# Exibindo figuras após as operações
for i in range(lista_circular.comprimento()):
    print(f"Figura {i + 1}: {lista_circular.pegar_na_posicao(i).exibir_vertices()}")


