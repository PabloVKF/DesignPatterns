from impostos import ISS, ICMS


class CalculadoraDeImpostos(object):
    @staticmethod
    def realiza_calculo(orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = CalculadoraDeImpostos()
    orcamento_teste = Orcamento(500)

    calculador.realiza_calculo(orcamento_teste, ISS)
    calculador.realiza_calculo(orcamento_teste, ICMS)
