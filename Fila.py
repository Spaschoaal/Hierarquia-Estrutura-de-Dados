from collections import deque
from datetime import datetime, timedelta

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.tempo_atendimento = 5  # Tempo médio de atendimento em minutos
        self.hora_entrada = datetime.now()
        self.atualizar_horas()

    def atualizar_horas(self):
        self.hora_prevista_atendimento = self.hora_entrada + timedelta(minutes=self.tempo_atendimento)
        self.hora_atual = datetime.now()

class Fila:
    def __init__(self):
        self.items = deque()

    def enfileirar(self, pessoa):
        self.items.append(pessoa)
        self.atualizar_contadores()

    def desenfileirar(self):
        if not self.fila_vazia():
            pessoa_atendida = self.items.popleft()
            self.atualizar_contadores()
            return pessoa_atendida
        else:
            raise IndexError("A fila está vazia")

    def desistir(self, nome_pessoa):
      for pessoa in self.items:
        if pessoa.nome == nome_pessoa:
          self.items.remove(pessoa)
          self.atualizar_contadores()
          return
      print(f"A pessoa {nome_pessoa} não está na fila.")

    def atrasar_atendimento(self, pessoa, tempo_atraso):
        if pessoa in self.items:
            index_pessoa = self.items.index(pessoa)
            for i in range(index_pessoa, len(self.items)):
                self.items[i].tempo_atendimento += tempo_atraso
            self.atualizar_contadores()

    def fila_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

    def tempo_espera_estimado(self, pessoa):
        fila_temporaria = self.items.copy()
        fila_temporaria.append(pessoa)
        posicao_na_fila = len(fila_temporaria)
        tempo_espera_estimado = posicao_na_fila * pessoa.tempo_atendimento
        return tempo_espera_estimado

    def tempo_espera_pessoa(self, pessoa_alvo):
        for i, pessoa in enumerate(self.items):
            if pessoa == pessoa_alvo:
                tempo_espera = (i + 1) * pessoa.tempo_atendimento
                return tempo_espera, pessoa.hora_entrada, pessoa.hora_prevista_atendimento, pessoa.hora_atual
        return None

    def atualizar_contadores(self):
        tempo_restante_total = 0
        for i, pessoa in enumerate(self.items):
            pessoa.atualizar_horas()
            pessoa.tempo_restante = (i + 1) * pessoa.tempo_atendimento
            pessoa.hora_prevista_atendimento = datetime.now() + timedelta(minutes=tempo_restante_total)
            tempo_restante_total += pessoa.tempo_atendimento

if __name__ == "__main__":
    usuario = input ('Digite o seu nome para obter informações sobre a fila: ')
    pessoainicial = Pessoa(usuario)
    fila = Fila()

    while True:
        print("\n1 - Adicionar pessoa à fila")
        print("2 - Calcular tempo de espera")
        print("3 - Atender próxima pessoa")
        print("4 - Desistir de uma pessoa")
        print("5 - Atrasar atendimento")
        print("6] - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da pessoa: ")
            nova_pessoa = Pessoa(nome)
            fila.enfileirar(nova_pessoa)
            print(f"{nova_pessoa.nome} foi adicionado(a) à fila.")

        elif opcao == "2":
            tempo_espera_estimado = fila.tempo_espera_estimado(pessoainicial)
            print(f"Tempo de espera estimado: {tempo_espera_estimado} minutos.")
            desicao = input('Deseja entrar na fila?')
            if desicao == 'sim' or 'Sim':
              fila.enfileirar(pessoainicial)
              tempo_espera_pessoainicial = fila.tempo_espera_pessoa(pessoainicial)
              print (f"Você foi adicionado(a) à fila. "
              f"Tempo de espera atualizado: {tempo_espera_pessoainicial[0]:.2f} minutos, "
              f"Hora de entrada: {tempo_espera_pessoainicial[1].strftime('%H:%M:%S')}, "
              f"Hora prevista de atendimento: {tempo_espera_pessoainicial[2].strftime('%H:%M:%S')}, "
              f"Hora atual: {tempo_espera_pessoainicial[3].strftime('%H:%M:%S')}")
            else:
              break

        elif opcao == "3":
            fila.desenfileirar()
            tempo_espera_atualizado = fila.tempo_espera_pessoa(pessoainicial)
            print (f"Alguém foi atendido. "
            f"Tempo de espera atualizado: {tempo_espera_atualizado[0]:.2f} minutos, "
            f"Hora de entrada: {tempo_espera_atualizado[1].strftime('%H:%M:%S')}, "
            f"Hora prevista de atendimento: {tempo_espera_atualizado[2].strftime('%H:%M:%S')}")

        elif opcao == "4":
            nome_desistente = input("Digite o nome da pessoa que desistiu: ")
            fila.desistir(nome_desistente)
            tempo_espera_desistir = fila.tempo_espera_pessoa(pessoainicial)
            print(f"Alguém desistiu da fila. "
            f"Tempo de espera atualizado: {tempo_espera_desistir[0]:.2f} minutos, "
            f"Hora de entrada: {tempo_espera_desistir[1].strftime('%H:%M:%S')}, "
            f"Hora prevista de atendimento: {tempo_espera_desistir[2].strftime('%H:%M:%S')}")

        elif opcao == "5":
            tempo_atraso = int(input("Digite o tempo de atraso em minutos: "))
            fila.atrasar_atendimento(pessoainicial, tempo_atraso)
            tempo_espera_atraso = fila.tempo_espera_pessoa(pessoainicial)
            print(f"O atendimento foi atrasado em {tempo_atraso} minutos."
            f"Tempo de espera atualizado: {tempo_espera_atraso[0]:.2f} minutos, "
            f"Hora de entrada: {tempo_espera_atraso[1].strftime('%H:%M:%S')}, "
            f"Hora prevista de atendimento: {tempo_espera_atraso[2].strftime('%H:%M:%S')}")

        elif opcao == "6":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
