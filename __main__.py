

import manipulaxls


def main():
    lista_planilhas = ['receitas', 'despesas', 'resultado']
    pasta = manipulaxls.cria_xls()
    pasta.active
    for planilha in lista_planilhas:
        manipulaxls.cria_planilha(planilha, pasta)
    pasta.save('orcamento.xlsx')
if __name__ == "__main__":
    main()
    
