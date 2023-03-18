import numpy as np
from satisfacao_restricoes import Restricao, SatisfacaoRestricoes

# Definir as variáveis e seus respectivos domínios
equipamentos = ['Balança Analítica', 'Agitador Magnético', 'Cromatógrafo Líquido', 
                'Cromatógrafo Gasoso', 'Espectrofotômetro UV-VIS', 'Espectrômetro Infravermelho', 
                'Espectrômetro de Massa', 'Microscópio']

analises = ['Análise 1', 'Análise 2', 'Análise 3', 'Análise 4', 'Análise 5', 
            'Análise 6', 'Análise 7', 'Análise 8', 'Análise 9', 'Análise 10']

dominios = {}
for equipamento in equipamentos:
    dominios[equipamento] = analises

# Definir as restrições
class UsoDiarioMaximo(Restricao):
    def __init__(self, equipamento, tempo_maximo):
        super().__init__([equipamento])
        self.equipamento = equipamento
        self.tempo_maximo = tempo_maximo

    def esta_satisfeita(self, atribuicao):
        if self.equipamento not in atribuicao:
            return True

        tempo_uso = sum([atribuicao[var] == self.equipamento for var in atribuicao])
        return tempo_uso <= self.tempo_maximo

class AnalisesConcorrentes(Restricao):
    def __init__(self, equipamento_1, equipamento_2):
        super().__init__([equipamento_1, equipamento_2])
        self.equipamento_1 = equipamento_1
        self.equipamento_2 = equipamento_2

    def esta_satisfeita(self, atribuicao):
        if self.equipamento_1 not in atribuicao or self.equipamento_2 not in atribuicao:
            return True

        return atribuicao[self.equipamento_1] != atribuicao[self.equipamento_2]

class DuracaoAnalise(Restricao):
    def __init__(self, equipamento, max_duracao):
        super().__init__([equipamento])
        self.equipamento = equipamento
        self.max_duracao = max_duracao
    
    def esta_satisfeita(self, atribuicao):
        dominio_equipamento = atribuicao[self.equipamento]
        duracao_analise = 0

        for valor in dominio_equipamento:
            duracao_analise = len(atribuicao)
        return duracao_analise <= self.max_duracao

# for equipamento in equipamentos:
#     restricoes.append(DuracaoAnalise(equipamento))

# Resolver o problema usando busca de backtracking
problema = SatisfacaoRestricoes(equipamentos, dominios)

problema.adicionar_restricao(AnalisesConcorrentes('Balança Analítica', 'Microscópio'))
problema.adicionar_restricao(AnalisesConcorrentes('Agitador Magnético', 'Espectrômetro Infravermelho'))
problema.adicionar_restricao(AnalisesConcorrentes('Cromatógrafo Líquido', 'Cromatógrafo Gasoso'))
problema.adicionar_restricao(AnalisesConcorrentes('Espectrofotômetro UV-VIS', 'Microscópio'))

problema.adicionar_restricao(UsoDiarioMaximo(equipamentos[0], 6))
problema.adicionar_restricao(UsoDiarioMaximo(equipamentos[1], 4))
problema.adicionar_restricao(UsoDiarioMaximo(equipamentos[2], 8))
problema.adicionar_restricao(UsoDiarioMaximo(equipamentos[3], 6))
problema.adicionar_restricao(UsoDiarioMaximo(equipamentos[4], 4))
problema.adicionar_restricao(UsoDiarioMaximo(equipamentos[5], 6))
problema.adicionar_restricao(UsoDiarioMaximo(equipamentos[6], 4))
problema.adicionar_restricao(UsoDiarioMaximo(equipamentos[7], 6))

problema.adicionar_restricao(DuracaoAnalise(equipamentos[0], 2))

solucao = problema.busca_backtracking()

print(problema.variaveis)

print(problema.dominios)

# if solucao is not None:
#     print("Solução encontrada:")
#     for equipamento, sala in solucao.items():
#         print(f"{equipamento} -> {sala}")
# else:
#     print("Não foi possível encontrar uma solução para o problema.")
