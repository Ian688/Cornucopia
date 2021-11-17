import pandas as pd
from tiingo import TiingoClient
import os
import matplotlib.pyplot as plt


os.environ["TIINGO_API_KEY"] = '9355858416d97287baf3deffadec823b1d0e060b'
client = TiingoClient()

# 'adjLow', 'adjHigh', 'adjClose', 'splitFactor', 'adjVolume'
# 'volume', 'low','open', 'close', 'adjOpen', 'divCash', 'high'
index = 'adjClose'
data = client.get_dataframe(['GOOGL']
                            , frequency='daily'
                            , metric_name='close'
                            , startDate='2000-01-01'
                            , endDate='2005-01-01')
data['date'] = data.index.map(lambda x: pd.to_datetime(str(x)[:11]))
df = data.fillna(0)
df.index = df['date']
# print(data)
print(df)
print(df.shape[0])
print(df.iloc[:,0])

fig, ax = plt.subplots()
ax.plot(data['date'], data['GOOGL'])
plt.show()


# ax = []
# ay = []
# plt.ion()
# for i in range(df.shape[0]):
#     ax.append(df.index[i])
#     ay.append(df.iloc[:, 0][i])
#     plt.clf()
#     plt.plot(ax, ay)
#     plt.pause(0.06)
#     plt.ioff()
