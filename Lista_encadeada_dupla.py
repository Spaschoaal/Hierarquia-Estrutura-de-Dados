class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#Implementando uma DoublyLinkedList(Lista duplamente encadeada)
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

#Adicionar elementos ao final da lista. *lista.append(90)*
    def append(self, elemento):
        node = DoublyNode(elemento)
        if self.head:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        else:
            self.head = node
            self.tail = node
        self.size = self.size + 1

#Adicionar elementos ao inicio da lista.
    def prepend(self, elemento):
        node = DoublyNode(elemento)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size = self.size + 1

#Tamanho da lista através do *len(lista)*
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self.size

#Leitura do elemento. *lista[1]*
    def __getitem__(self, item):
        if 0 <= item < self.size:
            ponteiro = self.head
            for i in range(item):
                ponteiro = ponteiro.next
            return ponteiro.data
        else:
            return None

#Buscador de elementos e retornando a posição. *lista.search(56)*
    def search(self, elemento):
        ponteiro = self.head
        i = 0
        while ponteiro:
            if ponteiro.data == elemento:
                return i
            ponteiro = ponteiro.next
            i += 1
        return None

#Removendo elementos do inicio da lista

    def pop(self):
        ponteiro = self.head
        if ponteiro:
            data = ponteiro.data
            if ponteiro.next:
                ponteiro = ponteiro.next
                ponteiro.prev = None
            else:
                ponteiro = None
                self.tail = None
            self.size -= 1
            return data
        else:
            return None

#Removendo elementos do final da lista

    def pop_back(self):
        if self.tail:
            data = self.tail.data
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            self.size -= 1
            return data
        else:
            return None

# Adicionando a troca dr duas posições sucessivas (swap)
def swap(self, pos):
    if pos < 0 or pos >= self.size - 1:
        print("Posição inválida para a operação de swap.")
        return

    ponteiro1 = self.get_node_at(pos)
    ponteiro2 = ponteiro1.next

    #Atualizando os nós adjacentes
    ponteiro1.prev.next = ponteiro2
    ponteiro2.next.prev = ponteiro1

    #Atualizando os ponteiros de ponteiro1
    ponteiro1.next = ponteiro2.next
    ponteiro1.prev = ponteiro2

    #Atualizando os ponteiros de ponteiro2
    ponteiro2.next = ponteiro1
    ponteiro2.prev = ponteiro1.prev

    #Atualizando o ponteiro anterior a ponteiro1
    if ponteiro1.next:
        ponteiro1.next.prev = ponteiro1

    #Atualizando o ponteiro seguinte a ponteiro2
    if ponteiro2.prev:
        ponteiro2.prev.next = ponteiro2

#Algoritmo de ordenação Bubble Sort
def bubble_sort(self):
    for i in range(self.size):
        for j in range(0, self.size - i - 1):
            node1 = self.get_node_at(j)
            node2 = node1.next

            # Comparando os elementos e trocando se necessário
            if node1.data > node2.data:
                temp = node1.data
                node1.data = node2.data
                node2.data = temp

# Função auxiliar para obter o nó em uma posição específica
def get_node_at(self, pos):
    if 0 <= pos < self.size:
        ponteiro = self.head
        for i in range(pos):
            ponteiro = ponteiro.next
        return ponteiro
    else:
        return None

DoublyLinkedList.swap = swap
DoublyLinkedList.bubble_sort = bubble_sort
DoublyLinkedList.get_node_at = get_node_at

#Exemplo de uso
lista=DoublyLinkedList()
lista.append(3)
lista.append(1)        
lista.append(4)
lista.append(1)
lista.append(5)
print("Antes do swap:")
print(list(lista))
lista.swap(2) #Troca os elementos nas posições 2 e 3
print("Depois do swap:")
print(list(lista))
lista.bubble_sort() #Ordena a lista com o Bubble Sort
print("Depois do Bubble Sort:")
print(list(lista))


#Exemplo de Uso
lista = DoublyLinkedList()
lista.append(7)
lista.append(8)
lista.append(9)
lista.append(80)
print("Lista original:", [lista[i] for i in range(len(lista))])
lista.prepend(5)
print("Adicionando no inicio:", [lista[i] for i in range(len(lista))])
lista.append(2)
print("Adicionando no final:", [lista[i] for i in range(len(lista))])
tamanho = len(lista)
print(f"Tamanho da lista: {tamanho}")
primeiro_elemento =lista[0]
print(f"Primeiro elemento da lista: {primeiro_elemento}")
posicao = lista.search(8)
print(f"O número 8 está na posição: {posicao}")
removido_do_inicio = lista.pop()
print("Removido do início:", removido_do_inicio)
print("Resultado:", [lista[i] for i in range(len(lista))])
removido_do_final = lista.pop_back()
print("Removido do final:", removido_do_final)
print("Resultado:", [lista[i] for i in range(len(lista))])


lista = DoublyLinkedList()
lista.append(7)
lista.append(8)
lista.append(9)
lista.append(80)
len(lista)
lista[0]
lista.search(8)

#TesteFuncionamento
#Lista original: [7, 8, 9, 80]
#Adicionando no inicio: [5, 7, 8, 9, 80]
#Adicionando no final: [5, 7, 8, 9, 80, 2]
#Tamanho da lista: 6
#Primeiro elemento da lista: 5
#O número 8 está na posição: 2
#Removido do início: 5
#Resultado: [5, 7, 8, 9, 80]
#Removido do final: 2
#Resultado: [5, 7, 8, 9]
#1

