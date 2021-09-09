import pandas as pd
from tiingo import TiingoClient
import os
os.environ["TIINGO_API_KEY"] = '9355858416d97287baf3deffadec823b1d0e060b'
client = TiingoClient()

data = client.get_ticker_price("AAPL",
                               fmt='json',
                               startDate='2021-08-01',
                               endDate='2021-09-08',
                               frequency='daily')

df = pd.DataFrame(data)

print(df.head(3))