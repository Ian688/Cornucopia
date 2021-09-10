import pandas as pd
from tiingo import TiingoClient
import os
os.environ["TIINGO_API_KEY"] = '9355858416d97287baf3deffadec823b1d0e060b'
client = TiingoClient()

# 'adjLow', 'adjHigh', 'adjClose', 'splitFactor', 'adjVolume'
# 'volume', 'low','open', 'close', 'adjOpen', 'divCash', 'high'
index = 'adjClose'

data = client.get_dataframe(['GOOGL', 'AAPL']
                            ,frequency='daily'
                            ,metric_name=index
                            ,startDate='2017-01-01'
                            ,endDate='2017-03-31')
df = pd.DataFrame(data)
print(data)





