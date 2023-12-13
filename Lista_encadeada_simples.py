#Estrutura auxiliar Node(nó)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Implementando uma LinkedList(Lista encadeada)
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

#Adicionar elementos ao final da lista. *lista.append(90)*
    def append(self, elemento):
        if self.head:
            ponteiro = self.head
            while(ponteiro.next):
                ponteiro = ponteiro.next
            ponteiro.next = Node(elemento)
        else:
            #primeiro elemento
            self.head = Node(elemento)
        self.size = self.size + 1

#Tamanho da lista através do *len(lista)*
    def __len__(self):
        """Retorna o tamanha da lista"""
        return self.size

#Leitura do elemento. *lista[1]*
    def __getitem__(self, item):
        ponteiro = self.head
        for i in range(item):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                return None
        if ponteiro:
            return ponteiro.data
        else:
            return None


#Moficar um elemento já existente. *lista [3] = 7*
    def __setitem__(self, item, elemento):
        ponteiro = self.head
        for i in range(item):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                return None
        if ponteiro:
            ponteiro.data = elemento
        else:
            return None

#Buscador de elementos e retornando a posição. *lista.search(56)*
    def search(self, elemento):
        """ Retorna o índice do elemento na lista"""
        ponteiro = self.head
        i = 0
        while(ponteiro):
            if ponteiro.data == elemento:
                return i
            ponteiro = ponteiro.next
            i = i+1
        return None


#Adicionar um elemento em qualquer posição da lista. *lista.insertelem(1, 22)*
    def posi(self, index):
        ponteiro = self.head
        for i in range(index - 1):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                return None
        return ponteiro

    def insertlem(self, index, elemento):
        if index == 0:
            node = Node(elemento)
            node.next = self.head
            self.head = node
        else:
            ponteiro = self.posi(index)
            node = Node(elemento)
            node.next = ponteiro.next
            ponteiro.next = node
        self.size = self.size + 1

#Remover um elemento da lista. *lista.remove(30)
    def remove(self, elemento):
        if self.head == None:
            return None

        elif self.head.data == elemento:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        else:
            antecessor = self.head
            ponteiro = self.head.next
            while(ponteiro):
                if ponteiro.data == elemento:
                    antecessor.next = ponteiro.next
                    ponteiro.next = None
                antecessor = ponteiro
                ponteiro = ponteiro.next
            self.size = self.size - 1
            return True

#Printar a lista. *print(lista)
    def __vis__(self):
        v = ""
        ponteiro = self.head
        while(ponteiro):
            v = v + str(ponteiro.data) + ","
            ponteiro = ponteiro.next
        return v
    def __str__(self):
        return self.__vis__()

#Função pop
    def pop(self, index=None):
        if index is None:
            if self.size == 1:
                elemento_removido = self.head.data
                self.head = None
                self.size = 0
                return elemento_removido
            else:
                ponteiro = self.head
                while ponteiro.next.next:
                    ponteiro = ponteiro.next
                elemento_removido = ponteiro.next.data
                ponteiro.next = None
                self.size -= 1
                return elemento_removido
        else:
            if index == 0:
                elemento_removido = self.head.data
                self.head = self.head.next
                self.size -= 1
                return elemento_removido
            elif 0 < index < self.size:
                ponteiro = self.posi(index - 1)
                elemento_removido = ponteiro.next.data
                ponteiro.next = ponteiro.next.next
                self.size -= 1
                return elemento_removido
            else:
                return None


#testes
lista = LinkedList()
lista.append(7)
lista.append(8)
lista.append(9)
lista.append(80)
lista[1]
print(lista)
lista.pop(1)
print(lista)
