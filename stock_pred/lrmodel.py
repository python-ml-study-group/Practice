import data
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
def train_model():
    print("Training Linear regression model")
    # Load the data
    df = data.prepare_df()
    #df = df[['Open', 'High', 'Low', 'Close', 'Volume', 'MA_20', 'UBB', 'LBB', 'label']]

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
    x_train, x_test, y_train, y_test = train_test_split(df[['st_up', 'st_down', 'prev_ubb_10', 'prev_lbb_10']], df['touched_ma20'], test_size=0.2)

    # Train the model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Save the model
    pickle.dump(model, open('lrmodel', 'wb'))
    #model.save('lrmodel')

    # Test the model
    y_pred = model.predict(x_test)


    # Plot the results
    df_pred = pd.DataFrame(y_pred)
    df_pred['pred'] = df_pred[[0]]
    df_pred['Index'] = df_pred.index
    df_test = y_test.to_frame()
    df_test.reset_index(inplace=True)
    df_test['Index'] = df_test.index

    sns.lineplot(data=df_pred, x='Index',  y="pred", label="Predicted")
    sns.lineplot(data=df_test, x="Index", y="touched_ma20", label="actual", color="red")

    plt.show()
    y_pred = np.where(y_pred > 0.5, 1, 0)

    # Evaluate the model
    #accuracy = model.evaluate(x_test, y_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: ", accuracy)
    # Prepare the model for the use

def get_pred (vals): 
    model = pickle.load(open('lrmodel', 'rb'))
    #model = tf.keras.models.load_model('lrmodel')
    y_pred = model.predict(vals)
    return y_pred

if __name__ == '__main__':
    train_model()
    # test the model with some values
    val1 = np.array([[0, 1, 1, 0]])
    pred = get_pred(val1)
    print ("pred: ", pred)


