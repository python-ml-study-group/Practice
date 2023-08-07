import yfinance as yf

def get_data(stock: str, startdate: str, enddate: str):
    df = yf.download(stock, start=startdate, end=enddate)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    return df
    
def cleanup(df):
    df.dropna(subset=['MA_20', 'UBB', 'LBB'], inplace=True)
    df = df.round(2)
    return df

def test(df):
    pass

def enrich(df):
    # Add moving average
    df['MA_20'] = df['Close'].rolling(20).mean()
    df['MA_200'] = df['Close'].rolling(200).mean()

    # Add bollinger bands high, low
    df['UBB'] = df['MA_20'] + 2 * df['Close'].rolling(20).std()
    df['LBB'] = df['MA_20'] - 2 * df['Close'].rolling(20).std()

def add_features (  df):
    # Check if short term is up
    # Check if short term is down
    # Check if current value of  MA_20 is more than its prev value 
    df['st_up'] = df['MA_20'] > df['MA_20'].shift(1)
    df['st_down'] = df['MA_20'] < df['MA_20'].shift(1)

    # Check if the price has touched the upper bollinger band in the last 10 days
    df['prev_ubb_10'] = df['High'].rolling(10).max() >= df['UBB']
    # Check if the price has touched the lower bollinger band in the last 10 days
    df['prev_lbb_10'] = df['Low'].rolling(10).min() <= df['LBB']
    
    # check if the the price has touched the upper bollinger band in the next 5 days
    df['next_ubb_5'] = df['High'].shift(-5).rolling(5).max() >= df['UBB'].shift(-5)
    # check if the the price has touched the lower bollinger band in the next 5 days
    df['next_lbb_5'] = df['Low'].shift(-5).rolling(5).min() <= df['LBB'].shift(-5)



    print (df)


def prepare_df():
    df = get_data('TSLA', '2022-08-01', '2023-12-31')
    enrich(df)

    df = cleanup(df)
    add_features(df)
    return df
    print(df.head())

if __name__ == '__main__':
    prepare_df()