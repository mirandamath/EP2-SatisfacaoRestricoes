import numpy as np
from satisfacao_restricoes import Restricao, SatisfacaoRestricoes

'''
    Abreviações dos equipamentos
    Espectrofotômetro UV-VIS = EV
    Cromatógrafo Gasoso = CG
    Cromatógrafo Líquido = CL
    Espectrômetro Infravermelho = IR
    Microscópio = MP
    Balança Analítica = BA
    Espectrômetro de Massa = EM
    Agitador Magnético = AM
'''

class conflitoEquipamento(Restricao):
    def __init__(self, variavel_1, variavel_2):
        super().__init__([variavel_1, variavel_2])
        self.variavel_1 = variavel_1
        self.variavel_2 = variavel_2

    def esta_satisfeita(self, atribuicao):
        # atribuindo dois valores diferentes para analises que n podem estar em uma msm hora
        if  self.variavel_1 not in atribuicao or self.variavel_2 not in atribuicao:
            return True
        return atribuicao[self.variavel_1] != atribuicao[self.variavel_2]
    
if __name__ == "__main__":

    variaveis = []

    equipamentos = []

    analises = {"Analise01" : ["EV", "CG"],
                "Analise02" : ["CL" , "IR"],
                "Analise03" : ["MP", "BA"],
                "Analise04" : ["EM"],
                "Analise05" : ["AM", "IR"],
                "Analise06" : ["CL" , "EV"],
                "Analise07" : ["EV", "MP"],
                "Analise08" : ["CG"],
                "Analise09" : ["IR", "BA"],
                "Analise10" : ["EM" , "CG"]                
                }
    
    for analise, valor in analises.items():
        for equipamento in valor:
            variaveis.append(analise + "-" + equipamento)
            if equipamento not in equipamentos:
                equipamentos.append(equipamento)

    dominio = {}

    for variavel in variaveis:
        dominio[variavel] = [1,2,3,4,5,6,7,8]

    problema = SatisfacaoRestricoes(variaveis, dominio)
    
    #restringindo para horarios diferentes analises conflitantes
    problema.adicionar_restricao(conflitoEquipamento('Analise01-EV', 'Analise07-EV'))
    problema.adicionar_restricao(conflitoEquipamento('Analise01-EV', 'Analise06-EV'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise01-EV', 'Analise01-CG'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise01-CG', 'Analise08-CG'))
    problema.adicionar_restricao(conflitoEquipamento('Analise01-CG', 'Analise10-CG'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise02-CL', 'Analise06-CL'))
    problema.adicionar_restricao(conflitoEquipamento('Analise02-CL', 'Analise02-IR'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise02-IR', 'Analise05-IR'))
    problema.adicionar_restricao(conflitoEquipamento('Analise02-IR', 'Analise09-IR'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise03-MP', 'Analise07-MP'))
    problema.adicionar_restricao(conflitoEquipamento('Analise03-MP', 'Analise03-BA'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise03-BA', 'Analise09-BA'))

    problema.adicionar_restricao(conflitoEquipamento('Analise04-EM', 'Analise10-EM'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise05-IR', 'Analise09-IR'))

    problema.adicionar_restricao(conflitoEquipamento('Analise05-AM', 'Analise05-IR'))

    problema.adicionar_restricao(conflitoEquipamento('Analise06-EV', 'Analise07-EV'))
    problema.adicionar_restricao(conflitoEquipamento('Analise06-EV', 'Analise06-CL'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise07-EV', 'Analise07-MP'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise08-CG', 'Analise10-CG'))
    
    problema.adicionar_restricao(conflitoEquipamento('Analise09-IR', 'Analise09-BA'))

    problema.adicionar_restricao(conflitoEquipamento('Analise10-EM', 'Analise10-CG'))


    resposta = problema.busca_backtracking()

    if resposta is None:
        print("Nenhuma resposta encontrada")
    else:
        print(resposta)
        for chave, valor in resposta.items():
            print(f"Hora {valor}: {chave}")
    

    