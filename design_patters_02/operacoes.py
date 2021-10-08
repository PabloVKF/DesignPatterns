class Subtracao:
    def __init__(self, expressao_esquerda, expressao_direita):
        self._expressao_esquerda = expressao_esquerda
        self._expressao_direita = expressao_direita

    @property
    def expressao_esquerda(self):
        return self._expressao_esquerda

    @property
    def expressao_direita(self):
        return self._expressao_direita

    def aceita(self, visitor):
        visitor.visita_subtracao(self)

    def avalia(self) -> float:
        return self._expressao_esquerda.avalia() - self._expressao_direita.avalia()


class Soma:
    def __init__(self, expressao_esquerda, expressao_direita):
        self._expressao_esquerda = expressao_esquerda
        self._expressao_direita = expressao_direita

    @property
    def expressao_esquerda(self):
        return self._expressao_esquerda

    @property
    def expressao_direita(self):
        return self._expressao_direita

    def aceita(self, visitor):
        visitor.visita_soma(self)

    def avalia(self) -> float:
        return self._expressao_esquerda.avalia() + self._expressao_direita.avalia()


class Numero:
    def __init__(self, numero):
        self._numero = numero

    def avalia(self) -> float:
        return self._numero

    def aceita(self, visitor):
        visitor.visita_numero(self)


if __name__ == "__main__":
    from impressao import Impresao

    expressao_esquerda_teste = Soma(Numero(10), Numero(20))
    expressao_direita_teste = Soma(Numero(10), Numero(20))
    expressao_conta_teste = Soma(expressao_esquerda_teste, expressao_direita_teste)
    print(expressao_conta_teste.avalia())

    print(Subtracao(Numero(10), Numero(30)).avalia())

    impressao_teste = Impresao()
    expressao_conta_teste.aceita(impressao_teste)
