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
* The best of two worlds: Forecasting high frequency volatility for cryptocurrencies and traditional currencies with Support Vector Regression
* Intelligent forecasting with machine learning trading systems in chaotic intraday Bitcoin market
* Reinforcement Learning for Quantitative Trading
* Applying Artificial Intelligence in Cryptocurrency Markets: A Survey
* Anticipating Cryptocurrency Prices Using Machine Learning
* Trading and Arbitrage in Cryptocurrency Markets
* AUTOMATED CRYPTOCURRENCIES PRICES PREDICTION USING MACHINE LEARNING
* Cryptocurrency Trading Using Machine Learning
* A deep Q-learning portfolio management framework for the cryptocurrency market
* EXTREME CORRELATION IN CRYPTOCURRENCY MARKETS
* Market Sentiment and an Overnight Anomaly
* Seasonality, Trend-following, and Mean reversion in Bitcoin
* Cryptocurrency trading: a comprehensive survey

### **Livros**
* Advances in Financial Machine Learning. LOPEZ DE PRADO, Marcos
* Artificial Intelligence in Finance A Python-Based Guide. Hilpisch, Yves.
* Introduction to the Economics and Mathematics of Financial Markets. ZAPATERO, Fernando.
* MACHINE LEARNING FOR ASSET MANAGERS. LOPEZ DE PRADO, Marcos
* Statistical Analysis of Financial Data. GENTLE, James.
* Analysis of Financial Time Series. RUEY S. TSAY
* THE ANALYSIS OF TIME SERIES AN INTRODUCTION. Chris Chatfield.

### Sites
* [Awesome Systematic Trading Repository](https://github.com/paperswithbacktest/awesome-systematic-trading.git)

# Etapa 1

1. **Introdução**
   
    A etapa 1 consiste em estimar o *Retorno Esperado* e o *Risco Esperado* de certa criptocurrency em determinado tempo $t$ utilizando as informações disponíveis em $t-1$
    * Como primeira estratégia, e também acredito eu que mais simples, temos que o retorno esperado do ativo será igual a média do retorno deste ativo em determinado intervalo de tempo $[t-p, t-1]$
        * Essa estratégia se baseia no conceito que o retorno do ativo segue uma distribuição aproximadamente constante ao longo do tempo. Logo o valor esperado dessa distribuição tende à média dos valores de nossa população, i.e. $E[R_t] = \frac{1}{N}\sum_{i= t-N}^{t-1}(R_i) = \overline{R}$
        * De modo análogo temos que $\sigma_t^2 = \frac{1}{N-1}\sum_{i= t-N}^{t-1}(R_i - \overline{R})^2$

# Etapa 2

# Etapa 3
