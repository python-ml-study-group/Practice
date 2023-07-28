import yfinance as yf

def get_data(stock: str, startdate: str, enddate: str):
    df = yf.download(stock, start=startdate, end=enddate)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    return df
    
def cleanup(df):
    df.dropna(subset=['MA_20', 'UBB', 'LBB'], inplace=True)
    df = df.round(2)
    return df

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
    df['ST_up'] = df['MA_20'] > df['MA_20'].shift(1)
    df['ST_down'] = df['MA_20'] < df['MA_20'].shift(1)

    # check if the the price has touched the upper bollinger band in the last 5 days
    df['Touched_UBB'] = df['High'].rolling(5).max() >= df['UBB']



def test():
    df = get_data('TSLA', '2023-01-01', '2023-12-31')
    enrich(df)
    df = cleanup(df)
    add_features(df)
    print(df.head())

if __name__ == '__main__':
    test()