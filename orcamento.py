class Orcamento(object):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor


if __name__ == "__main__":
    orcamento_teste = Orcamento(500)
    print(orcamento_teste.valor)
