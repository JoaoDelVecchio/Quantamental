Repositório do projeto para o desafio ITAU Quantamental.

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

# Etapa 1

### 1. **Introdução**

Nesta etapa, nosso objetivo é estimar o *Retorno Esperado* e o *Risco Esperado* de uma determinada criptomoeda em um momento futuro \( t \), utilizando as informações disponíveis até o instante \( t-1 \).

### 2. **Estratégia 1**
Como primeira estratégia, adotamos uma abordagem simples onde o retorno esperado do ativo é calculado como a média dos retornos observados em um intervalo de tempo anterior, definido como \([t-p, t-1]\).

Essa estratégia baseia-se na *hipótese* de que o **retorno do ativo segue uma distribuição aproximadamente constante ao longo do tempo.** Portanto, o valor esperado dessa distribuição pode ser estimado pela média dos retornos passados.

$$
E[R_t] = \frac{1}{N}\sum_{i= t-N}^{t-1} R_i = \overline{R}
$$

Analogamente, a variância do retorno (que representa o risco) é dada por:

$$
\sigma_t^2 = \frac{1}{N-1}\sum_{i= t-N}^{t-1} (R_i - \overline{R})^2
$$

Importante lembrar que esse retorno é o logarítmico, embora ele seja muito próximo do retorno percentual para valores pequenos.

- **Retorno Percentual**: $r_{t} = \frac{X_t - X_{t-1}}{X_{t-1}}$
- **Retorno Logarítmico**: $R_t = \ln(r_t + 1)$

Onde $X_t$ representa o valor do ativo no instante $t$

Desse modo, temos o seguinte roteiro: Para determinada moeda, em determinado instante t, realizamos a média dos últimos N instantes. O valor esperado será igual a essa média.
Além disso, calculamos a variância amostral desses q ultimos instantes, este será o valor esperado do risco.

> Peceba que surge um hiperparâmetro - Qual a quantidade de instantes N que eu devo contabilizar na média?

Embora uma quantidade maior eu esteja pegando teoricamente encontrando um valor mais preciso da média da distribuição temos que lembrar que a distribuição pode mudar, logo valores menores fazem com que consideremos apenas a teorica *distribuição mais recente*.

Além disso, um pouco mais discreto, temoso hiperparâmetro que representa o intevalo de tempo que pretendemos realizar o trading. Chamaremos ele de T

> Qual o intervalo de tempo T entre nossas operações?

Para valores altos de T estamos provavelmente trabalhando com volatilidades menores. Entretanto, quanto maior o valor de T, menor será a nossa possibilidade de treinamento e backtesting pois menor será a nossa quantidade de dados disponíveis.

A Aplicação desta estratégia foi feita [aqui]()


# Etapa 2

# Etapa 3
