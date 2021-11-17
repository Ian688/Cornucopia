import pymysql
import pandas as pd
from tiingo import TiingoClient
import os
from sqlalchemy import create_engine

os.environ["TIINGO_API_KEY"] = '9355858416d97287baf3deffadec823b1d0e060b'
client = TiingoClient()
engine = create_engine("mysql+pymysql://root:12345678@localhost/tickerDay?charset=utf8")

data = client.get_ticker_price('AAPL',fmt='json',
                                startDate='2010-01-01',
                                endDate='2021-09-01',
                                frequency='daily')

df = pd.DataFrame(data)
df.tail(3)

df['date'] = df['date'].map(lambda x:str(x)[0:10])
df

df.to_sql('GOOGL_day',engine,if_exists='append',index=False)


df = pd.DataFrame(data)
print(df.head(3))


engine.dispose()