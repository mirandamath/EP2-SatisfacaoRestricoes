# EP2-SatisfacaoRestricoes


##### Suponha que um laboratório de química precisa organizar o uso de seus equipamentos para garantir que todas as análises necessárias possam ser realizadas dentro do prazo esperado e que as restrições de segurança e capacidade dos equipamentos sejam cumpridas. O laboratório possui um conjunto de equipamentos, como balanças, espectrômetros e microscópios, que são usados para realizar diferentes tipos de análises químicas.

##### Existem várias análises que precisam ser realizadas, cada uma com seus próprios requisitos de equipamentos e tempo de execução. Alguns equipamentos só podem ser usados para uma análise específica, enquanto outros podem ser compartilhados entre diferentes análises.

##### As restrições a serem satisfeitas incluem:

##### 1. Cada equipamento tem uma capacidade máxima de uso diário e só pode ser usado para uma análise por vez.
##### 2. Uma análise não pode estar em 2 equipamentos ao mesmo tempo.
##### 3. Cada análise fica 1 hora em cada equipamento

##### O objetivo é encontrar um cronograma de uso de equipamentos que atenda a todas as restrições e minimize o tempo total necessário para concluir todas as análises.

##### Para ajudar a visualizar o problema, aqui está uma tabela com as análises, os equipamentos necessários e os tempos de execução estimados:

##### **Tabela de Análises**

| Análise | Equipamentos Necessários |
| --- | --- |
| Análise 1 | Espectrofotômetro UV-VIS, Cromatógrafo Gasoso |
| Análise 2 | Cromatógrafo Líquido, Espectrômetro Infravermelho |
| Análise 3 | Microscópio, Balança Analítica |
| Análise 4 | Espectrômetro de Massa |
| Análise 5 | Agitador Magnético, Espectrômetro Infravermelho |
| Análise 6 | Cromatógrafo Líquido, Espectrofotômetro UV-VIS |
| Análise 7 | Espectrofotômetro UV-VIS, Microscópio |
| Análise 8 | Cromatógrafo Gasoso |
| Análise 9 | Espectrômetro Infravermelho, Balança Analítica |
| Análise 10 | Espectrômetro de Massa, Cromatógrafo Gasoso |

**Tabela de Restrições**

| Equipamento | Tempo Máximo de Uso por Dia |
| --- | --- |
| Balança Analítica | 6 horas |
| Agitador Magnético | 4 horas |
| Cromatógrafo Líquido | 8 horas |
| Cromatógrafo Gasoso | 6 horas |
| Espectrofotômetro UV-VIS | 4 horas |
| Espectrômetro Infravermelho | 6 horas |
| Espectrômetro de Massa | 4 horas |
| Microscópio | 6 horas |

### Para gerenciarmos onde e em qual horário cada Equipamento será usado usamos BackTracking junto as restrições que criamos

# Modelando o problema
 
 
#### Decidimos modelar nossa variáveis como sendo o conjunto das Analises com seus respectivos equipamentos de modo que cada variavel é uma string que concatena uma analise e um equipamento e nosso dominio são os horários de uso


# Resultado do Algoritmo de BackTracking

As linhas horrespondem aos equipamento, as colunas as Horas que foram necessários para o plano de uso das analises e as células correspondem as análises

![image](https://user-images.githubusercontent.com/80297874/226154047-5cf485d6-26df-4cac-957e-32b6dffef54e.png)
