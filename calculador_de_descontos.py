from descontos import DescontoCincoItens, DescontoMaisDeQuintosReais, SemDesconto


class CalculadorDeDescintos:
    @staticmethod
    def calcula(orcamento) -> float:
        desconto = DescontoCincoItens(
            DescontoMaisDeQuintosReais(SemDesconto())
        ).calcula(orcamento)

        return desconto


if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcament_teste = Orcamento()
    orcament_teste.adiciona_item(Item('ITEM - 1', 100))
    orcament_teste.adiciona_item(Item('ITEM - 2', 50))
    orcament_teste.adiciona_item(Item('ITEM - 3', 400))
    orcament_teste.adiciona_item(Item('ITEM - 3', 400))
    orcament_teste.adiciona_item(Item('ITEM - 3', 400))
    orcament_teste.adiciona_item(Item('ITEM - 3', 400))

    calculador_teste = CalculadorDeDescintos()

    desconto_teste = calculador_teste.calcula(orcament_teste)

    print('Desconto calculado {}'.format(round(desconto_teste, 2)))
