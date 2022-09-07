#modulo orçamento_xls
#Descrição: Este modulo oferece funções para manipular aquivos xls
#Autor: luiznf
#Versão:0.0.1
#Data: hoje

#importação de pacotes


from openpyxl import Workbook

def cria_xls() -> None:
    pasta = Workbook()
    return pasta

def cria_planilha(nome_planilha: str, pasta: Workbook) -> None:
    pasta.active
    pasta.create_sheet(nome_planilha)
