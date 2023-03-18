import numpy as np
from satisfacao_restricoes import Restricao, SatisfacaoRestricoes




if __name__ == "__main__":

    variaveis = []

    equipamentos = []

    analises = {"Analise1" : ["Espectrofotômetro UV-VIS", "Cromatógrafo Gasoso"],
                "Analise2" : ["Cromatógrafo Líquido" , "Espectrômetro Infravermelho"],
                "Analise3" : ["Microscópio", "Balança Analítica"],
                "Analise4" : ["Espectrômetro de Massa"],
                "Analise5" : ["Agitador Magnético", "Espectrômetro Infravermelho"],
                "Analise6" : ["Cromatógrafo Líquido" , "Espectrofotômetro UV-VIS"],
                "Analise7" : ["Espectrofotômetro UV-VIS", "Microscópio"],
                "Analise8" : ["Cromatógrafo Gasoso"],
                "Analise9" : ["Espectrômetro Infravermelho", "Balança Analítica"],
                "Analise10" : ["Espectrômetro de Massa" , "Cromatógrafo Gasoso"]                
                }
    
    for analise, valor in analises.items():
        for equipamento in valor:
            variaveis.append(analise + "_" + equipamento)
            if equipamento not in equipamentos:
                equipamentos.append(equipamento)

    dominio = {}

    for variavel in variaveis:
        dominio[variavel] = [1,2,3,4,5,6,7,8]

    problema = SatisfacaoRestricoes(variaveis, dominio)

    # problema.adicionar_restricao(RestricaoEmUso("Analise1_Espectrofotômetro UV-VIS", "Espectrofotômetro UV-VIS"))

    solucao = problema.busca_backtracking()

    print(variaveis)
    print(equipamentos)
    print(dominio)
    