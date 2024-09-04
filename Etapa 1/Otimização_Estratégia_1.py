import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
vator_otimo = [0, 0, 0]
max = -float('inf')
symbol = 'BTC-USD'
start_date = '2010-01-01'
end_date = '2022-12-31'
data_BTC = yf.download(symbol, start=start_date, end=end_date)
k=0
for N in range(2, 100):
    for x_days in range(1, 30):
        for SR in np.arange(0, 1, 0.001):
            resample_period = f'{x_days}D'
            
            data_BTC= data_BTC.resample(resample_period).agg({'Open': 'first', 'Close': 'last'})
            data_BTC['Log Return'] = (data_BTC['Close'] / data_BTC['Open']).apply(math.log)
            data_BTC['Percentual Return'] = ((data_BTC['Close'] - data_BTC['Open'])/data_BTC['Open'])
            
            data_BTC['Predicted Value'] = data_BTC['Log Return'].rolling(window=N).mean().shift(1)
            data_BTC['Predicted Risk'] = data_BTC['Log Return'].rolling(window=N).std().shift(1)
            data_BTC = data_BTC.dropna()
            data_BTC['Sharpe Ratio'] = data_BTC['Predicted Value'] / data_BTC['Predicted Risk']
            data_BTC['Signal'] =  np.where(data_BTC['Sharpe Ratio'] > SR, 1, 0)
            data_BTC['Profit'] =  data_BTC['Percentual Return'] * data_BTC['Signal']
            
            if data_BTC['Profit'].sum() > max:
                max = data_BTC['Profit'].sum()
                vetor_otimo = [N, x_days, SR]
            
            k = k + 1
            print("---------------------")
            print("iteração:", k)
            print("Valor máximo atual: ", max, "\nVetor desse valor máximo: ", vetor_otimo)

print("Soma ótima:\n", max, "\nValores de N, x_days, SR ótimos:\nN, X_days, SR = ", vetor_otimo)
