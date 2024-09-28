Projeto Quant.

*Autores: Bruno Franco, Jean Carlo Amaral, João Matheus Del Vecchio.*

# Referências

### **Papers**
* [The best of two worlds: Forecasting high frequency volatility for cryptocurrencies and traditional currencies with Support Vector Regression](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/Forecasting%20HFT%20volatility%20for%20crypto%20with%20SVM)
* [Intelligent forecasting with machine learning trading systems in chaotic intraday Bitcoin market](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/forecasting%20with%20machine%20learning%20trading%20in%20chaotic%20intraday%20Bitcoin)
* [Reinforcement Learning for Quantitative Trading](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/Reinforcement%20Learning%20for%20Quantitative%20Trading)
* [Applying Artificial Intelligence in Cryptocurrency Markets: A Survey](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/Applying%20Artificial%20Intelligence%20in%20Cryptocurrency%20Markets)
* [Anticipating Cryptocurrency Prices Using Machine Learning](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/Anticipating%20Cryptocurrency%20Prices%20Using%20Machine%20Learning)
* [Trading and Arbitrage in Cryptocurrency Markets](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/Trading%20and%20Arbitrage)
* [AUTOMATED CRYPTOCURRENCIES PRICES PREDICTION USING MACHINE LEARNING](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/AUTOMATED%20CRYPTOCURRENCIES%20PRICES%20PREDICTION%20USING%20ML)
* [Cryptocurrency Trading Using Machine Learning](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/Cryptocurrency%20Trading%20Using%20Machine%20Learning)
* [A deep Q-learning portfolio management framework for the cryptocurrency market](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/A%20deep%20Q-learning%20portfolio%20management%20framework)
* [EXTREME CORRELATION IN CRYPTOCURRENCY MARKETS](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/EXTREME%20CORRELATION%20IN%20CRYPTOCURRENCY%20MARKETS)
* [Market Sentiment and an Overnight Anomaly](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/Market%20Sentiment%20and%20an%20Overnight%20Anomaly)
* [Seasonality, Trend-following, and Mean reversion in Bitcoin](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/Seasonality%2C%20Trend-following%2C%20and%20Mean%20reversion%20in%20Bitcoin)
* [Cryptocurrency trading: a comprehensive survey](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Papers/Cryptocurrency%20trading%20a%20comprehensive)

### **Livros**
* [Advances in Financial Machine Learning. LOPEZ DE PRADO, Marcos](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Livros/Marcos%20Lopez%20%20Advances%20in%20Financial%20Machine%20Learning)
* [Artificial Intelligence in Finance A Python-Based Guide. Hilpisch, Yves.](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Livros/artificial-intelligence-in-finance-a-python-based-guide)
* [Introduction to the Economics and Mathematics of Financial Markets. ZAPATERO, Fernando.](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Livros/Caltech%20-%20Mathematical%20Models%20for%20Finance)
* [MACHINE LEARNING FOR ASSET MANAGERS. LOPEZ DE PRADO, Marcos](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Livros/MACHINE%20LEARNING%20FOR%20ASSET%20MANAGERS)
* [Statistical Analysis of Financial Data. GENTLE, James.](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Livros/statistical-analysis-of-financial-data)
* [Analysis of Financial Time Series. RUEY S. TSAY](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Livros/analysis-of-financial-time-series)
* [THE ANALYSIS OF TIME SERIES AN INTRODUCTION. Chris Chatfield.](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Livros/the-analysis-of-time-series-an-introduction-5-ed)

### Sites
* [Awesome Systematic Trading Repository](https://github.com/paperswithbacktest/awesome-systematic-trading.git)




# 1. Fundamentação e Estrutura

O projeto tem como objetivo criar uma estratégia quantitativa de investimento aplicada no mercado de criptomoedas, utilizando de Redes Neurais com arquiteturas LSTM para a predição do retorno de cada ativo e da teoria de portifólio de Markowitz para a construção de uma carteira otimizada.

## Tese

O mercado de Criptomoedas possui duas características singulares que o diferencia dos outros tipos de ativos financeiros: **alta** **volatilidade** dos preços e **alta** **correlação** entre as principais moedas. 

A primeira característica implica em uma dificuldade inerente em se utilizar de modelos estatísticos e econometricos bem estabelecidos, como estratégias de Média Móvel, Trend Following ou Reversão a Média para a predição do retorno de Criptomoedas, uma vez que esses modelos econometricos baseados em regressão são extremamente dependentes da linearidade dessas características, porém a alta volatilidade nos dá indícios de uma dependência não linear entre os dados passados e o alvo futuro. Desse modo, temos a hipótese de que, para o mercado de Criptomoedas, a utilização de modelos de Machine Learning mais complexos não é apenas interessante, mas **decisiva** e **fundamental** para uma estratégia quantitativa eficiente nesse setor.

A respeito da segunda, podemos elaborar a tese de que, para a predição mais efetiva do valor esperado de uma criptomoeda, devemos levar em consideração dados e informações das outras semelhantes para a modelagem do problema.

Além disso, podemos hipotetizar uma possível dependencia entre o preço das Criptomoedsa e fatores que influênciam a atividade de mineiração de Bitcoin, como preço de óleo e gás, ou custo de energia nos países chaves para a mineração, ou catástrofes climáticas de escopo global.

## Revisão da Literatura

A principal revisão de literatura é o aritigo ""Anticipating Cryptocurrency Prices Using Machine Learning" que utiliza de 3 modelos de Machine Learning para prever retorno de uma carteira de criptomoedas, sendo um desses modelos uma Rede Neural com Arquitetura LSTM. 

Nos dois modelos iniciais ele utiliza a ideia de se basear nos dados das outras moedas também para a modelagem do preço futura de uma única moedas espcífica. Entretanto, ele não aplica essa ideia no modelo de LSTM, no qual ele se limita a utilizar o retorno de uma certa moeda X nos ultimos T dias para prever o valor futura. Além disso, o paper é bastante vago quanto a forma como eles otimizam seus hiperparâmetros e não parece ter um método rigoro, moderno ou científico para realizar a Ciência de Dados (evitando overfitt, incoerências, etc). 

Portanto, observamos aí uma oportunidade de melhorar essa estratégia: adicionando novas features ao modelo, realizando um método científico mais rigoroso e moderno com base no livro "Advances in Financial Machine Learning. LOPEZ DE PRADO, Marcos" para a escolha de hiperparâmetros e fuga de overfit, e possívelmente realizando um sampleling mais complexo com Dollar Bars ou Unbalanced Dollars Bars.


## Etapas

O projeto como um todo seguirá as etapas abaixo.

- [ ] Coleta de Dados
- [ ] Análise Exploratória
- [ ] Tratamento dos Dados
- [ ] Código do Modelo
- [ ] Aplicação do Modelo
- [ ] Backtesting
- [ ] Análise dos Resultados
- [ ] Melhorias


## Cronograma

## Desafios e Problemas

Principal desafio é se isso realmente tem potencial de funcionar ou vai dar tudo errado kkkkk

Mas falando sério, as principais complicações que vejo no projeto são:

* A maior parte das criptomoedas são extremamente recentes, dificultando usar dados muito antigos
* A dimensionalidade do modelo pode estar muito grande devido a essa hipotese de adicionar os valores de todas as moedas como features.
* A complexidade de se criar um algoritmo de LSTM vai ser enorme. Principalmente porque é possível que algumas partes nós teremos que implementar na mão, uma vez que nosso método científico é meio específico a fim de evitar overfitt e trazer resultados mais robustos
* A volatilidade ainda me é uma dúvida, não sei se o ideal seria adicionar um modelo de previsão para ela ou o que. Para contornar esse problema sugiro começarmos primeiro do mais simples.

## Hasta la vista, Cripto

Como ideia de design e personalidade do nosso "Algoritimo", sugiro que o nome dele seja **LSTMinator**. Como referência ao querido e famoso Android dos cinemas "Terminator". Além de possuir a referência/metáfora de ser um exterminador do futuro assim como nosso projeto tem a ideia de se baser no passado pra prever o futuro e todo esse blá blá blá e baboseira que parece divertido para a banca.


# 2. Dados

## Panorama Geral e Contextualização

A parte de coleta de dados consiste em coletarmos os dados (quem diria né) necessários para a aplicação do modelo. Os dados que precisamos coletar são diretamente dependentes dos atributos que iremos considerar para a função objetivo.

Desse modo, nesse capítulo será dito quais são as tabelas que a equipe de dados terá que criar e tratar para serem usadas pela equipe de código.

## Estruturas de Atributos

Como possibilidades de atributos a se considerar no modelo, temos 4 estruturas, que aqui estão enunciadas da ordem de menos complexa para mais complexa.

### Estrutura 1 - Simples

  * $w$ últimos Retornos Logaritmos da moeda a ser analisada.
  
Ou seja, nessa estrutura estamos supondo que o valor esperado do nosso Retorno Logarítmo para certo dia de uma certa moeda $m_k$ será uma função dos $w$ últimos Retornos Logaritmos dessa moeda $m$


$$
R^i_{m_k} = f(R^{i-1}_{m_k}, R^{i-2}_{m_k}, ..., R^{i-w}_{m_k}) + \epsilon
$$


Numero total de atributos =  $w$

### Estrutura 2 - Simples com cerejinha

  * $w$ últimos Retornos Logaritmos da moeda a ser analisada.
  * $w$ últimos valores de volume da moeda a ser analisada.
  * $w$ últimos valores em dólares de transações da moeda a ser analisada.
  * idade da moeda
  
Ou seja, nessa estrutura estamos supondo que o valor esperado do nosso Retorno Logarítmo para certo dia de uma certa moeda $m_k$ será uma função dos $w$ últimos Retornos Logaritmos dessa moeda $m$


$$
R^i_{m_k} = f(R^{i-1}_{m_k},..., R^{i-w}_{m_k}, V^{i-1}_{m_k}, ..., V^{i-w}_{m_k},  D^{i-1}_{m_k}, ..., D^{i-w}_{m_k}, I^{i-1}_{m_k}) + \epsilon
$$


Total de Features =  $3 w + 1$

### Estrutura 3 - Simples criativa

* $w$ últimos Retornos Logaritmos de todo um conjunto de N moedas a serem analisadas.
* Idade da moeda


$$
R^i_{m_k} = f(R^{i-1}_{m_1}, ..., R^{i-w}_{m_1}, ..., R^{i-1}_{m_k}, ..., R^{i-w}_{m_k}, ..., R^{i-1}_{m_N}, ..., R^{i-w}_{m_N}, I^{i-1}_{m_k}) + \epsilon
$$


Total de Features =  $Nw + 1$

### Estrutura 4 - Simples criativa e com cerejinha

* $w$ últimos Retornos Logaritmos de todo um conjunto de N moedas a serem analisadas.
* $w$ últimos valores de volume da moeda a ser analisada.
* $w$ últimos valores em dólares de transações da moeda a ser analisada.
* Idade da moeda


$$
R^i_{m_k} = f(R^{i-1}_{m_1}, ..., R^{i-w}_{m_1}, ..., R^{i-1}_{m_k}, ..., R^{i-w}_{m_k}, ..., R^{i-1}_{m_N}, ..., R^{i-w}_{m_N}, \\
V^{i-1}_{m_k}, ..., V^{i-w}_{m_k},  D^{i-1}_{m_k}, ..., D^{i-w}_{m_k}, I^{i-1}_{m_k}) + \epsilon
$$


Total de Features =  $(N+2)w + 1$

### Estrutura 4 -  Alternativa

  * Média dos $w$ últimos Retornos Logaritmos de todo um conjunto de N moedas a serem analisadas.
  * Desvio padrão dos $w$ últimos Retornos Logaritmos de todo um conjunto de N moedas a serem analisadas.
  * Média dos $w$ últimos valores de volume de todo um conjunto de N moedas a serem analisadas.
  * Desvio padrão dos $w$ últimos valores de volume de todo um conjunto de N moedas a serem analisadas.
  * Média dos $w$ últimos valores em dólares de transações de todo um conjunto de N moedas a serem analisadas.
  * Desvio Padrão dos $w$ últimos valores em dólares de transações de todo um conjunto de N moedas a serem analisadas.
  * Média do Market Share dessa moeda dos ultimos $w$ dias
  * Desvio Padrão do Market Share dessa moeda dos ultimos $w$ dias
  * Trend do Market Share dessa moeda dos ultimos $w$ dias
  * Idade da moeda

 
$$
R^i_{m_k} = f(\mu^{R}_{m_1}, \sigma^{R}_{m_1}, ..., \mu^{R}_{m_N},\sigma^{R}_{m_N}, ..., \mu^{V}_{m_1}, \sigma^{V}_{m_1},..., \mu^{V}_{m_N}, \sigma^{V}_{m_N},\\  \mu^{D}_{m_1}, \sigma^{D}_{m_1},..., \mu^{D}_{m_N}, \sigma^{D}_{m_N},\\
 \mu_{ms}, \sigma_{ms}, \Delta_{ms}, I^{i-1}_{m_k} ) + \epsilon
$$


Total de Features =  $6N + 4$

### Estrutura 5 - All In

* $w$ últimos Retornos Logaritmos de todo um conjunto de N moedas a serem analisadas.
* $w$ últimos valores de volume de todo um conjunto de N moedas a serem analisadas.
* $w$ últimos valores em dólares de transações de todo um conjunto de N moedas a serem analisadas.
* Idade da moeda
* Média do Market Share dessa moeda dos ultimos $w$ dias
* Desvio Padrão do Market Share dessa moeda dos ultimos $w$ dias
* Trend do Market Share dessa moeda dos ultimos $w$ dias


$$
R^i_{m_k} = f(R^{i-1}_{m_1}, ..., R^{i-w}_{m_1}, ..., R^{i-1}_{m_N}, ..., R^{i-w}_{m_N},
V^{i-1}_{m_1}, ..., V^{i-w}_{m_1},..., V^{i-1}_{m_N}, ..., V^{i-w}_{m_N},\\
D^{i-1}_{m_1}, ..., D^{i-w}_{m_1}, ..., D^{i-1}_{m_N}, ..., D^{i-w}_{m_N}, I^{i-1}_{m_k}, \mu_{ms}, \sigma_{ms}, \Delta_{ms} ) + \epsilon
$$


Total de Features =  $3Nw + 4$



















# Introdução

1. Queremos fazer um projeto na área de criptomoedas
    1. Vantagens: 
        * Ganhamos pontos por criatividade; 
        * Mercado com alto potencial de ganho; 
        * Papers na área que apresentam bons resultados;
    2. Desvantagens: 
        * Dificuldade em fazer backtest;
            * "Todas" estratégias geram retornos positivos;
            * Pouquíssima base de dados: boa parte das moedas começaram a existir em 2014 pra frente;
        * Alta volatilidade, tornando previsões imprecisas;
        * Poucos papers na área em comparação com outros ativos;
2. Projeto atualmente está definido em 3 fases
    1. Forecasting do valor esperado de uma moeda e do seu risco;
    2. Montagem de portfólio com várias moedas que otimize a utilidade da estratégia;
    3. BackTest da estratégia para avaliar os resultados
> Na verdade seria interessante que ambas as duas primeiras etapas por si só tivessem seu próprio backtest
> uma vez que para cada uma dessas fases haverá uma modelagem própria que deve ser avaliada.
> 

# Etapa 1

### 1. **Introdução**

Nesta etapa, nosso objetivo é estimar o *Retorno Esperado*, o *Risco Esperado* de uma determinada criptomoeda e a Covariância entre diferentes Criptomoedas em um momento futuro $t$, utilizando as informações disponíveis até o instante $t-1$.

## 2. **Estratégia 1.1**
Como primeira estratégia, adotamos uma abordagem simples onde o retorno esperado do ativo é calculado como a média dos retornos observados em um intervalo de tempo anterior, definido como $[t-p, t-1]$.

Essa estratégia baseia-se na *hipótese* de que o **retorno do ativo segue uma distribuição aproximadamente constante ao longo do tempo.** Portanto, o valor esperado dessa distribuição pode ser estimado pela média dos retornos passados.

$$
E[R_t] = \frac{1}{N}\sum_{i= t-N}^{t-1} R_i = \overline{R}
$$

Analogamente, a variância do retorno (que representa o risco) é dada por:

$$
\sigma_t^2 = \frac{1}{N-1}\sum_{i= t-N}^{t-1} (R_i - \overline{R})^2
$$

$$
Cov(R_x, R_y) = \frac{1}{N-1} \sum_{i=t-N}^{t-1} (R^y_i - m_y)(R^x_i - m_x)
$$

Importante lembrar que esse retorno é o logarítmico, embora ele seja muito próximo do retorno percentual para valores pequenos.

- **Retorno Percentual**: $r_{t} = \frac{X_t - X_{t-1}}{X_{t-1}}$
- **Retorno Logarítmico**: $R_t = \ln(r_t + 1)$

Onde $X_t$ representa o valor do ativo no instante $t$

Desse modo, temos o seguinte roteiro: Para determinada moeda, em determinado instante t, realizamos a média dos últimos N instantes. O valor esperado será igual a essa média.
Além disso, calculamos a variância amostral desses q ultimos instantes, este será o valor esperado do risco.

> Peceba que surge um hiperparâmetro - Qual a quantidade de instantes N que eu devo contabilizar na média?

Embora uma quantidade maior eu esteja pegando teoricamente encontrando um valor mais preciso da média da distribuição temos que lembrar que a distribuição pode mudar, logo valores menores fazem com que consideremos apenas a teorica *distribuição mais recente*.

Além disso, um pouco mais discreto, temoso hiperparâmetro que representa o intevalo de tempo que pretendemos realizar o trading. Chamaremos ele de $x_{days}$

> Qual o intervalo de tempo $x_{days}$ entre nossas operações?

Para valores altos de $x_{days}$ estamos provavelmente trabalhando com volatilidades menores. Entretanto, quanto maior o valor de $x_{days}$, menor será a nossa possibilidade de treinamento e backtesting pois menor será a nossa quantidade de dados disponíveis.

A Aplicação desta estratégia foi feita [aqui](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Etapa%201/Estrat%C3%A9gia%2001)

Realizei uma otimização força bruta para encontrar os melhores valores dos hiperparâmetros acima. Como métrica eu considerei a tupla de $(N,x_{days})$ que acarretasse em menor média de Erro Quadrático Médio (MSE) nas 20 moedas selecionadas, em todo o período de existência de cada uma.

> Moedas selecionadas: *Bitcoin, Ethereum, XRP (Ripple), Litecoin, Bitcoin Cash, Cardano, Polkadot, Chainlink, Dogecoin, Polygon, Uniswap, Solana, TRON, Stellar Lumens, Avalanche, Shiba Inu, Filecoin, Algorand, VeChain, Tezos, EOS.*

Resultado da Otimização de parâmetros - 

**Tabela 1: 10 Valores de  $(N,x_{days})$ com menores MSE entre as principais 20 criptomoedas**
| Média MSE  | 0.014484 | 0.014487 | 0.014487 | 0.014487 | 0.014488 | 0.014489 | 0.014490 | 0.014491 | 0.014494 | 0.014494 |
|------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| N          | 62       | 59       | 69       | 60       | 61       | 70       | 64       | 58       | 63       | 71       |
| x_days     | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |

Percebe-se que para essa etratégia, o período mais eficaz de trading foi de 1 dia para cada operação. Além disso, considerar em torno de 1 mês para realizar a média dos retornos mostrou-se mais eficaz.

# Etapa 2
### **Introdução**

O Objetivo da etapa 2 consiste, com base nos valores esperados calculados pela etapa 1, alocar um determinado percentual de um capital C em um conjunto de n possíveis ativos financeiros de risco de modo a maximizar  a relação Retorno_ajustado/Risco.

## **Estratégia 2.1**
A estratégia 2.1 consiste em aplicar um algoritmo genético para encontrar a melhor alocação perncentual de capital num conjunto de criptomoedas determinado
Para a aplicação desta estratégia, precisamos de: valor esperado do retorno do ativo e matriz de covariânvia entre os ativos.

A estratégia está sendo implementada [aqui](https://github.com/JoaoDelVecchio/Quantamental/tree/main/Etapa%202/Estrat%C3%A9gia%202.1).

Essa estratégia a alocação de portfolio financeiro é baseada na Teoria de Portfólio  Markowitz (Mean-Variance Portfolio Theory)  e assim tem como base o cálculo de retornos e covariâncias destes retornos. 

Lembrando:
- **Retorno Percentual**: $r_{t} = \frac{X_t - X_{t-1}}{X_{t-1}}$
- **Retorno Logarítmico**: $R_t = \ln(r_t + 1)$
- **Valor Esperado do Retorno Percentual:=** $m$
- **Valor Esperado do Retorno Logartimico:=** $\mu$
- **Risco Percentual:=** $s^2$
- **Risco Logartimico:=** $\sigma^2$

Relação entre ambos: $m = e^{\mu} - 1$ ,     $s^2 = e^{2\mu}(e^{\sigma^2} - 1)$

* Por motivos práticos, para a etapa de otimização de portfólio vamos utilizar os valores percentuais.
* Além disso, vamos considerar inicialmente o valor esperado do retorno anual de cada ativo (Podemos alterar isso depois)

> Essa alteração deve ser feita em conjunto com a otimização de parâmetros da *Etapa 1*. Observe que inicialmente consideramos $x_{days} = 252$ e $N = maximo$.

Assim, para encontrarmos o valor esperado de cada ativo:

$$
E[R_{t}] = \mu_t = 252 (\frac{1}{N} \sum_{i = t-N}^{t-1}{R_i}) = 252 \overline{R}
$$

$$
m_t = e^{\mu_t} - 1 = e^{252 \overline{R}} - 1 
$$

$$
m_t = e^{\frac{252}{N} \sum{R_i}} - 1 
$$

$$
m_t = e^{\frac{252}{N} \sum{ln(1 + r_i)}} - 1
$$

$$
m_t = e^{\sum{ln(1 + r_i)^{\frac{252}{N}}}} - 1 = \prod{(1+r_i)^{\frac{252}{N}}} - 1
$$

$$
m_t = \prod_{i = t-N}^{t-1}{(1+r_i)^{\frac{252}{N}}} - 1
$$

Dessa forma, será este o valor esperado para uma certo criptomoeada que iremos utilizar na implementação.

Além disso, a Matriz de Covariância Cov é fácil de se calcular:

$$
Cov(r_x, r_y) = \frac{1}{N-1} \sum_{i=t-N}^{t-1} (r^y_i - m_y)(r^x_i - m_x)
$$
> Questionamento: Porque é assim?

> Note que estamos a todo momento dependendo desse hiperparâmetro N, assim como na etapa 1

Vamos considerar o vetor x como sendo o vetor contendo os pesos de cada ação no portifólio (porcentagem do capital total investido nesta).
Tome que a quantidade de criptos utilizada no portifólio é 20.

$$
X = [w_1,w_2,...,w_i,..., w_{20}]^T
$$

O vetor m contem o retorno médio percentual anual esperado de cada cripto

$$
M = [m_1,..m_i,...,m_{20}]^T
$$

Temos que o valor esperado do retorno percentual do portifólio será:

$$
E[r_P] = E[\sum_{i=1}^{20}{w_i r_i}] = \sum_{i=1}^{20}{w_i m_i} = \langle X, M \rangle
$$

Além disso, o risco desse nosso portifólio é:

$$
s_P = \sqrt{\sum{w_i^2 s_i^2}  +\sum{\sum_{i \neq j}{2 w_i w_j Cov_{i,j}}}} = \sqrt{X^T * Cov * X}
$$


# Etapa 3
