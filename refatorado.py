from abc import ABC, abstractmethod


class Observador(ABC):
    @abstractmethod
    def notificarCampeao(self, vencedor):
        pass


class Continente(Observador):
    def __init__(self, nome):
        self.nome = nome

    def notificarCampeao(self, vencedor):
        print(f"Região {self.nome}: Jogador {vencedor} conquistou esta região!")


class JogoWar:
    def __init__(self):
        self.observadores = []

    def adicionarObservador(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def removerObservador(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)
        else:
            print(f"O observador {observador} não está na lista de observadores.")

    def notificarObservadores(self, vencedor):
        for observador in self.observadores:
            observador.notificarCampeao(vencedor)

    def jogadorVence(self, vencedor):
        print(f"Jogador {vencedor} venceu o jogo!")
        self.notificarObservadores(vencedor)

if __name__ == "__main__":
    continentes = [Continente("América do Norte"), Continente("Ásia")]

    jogo = JogoWar()

    for continente in continentes:
        jogo.adicionarObservador(continente)

    jogo.jogadorVence(1)
