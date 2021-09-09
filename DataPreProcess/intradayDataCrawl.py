import pandas as pd
import requests

headers = {'Content-Type': 'application/json'}

tgUrl = "https://api.tiingo.com/iex/"
tgToken = '9355858416d97287baf3deffadec823b1d0e060b'
ticSubName = 'aapl'
ticStartDay = '2021-08-01'
ticFreq = '5min'
ticColumns = 'open,high,low,close,volume'

url = tgUrl+ticSubName+'/prices'+'?startDate='+ticStartDay+'&resampleFreq='+ticFreq+'&columns='+ticColumns+'&token='+tgToken
requestResponse = requests.get(url, headers=headers)
data = pd.DataFrame(requestResponse.json())


