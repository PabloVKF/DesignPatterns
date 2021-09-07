from abc import ABCMeta, abstractmethod


class TemplateImpostoCondicional(metaclass=ABCMeta):
    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ISS:
    @staticmethod
    def calcula(orcamento) -> float:
        return orcamento.valor * 0.1


class ICMS:
    @staticmethod
    def calcula(orcamento) -> float:
        return orcamento.valor * 0.06


class ICPP(TemplateImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento) -> bool:
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento) -> bool:
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento) -> bool:
        return orcamento.valor * 0.05


class IKCV(TemplateImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento) -> bool:
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento) -> bool:
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento) -> bool:
        return orcamento.valor * 0.06

    @staticmethod
    def __tem_item_maior_que_100_reais(orcamento) -> bool:
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False
