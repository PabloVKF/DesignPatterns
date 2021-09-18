from impostos import ISS, ICMS, ICPP, IKCV


class CalculadoraDeImpostos:
    @staticmethod
    def realiza_calculo(orcamento, imposto) -> None:
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento, Item

    calculador = CalculadoraDeImpostos()
    orcamento_teste = Orcamento()
    orcamento_teste.adiciona_item(Item('ITEM - 1', 50))
    orcamento_teste.adiciona_item(Item('ITEM - 2', 200))
    orcamento_teste.adiciona_item(Item('ITEM - 3', 250))

    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento_teste, ISS())
    calculador.realiza_calculo(orcamento_teste, ICMS())

    print('ISS com ICMS')
    calculador.realiza_calculo(orcamento_teste, ISS(ICMS()))

    print('ICPP e IKCV')
    calculador.realiza_calculo(orcamento_teste, ICPP())
    calculador.realiza_calculo(orcamento_teste, IKCV())

    print("ICPP com IKCV")
    calculador.realiza_calculo(orcamento_teste, ICPP(IKCV()))
