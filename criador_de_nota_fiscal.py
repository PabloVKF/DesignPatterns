from datetime import date
from typing import List

from nota_fiscal import NotaFiscal, Item


class CriadorNotaFiscal:
    def __init__(self):
        self._razao_social = None
        self._cnpj = None
        self._data_de_emissao = None
        self._itens = None
        self._detalhes = None

    def com_razao_social(self, razao_social: str):
        self._razao_social: str = razao_social
        return self

    def com_cnpj(self, cnpj: str):
        self._cnpj: str = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao: date):
        self._data_de_emissao: date = data_de_emissao
        return self

    def com_itens(self, itens: List[Item]):
        self._itens: List[Item] = itens
        return self

    def com_detalhes(self, detalhes: str):
        self._detalhes: str = detalhes
        return self

    def controi(self):
        if not self._razao_social:
            raise Exception("Razão Social deve ser preenchida")
        if not self._cnpj:
            raise Exception("CNPJ deve ser preenchida")
        if not self._itens:
            raise Exception("Itens deve ser preenchida")
        if not self._data_de_emissao:
            self._data_de_emissao = date.today()
        if not self._detalhes:
            self._detalhes = ''

        return NotaFiscal(
            razao_social=self._razao_social,
            cnpj=self._cnpj,
            itens=self._itens,
            data_de_emissao=self._data_de_emissao,
            detalhes=self._detalhes
        )
