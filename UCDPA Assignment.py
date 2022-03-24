import requests
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=58AOTKBLQKCCPH1'
r = requests.get(url)
data = r.json()

import pandas as pd
filename = r'C:\Users\walsh\Downloads\weekly_adjusted_IBM.csv'
df = pd.read_csv(r'C:\Users\walsh\Downloads\weekly_adjusted_IBM.csv')
df.fillna(method='bfill')
df2 = df.loc[:, 'timestamp': 'open']. sort_values('open', ascending=False)
df2.rename(columns= {'timestamp': 'timestamp', 'open': 'open_IBM'}, inplace=True)
df2['year'] = pd.DatetimeIndex(df2['timestamp']).year
df2['month'] = pd.DatetimeIndex(df2['timestamp']).month

filename_2 = r'C:\Users\walsh\Downloads\HPE.csv'
df3 = pd.read_csv(r'C:\Users\walsh\Downloads\HPE.csv')
df3.fillna(method='bfill')
df4 = df3.loc[:, 'Date': 'Open']. sort_values('Open', ascending=False)
df4.rename(columns= {'Date': 'timestamp', 'Open': 'open_HPE'}, inplace=True)
df4['year'] = pd.DatetimeIndex(df4['timestamp']).year
df4['month'] = pd.DatetimeIndex(df4['timestamp']).month

results= pd.merge(df2, df4, on=['year', 'month'])

import numpy as np
average_open_IBM = np.mean(results['open_IBM'])
average_open_HPE = np.mean(results['open_HPE'])
openIBM= results['open_IBM'].values

results.describe()

grouped_results = results.groupby(['open_IBM', 'open_HPE']).agg('mean')

results.set_index(keys='open_IBM', drop=True, append=False, inplace=False, verify_integrity=False)

dfs = [df,df2,df3, df4, results]
def max (dfs):
    print( dfs.max())
    return

from matplotlib import pyplot as plt
fig, ax = plt.subplots()
ax.plot(df['timestamp'] , df['adjusted close'])
plt.xlabel('Date')
ax.invert_xaxis()
plt.tick_params(axis='x', labelrotation= 90, grid_alpha=0.8, direction='in', length=10, width=0.01)
every_nth = 60
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
plt.ylabel('Stock Price')
plt.title('IBM Stock Price over Time')

import seaborn as sns
fig, ax = plt.subplots(1, 2, figsize=(10,4))
sns.histplot(data=df4, x='open_HPE', ax=ax[0])
ax[0].set_title("Histogram")
sns.boxplot(data=df4, x='open_HPE', ax=ax[1])
ax[1].set_title("Boxplot")
plt.show()








































