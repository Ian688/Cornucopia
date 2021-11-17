import matplotlib.pyplot as plt
import seaborn as sns
from dayTickCrawl import df

fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(df.index, df['GOOGL'])
plt.plot(df.index, df['AAPL'])
plt.xlabel('date')
plt.ylabel('close',rotation=0)
plt.title('trend')
plt.legend(['googl', 'aapl'], loc='best')

plt.show()
