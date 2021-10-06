from typing import List
from abc import ABCMeta, abstractmethod


class Orcamento:
    def __init__(self):
        self._itens: List[Item] = []
        self.estado_atual = EmAprovacao()
        self._desconto_extra = 0
        self.desconto_aplicado = False

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def aplica_desconto_extra(self):
        if not self.desconto_aplicado:
            self.estado_atual.aplica_desconto_extra(self)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')

    def adiciona_desconto_extra(self, desconto):
        self._desconto_extra += desconto

    @property
    def valor(self) -> float:
        total: float = 0.0
        for item in self._itens:
            total += item.valor
        return total - self._desconto_extra

    def obter_itens(self) -> tuple:
        return tuple(self._itens)

    @property
    def total_itens(self) -> int:
        return len(self._itens)

    def adiciona_item(self, item) -> None:
        self._itens.append(item)


class Item:
    def __init__(self, nome: str, valor: float):
        self.__nome: str = nome
        self.__valor: float = valor

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def nome(self) -> str:
        return self.__nome


class EstadoOrcamento(metaclass=ABCMeta):
    @abstractmethod
    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        pass

    @abstractmethod
    def aprova(self, orcamento: Orcamento) -> None:
        pass

    @abstractmethod
    def reprova(self, orcametno: Orcamento) -> None:
        pass

    @abstractmethod
    def finaliza(self, orcamento: Orcamento) -> None:
        pass


class EmAprovacao(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento: Orcamento) -> None:
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento: Orcamento) -> None:
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento: Orcamento) -> None:
        raise Exception("Orçamento em aprovaçãp não pode ser finalizado")


class Aprovado(EstadoOrcamento):

    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento: Orcamento) -> None:
        raise Exception("Orçamento já aprovado")

    def reprova(self, orcamento: Orcamento) -> None:
        raise Exception("Orçamento já aprovado")

    def finaliza(self, orcamento: Orcamento) -> None:
        orcamento.estado_atual = Finalizado()


class Reprovado(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento: Orcamento) -> None:
        raise Exception("Orçamento já reprovado")

    def reprova(self, orcamento: Orcamento) -> None:
        raise Exception("Orçamento já reprovado")

    def finaliza(self, orcamento: Orcamento) -> None:
        orcamento.estado_atual = Finalizado()


class Finalizado(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento) -> None:
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento: Orcamento) -> None:
        raise Exception("Orçamento já finalizado")

    def reprova(self, orcamento: Orcamento) -> None:
        raise Exception("Orçamento já finalizado")

    def finaliza(self, orcamento: Orcamento) -> None:
        raise Exception("Orçamento já finalizado")


if __name__ == "__main__":
    orcamento_teste = Orcamento()
    orcamento_teste.adiciona_item(Item('Item_1', 100))
    orcamento_teste.adiciona_item(Item('Item_2', 50))
    orcamento_teste.adiciona_item(Item('Item_3', 400))

    print(orcamento_teste.valor)

    orcamento_teste.aprova()
    orcamento_teste.aplica_desconto_extra()
    orcamento_teste.finaliza()
    print(orcamento_teste.valor)


