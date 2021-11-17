import pymysql
import pandas as pd


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='12345678', db='tickerDay')
    return conn


def query(sqlQuery, args):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sqlQuery, args)
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results


if __name__ == '__main__':
    sqlQuery = 'SELECT  * FROM AAPL_day;'
    data = query(sqlQuery, None)
    df = pd.DataFrame(data)
    df.columns = ['date', 'close', 'high', 'low', 'open', 'volume', 'adjClose', 'adjHigh'
        , 'adjLow', 'adjOpen', 'adjVolume', 'divCash', 'splitFactor']


df.to_csv('AAPL_day.csv')
