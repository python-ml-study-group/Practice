import data
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
def train_model():
    print("Training Linear regression model")
    # Load the data
    df = data.prepare_df(  )
    df = df[['Open', 'High', 'Low', 'Close', 'Volume', 'MA_20', 'UBB', 'LBB', 'label']]

    # Add the label "Touched MA_20 in the next 10 days"
    df['touched_ma20'] = np.where(df['Close'].shift(-10) > df['MA_20'].shift(-10), 1, 0)
    # predicted, actual

    #Draw the line graph
    if (False):
        sns.lineplot(data=df, x="Date", y="Close", label="Close")
        sns.lineplot(data=df, x="Date", y="MA_20", label="MA_20", color="red")
        sns.lineplot(data=df, x="Date", y="UBB", label="UBB", color="green")
        sns.lineplot(data=df, x="Date", y="LBB", label="LBB", color="green")


    # Split the data into train and test
    x_train, x_test, y_train, y_test = train_test_split(df[['Open', 'High', 'Low', 'Close', 'Volume']], df['touched_ma20'], test_size=0.2)

    # Train the model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Save the model
    model.save('lrmodel')

    # Test the model
    y_pred = model.predict(x_test)

    # Plot the results

    # Evaluate the model

    # Prepare the model for the use

if __name__ == '__main__':
    train_model()