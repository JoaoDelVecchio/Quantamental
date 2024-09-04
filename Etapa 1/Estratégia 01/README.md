## Problemas, Sugestões e Discussões a respeito da Estratégia 1


### Etapa de otimização dos hiperparâmetros $(N,x_{days})$
* **Sugestão:** Talvez seja melhor considerar a melhor tupla $(N,x_{days})$ para cada moeda em específico?
* **Problema e Sugestão:** *Minha Otimização pode ter ficado levemente enviesada -* eu utilizei todo o histórico de preço de cada moedas para calcular o MSE. Entretanto talvez seja melhor eu considerar a tupla que gera um MSE mínimo para uma primeira parte de seu histórico de retornos, e testar a validade dessa tupla na parte em seguinte.
* **Problema**: A otimização demorou **muito** (cerca de 3 horas)
* **Discussão**: Backtest ocorreria da seguinte forma: no período de, e.g. 2018 a 2023, para cada instante $t$ eu calculo $E[R_t | N, x_{days}, R_{t-1},...]$. Consequentemente $(N,x_{days})$ só podem ser encontrados com informações de $t-1$ para trás.
* **Discussão:** Então fica a dúvida: Escolhemos um $(N,x_{days})$ fixo ou Para cada instante t calculamos $(N,x_{days})$?
* **Sugestão:** Construir uma otimização da seguinte forma - para cada instante t, para cada criptomoeda específica, eu encontro os valores de $(N,x_{days})$ ótimos. Como métrica, basta encontrar o MSE que essa ideia vai gerar quando aplicada em todas as moedas e em todo intervalo de tempo.
* **Sugestão:** Para evitar um tempo infinito, tente construir de tal forma que , quando num tempo t, abendo o MSE de cada tupla $(N,x_{days})$, consiga atualizá-los de forma mais ágil.

$$
MSE_{New}^2 = MSE^2 + (E[R_{t-1}] - R_{t-1})^2
$$

* **Problema:** Da forma como está praticamente todos os casos em que ou N ou x são um pouco grandes não retornam valores, por conta de algumas moedas que são muito recentes, gerando resultado NaN
