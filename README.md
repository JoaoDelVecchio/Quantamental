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
* [Advances in Financial Machine Learning. LOPEZ DE PRADO, Marcos]()
* [Artificial Intelligence in Finance A Python-Based Guide. Hilpisch, Yves.]()
* [Introduction to the Economics and Mathematics of Financial Markets. ZAPATERO, Fernando.]()
* [MACHINE LEARNING FOR ASSET MANAGERS. LOPEZ DE PRADO, Marcos]()
* [Statistical Analysis of Financial Data. GENTLE, James.]()
* [Analysis of Financial Time Series. RUEY S. TSAY]()
* [THE ANALYSIS OF TIME SERIES AN INTRODUCTION. Chris Chatfield.]()

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
