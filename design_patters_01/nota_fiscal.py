from typing import List
from datetime import date


class Item:
    def __init__(self, descricao: str, valor: float):
        self._descricao: str = descricao
        self._valor: float = valor

    @property
    def descricao(self) -> str:
        return self._descricao

    @property
    def valor(self) -> float:
        return self._valor


class NotaFiscal:
    def __init__(self,
                 razao_social: str,
                 cnpj: str,
                 itens: List[Item],
                 data_de_emissao: date = date.today(),
                 detalhes: str = '',
                 observadores: List[any] = []):
        self._razao_social: str = razao_social
        self._cnpj: str = cnpj
        self._data_de_emissao: date = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não podem ter mais que 20 caracteres')
        self._detalhes: str = detalhes
        self._itens: List[Item] = itens

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self) -> str:
        return self._razao_social

    @property
    def cnpj(self) -> str:
        return self._cnpj

    @property
    def data_de_emissao(self) -> date:
        return self._data_de_emissao

    @property
    def detalhes(self) -> str:
        return self._detalhes


if __name__ == "__main__":
    from criador_de_nota_fiscal import CriadorNotaFiscal

    from observadores import *


    itens_teste: List[Item] = [
        Item(
            'A',
            100
        ),
        Item(
            'B',
            200
        )
    ]

    nota_fiscal: NotaFiscal = NotaFiscal(
        razao_social="FHSA Limitada",
        cnpj="012345678901234",
        itens=itens_teste,
        observadores=[imprime, envia_por_email, salva_no_banco]
    )
    print(nota_fiscal.__dict__)

    # nota_fiscal_criada_com_builder = (CriadorNotaFiscal()
    #                                   .com_razao_social("FHSA Limitada")
    #                                   .com_cnpj("012345678901234")
    #                                   .com_itens(itens_teste)
    #                                   .controi())
    # print(nota_fiscal_criada_com_builder.__dict__)
