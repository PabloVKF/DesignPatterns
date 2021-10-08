from datetime import date


class Contrato:

    def __init__(self, data: date, cliente: str, tipo: str):
        self._data = data
        self._cliente = cliente
        self._tipo = tipo

    @property
    def data(self):
        return self._data

    def _set_data(self, data):
        self._data = data

    @property
    def cliente(self):
        return self._cliente

    def _set_cliente(self, cliente):
        self._cliente = cliente

    @property
    def tipo(self):
        return self._tipo

    def _set_tipo(self, tipo):
        self._tipo = tipo

    def avanca(self):
        if self._tipo == "NOVO":
            self._tipo = "EM ANDAMENTO"
        elif self._tipo == "EM ANDAMENTO":
            self._tipo = "ACERTADO"
        elif self._tipo == "ACERTADO":
            self._tipo = "CONCLUIDO"

    def salva_estado(self):
        return Estado(Contrato(
            data=self._data,
            cliente=self._cliente,
            tipo=self._tipo
        ))

    def restaura_estado(self, estado):
        self._cliente = estado.contrato.cliente
        self._data = estado.contrato.data
        self._tipo = estado.contrato.tipo


class Estado:
    def __init__(self, contrato):
        self._contrato = contrato

    @property
    def contrato(self):
        return self._contrato


class Historico:
    def __init__(self):
        self._estados_salvos = []

    def obtem_estado(self, indice):
        return self._estados_salvos[indice]

    def adiciona_estado(self, estado):
        self._estados_salvos.append(estado)


if __name__ == "__main__":

    historico = Historico()

    contrato = Contrato(
        data=date.today(),
        cliente='Flávio Almeida',
        tipo='NOVO'
    )

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    print(contrato.__dict__)
    contrato.restaura_estado(historico.obtem_estado(1))
    print(contrato.__dict__)
