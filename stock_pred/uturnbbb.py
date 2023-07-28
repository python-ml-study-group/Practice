# Predict if the price takes the uturn at bollinger bottom

def add_label(df):
    # Check if the price has moved up from the lower bollinger band to cross the MA_20,
    #    in the next 5 days
    # If yes, then label it as 1
    # If no, then label it as 0
    df['label'] = np.where((df['Close'].shift(-5) > df['MA_20'].shift(-5)) & (df['Close'] < df['LBB']), 1, 0)


def train_model (df):
    pass