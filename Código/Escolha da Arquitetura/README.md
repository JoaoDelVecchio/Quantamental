
# Catalogar Arquiteturas e verificar quais tem melhor desempenho

INTERVALO A SER ANALIZADO:
2017-06-01 até 2019-10-31
881 dias no total


Criptomoedas a ser analizadas: LTC e BTC

Métricas de desempenho: 

- Precisão (quantas são verdadeiras daquelas categorizadas como verdadeiras)
- Mean Absolute Error
- Acurácia (quantas eu acertei a categoria)
- Precisão para os 25% maiores

Para os dados analisados das arquiteturas, tinhamos 54.029512% como sendo subidas para BTC e 47.2190% sendo subidas para LTC.

## Baseline

Considerar o próximo retorno como a média dos ultimos 14 retornos

## Arquitetura SubZero

*Arquitetura que eu usei pra produzir os primeiros resultados*

LSTM, 1 || Dropout 0.2 || Dense 1 || Otimizador Adam

- 1 Features
- 50 epochs

w = 50
W = 80

## Arquitetura 0

*Arquitetura SubZero mas com 2 Features em vez de 1*

LSTM, 1 || Dropout 0.2 || Dense 1 || Otimizador Adam

- 2 Features
- 50 epochs

w = 50
W = 80

## Arquitetura 0.5

*Arquitetura SubZero mas com 32 neurônios em vez de 1 na camada LSTM e também com os valores de w e W diferentes e otimizador RMSProp e condição de parada*

LSTM, 32 || Dropout 0.3 || Dense 1 || Otimizador RMSProp 5e-3

- 1 Feature
- 300 epochs com condição de parada

w = 14
W = 250

Para BTC:

    - Precisão = 0.558935
    - MAE = 0.031253
    - Acurácia = 0.497872
    - Precisão_25 = 0.527473

Para LTC:

    - Precisão = 0.471816
    - MAE = 0.043606
    - Acurácia = 0.474540
    - Precisão_25 = 0.500000

Média: 

    - Pre_media = 0.5153758225707867
    - Acc_media = 0.4862059
    - MAE_media = 0.03742927
    - Precisao_25_media = 0.5137362

## Arquitetura 0.8

*Arquitetura 0.5 mas com duas Features em vez de apenas uma*

LSTM, 32 || Dropout 0.3 || Dense 1 || Otimizador RMSProp 5e-3

- 2 Feature
- 300 epochs com condição de parada

w = 14
W = 250

Para BTC:

    - Precisão = 0.527410    
    - MAE = 0.031710
    - Acurácia = 0.445697    
    - Precisão_25 = 0.528000

Para LTC:

    - Precisão = 0.494005
    - MAE = 0.043313 
    - Acurácia = 0.548272
    - Precisão_25 = 0.484472
  
Média: 

    - Pre_media = 0.510707
    - Acc_media = 0.496984
    - MAE_media = 0.037511
    - Precisao_25_media = 0.5062360

## Arquitetura 1

*Arquitetura mais complexa, com duas camadas lstm e una batch normalization. Além disso temos 2 atributos*

LSTM, 64|| Drop 0.3 || Batch Norm || LSTM, 32 || Drop 0.3 || Dense 1 || Otimizador RMSProp 1e-5

- 2 Atributos, ROI e ROI_BTC
- 300 epochs +  metodo de parada

w = 14
W = 250

## Arquitetura 1.5

*Arquitetura 1 mas com apenas 1 atributo*

LSTM, 64 || Drop 0.3 || Batch Norm || LSTM, 32 || Drop 0.3 || Dense 1 || Otimizador RMSProp 1e-5

- 1 Atributo
- 300 epochs +  metodo de parada

w = 14
W = 250
  
Para BTC:

    - Precisão = 
    - MAE = 
    - Acurácia = 
    - Precisão_25 = 

Para LTC:

    - Precisão =
    - MAE =
    - Acurácia = 
    - Precisão_25 = 

Média: 

    - Pre_media =
    - Acc_media = 
    - MAE_media = 
    - Precisao_25_media =
  

## Arquitetura 2

CNN 15 || Pooling Layer 2 ||  LSTM 50 || Batch Norm || dropout 0.5 || Dense 128 || Batch Norm || Drop 0.2 || Dense 1 || Otimizador RMSProp 1e-3

- 2 Atributos, ROI e ROI_BTC
- 300 epochs +  metodo de parada

w = 30
W = 250
  
Para BTC:

    - Precisão = 
    - MAE = 
    - Acurácia = 
    - Precisão_25 = 

Para LTC:

    - Precisão =
    - MAE =
    - Acurácia = 
    - Precisão_25 = 

Média: 

    - Pre_media =
    - Acc_media = 
    - MAE_media = 
    - Precisao_25_media =


