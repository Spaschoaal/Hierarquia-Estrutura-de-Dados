class No:  # Classe Nó
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
        self._tamanho = 0

    def push(self, dado):
        if not isinstance(dado, (int, str)) and not (isinstance(dado, tuple) and len(dado) == 4):
            raise Exception("TipoErro")

        novo_no = No(dado)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self._tamanho += 1

    def pop(self):
        if self.pilha_esta_vazia():
            raise Exception("PilhaVaziaErro")

        dado = self.topo.dado
        self.topo = self.topo.proximo
        self._tamanho -= 1
        return dado

    def pilha_esta_vazia(self):
        return self.topo is None

    def pilha_esta_cheia(self):
        return False

    def swap(self):
        if self._tamanho > 1:
            topo_dado = self.topo.dado
            segundo_no = self.topo.proximo
            self.topo.dado = segundo_no.dado
            segundo_no.dado = topo_dado

    def obter_tamanho(self):                                                                                                                                                                                                                                                                                                                                                                            
        return self._tamanho
