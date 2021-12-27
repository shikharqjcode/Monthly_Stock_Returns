import yahoo_fin.stock_info as si
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 10)

# for-extracting-stock-data
infy = si.get_data('infy.ns', start_date='2016-03-01', end_date='2020-03-01', interval='1mo',  index_as_date=False)
sbin = si.get_data('sbin.ns', start_date='2016-03-01', end_date='2020-03-01', interval='1mo', index_as_date=False)
lt = si.get_data('lt.ns', start_date='2017-03-01', end_date='2021-03-01', interval='1mo', index_as_date=False)
itc = si.get_data('itc.ns', start_date='2017-03-01', end_date='2021-03-01', interval='1mo', index_as_date=False)

# for-storing-closing-of-the-stocks
sdf = pd.DataFrame({
                    'Date':
                    infy['date'],
                    'Infosys':
                    infy['close'],
                    'SBI':
                    sbin['close'],
                    'L&T':
                    lt['close'],
                    'ITC':
                    itc['close']
})

# allocation-per-stock = equal

# for-creating-dataframe-for-storing-returns-of-the-stocks
returns = pd.DataFrame()
returns['Date'] = sdf['Date'].dt.strftime('%b %d, %Y')
returns['Infosys'] = sdf['Infosys']/sdf['Infosys'].shift(1)-1
returns['SBI'] = sdf['SBI']/sdf['SBI'].shift(1)-1
returns['L&T'] = sdf['L&T']/sdf['L&T'].shift(1)-1
returns['ITC'] = sdf['ITC']/sdf['ITC'].shift(1)-1
returns['Portfolio'] = (returns['SBI'] + returns['Infosys']+ returns['L&T']+ returns['ITC'])/4
returns.set_index('Date', inplace=True)
returns.replace(np.nan, 0, inplace=True)

# stocks-data
monstd = (returns.std()*100).round(2)
monavgmean = (returns.mean()*100).round(2)
nos_mons = returns.shape[0]
mongeomean = ((np.prod(1+returns)**(1/nos_mons)-1)*100).round(2)
annstd = (returns.std()*np.sqrt(12)*100).round(2)
annavgmean = (returns.mean()*12*100).round(2)
anngeomean = ((np.prod(1+returns)**(12/nos_mons)-1)*100).round(2)
corr = returns.corr()
covar = returns.cov()
var = returns.var()
