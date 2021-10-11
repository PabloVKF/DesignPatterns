from datetime import date
from abc import ABCMeta, abstractmethod


class Pedido:
    def __init__(self, cliente, valor):
        self._cliente = cliente
        self._valor = valor
        self._status = 'NOVO'
        self._data_finalizacao = None

    @property
    def cliente(self):
        return self._cliente

    @property
    def valor(self):
        return self._valor

    @property
    def status(self):
        return self._status

    @property
    def data_finalizacao(self):
        return self._data_finalizacao

    def paga(self):
        self._status = 'PAGO'

    def finaliza(self):
        self._data_finalizacao = date.today()
        self._status = 'ENTREGUE'


class Comando(metaclass=ABCMeta):
    @abstractmethod
    def executa(self):
        pass


class ConcluiPedido(Comando):
    def __init__(self, pedido):
        self._pedido = pedido

    def executa(self):
        self._pedido.finaliza()


class PagaPedido(Comando):
    def __init__(self, pedido):
        self._pedido = pedido

    def executa(self):
        self._pedido.paga()


class FilaTrabalho:
    def __init__(self):
        self._comando = []

    def adiciona(self, comando):
        self._comando.append(comando)

    def processa(self):
        for comando in self._comando:
            comando.executa()

if __name__ == '__main__':
    pedido_1 = Pedido('Pablo', 57468)
    pedido_2 = Pedido('João', 13873)

    fila_de_trabalho = FilaTrabalho()

    comando_1 = ConcluiPedido(pedido_1)
    comando_2 = PagaPedido(pedido_1)
    comando_3 = ConcluiPedido(pedido_2)

    fila_de_trabalho.adiciona(comando_1)
    fila_de_trabalho.adiciona(comando_2)
    fila_de_trabalho.adiciona(comando_3)

    fila_de_trabalho.processa()