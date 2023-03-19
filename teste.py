import numpy as np
from satisfacao_restricoes import Restricao, SatisfacaoRestricoes

def setEquip(variavel : dict, nome, maxHoras):
    horas = []
    for i in range(1, maxHoras + 1):
        horas.append("Hora" + str(i))
    variavel[nome] = horas

# Restringe qual analise eh usada no equipamento
def alteraDominioDaVariavel(dominio : dict, variavel, analise):
    dominio[variavel] = analise

class RestricaoChecaDominio(Restricao):
    def __init__(self, variavel, dominio):
        super().__init__(variavel)
        self.variavel = variavel
        self.dominio = dominio
    
    def esta_satisfeita(self, atribuicao):
        if str(atribuicao.keys()) not in self.dominio:
            return False
        return True

class RestringeEquip(Restricao):
    def __init__(self, variavel, dominio):
        super().__init__([variavel])
        self.variavel = variavel
        self.dominio = dominio

    def esta_satisfeita(self, atribuicao):
        # se nenhuma analise ja esta usando esse horario do equipamento
        if self.variavel not in atribuicao:
            return True
        # 
        # animais que não devem estar na mesma jaula
        return atribuicao[self.variavel] != atribuicao[self.estado2]

if __name__ == "__main__":

    equipamentos = {}

    setEquip(equipamentos, "Balanca Analitica", 6)
    setEquip(equipamentos, "Agitador Magnetico", 4)
    setEquip(equipamentos, "Cromatografo Liquido", 8)
    setEquip(equipamentos, "Cromatografo Gasoso", 6)
    setEquip(equipamentos, "Espectrofotometor UV-VIS", 4)
    setEquip(equipamentos, "Espectrometro Infravermelho", 6)
    setEquip(equipamentos, "Espectrometro de Massa", 4)
    setEquip(equipamentos, "Microscopio", 6)

    dominio = {}
    # for var in equipamentos:
    #     dominio[var] = np.array(["Analise1-Hora1", "Analise1-Hora2","Análise2-Hora1","Análise2-Hora2","Análise2-Hora3", "Análise3-Hora1","Análise3-Hora2","Análise4-Hora1","Análise5-Hora1", "Análise5-Hora2","Análise5-Hora3", "Análise6-Hora1", "Análise6-Hora2","Análise7-Hora1","Análise7-Hora2", "Análise8-Hora1","Análise9-Hora1","Análise9-Hora2", "Análise10-Hora1","Análise10-Hora2"])

    alteraDominioDaVariavel(dominio, "Balanca Analitica", ["Analise3", "Analise9"])
    alteraDominioDaVariavel(dominio, "Agitador Magnetico", ["Analise5"])
    alteraDominioDaVariavel(dominio, "Cromatografo Liquido", ["Analise2", "Analise6"])
    alteraDominioDaVariavel(dominio, "Cromatografo Gasoso", ["Analise1", "Analise8", "Analise10"])
    alteraDominioDaVariavel(dominio, "Espectrofotometor UV-VIS", ["Analise1", "Analise6", "Analise7"])
    alteraDominioDaVariavel(dominio, "Espectrometro Infravermelho", ["Analise2" , "Analise5", "Analise9"])
    alteraDominioDaVariavel(dominio, "Espectrometro de Massa", ["Analise4", "Analise10"])
    alteraDominioDaVariavel(dominio, "Microscopio", ["Analis3", "Analise7"])

    problema = SatisfacaoRestricoes(equipamentos, dominio)

    problema.adicionar_restricao(RestricaoChecaDominio(["Balanca Analitica"], dominio))

    print(dominio)
    
    # problema.adicionar_restricao(RestringeEquip(variaveis[0], "Analise3-Hora2"))
    # problema.adicionar_restricao(RestringeEquip(variaveis[0], "Analise9-Hora2"))

    # print dominios das variaveis
    # for variavel in problema.restricoes:
    #     for i in range(len(problema.restricoes[variavel])):
    #         print(problema.restricoes[variavel][i].dominio)
    
    resposta = problema.busca_backtracking()
    
    # if resposta is None:
    #     print("Nenhuma resposta encontrada")
    # else:
    #     print(resposta)