import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# --------------------------------------------------
# Step 1 : Get Data
# --------------------------------------------------

def GetData():
    print("Step 1 : Getting Data")
    Datapath =  "MarvellousInfosystems_PlayPredictor.csv"
    df = pd.read_csv(Datapath)

    print("\nDataset:")
    print(df)

    return df


# --------------------------------------------------
# Step 2 : Clean, Prepare and Manipulate Data
# --------------------------------------------------

def PrepareData(df):

    print("Step 2 : Preparing Data")

    # Create LabelEncoder objects
    wether_encoder = LabelEncoder()
    temperature_encoder = LabelEncoder()
    play_encoder = LabelEncoder()

    # Convert categorical data into numerical data
    df["Wether"] = wether_encoder.fit_transform(df["Wether"])
    df["Temperature"] = temperature_encoder.fit_transform(
        df["Temperature"]
    )
    df["Play"] = play_encoder.fit_transform(df["Play"])

    print("\nEncoded Dataset:")
    print(df)

    return df, wether_encoder, temperature_encoder, play_encoder


# --------------------------------------------------
# Step 3 : Train Data
# --------------------------------------------------

def TrainData(df):

    print("step 3 : Training Data")

    # Features
    X = df[["Wether", "Temperature"]]

    # Target
    Y = df["Play"]

    # KNN classifier
    K = 3

    model = KNeighborsClassifier(n_neighbors=K)

    # Train the model
    model.fit(X, Y)

    print("KNN model trained successfully.")
    print("K =", K)
    

    return model, X, Y


# --------------------------------------------------
# Step 4 : Test Data
# --------------------------------------------------

def TestData(model, wether_encoder, temperature_encoder, play_encoder):

    print("\nStep 4 : Testing Data")

    # Take input from user
    wether = input(
        "Enter Wether (Sunny/Overcast/Rainy): "
    )

    temperature = input(
        "Enter Temperature (Hot/Cool/Mild): "
    )

    # Convert input into numerical form
    wether_value = wether_encoder.transform([wether])[0]

    temperature_value = temperature_encoder.transform(
        [temperature]
    )[0]

    # Create input for prediction
    test_data = [[wether_value, temperature_value]]

    # Predict
    result = model.predict(test_data)

    # Convert numerical result back to Yes/No
    prediction = play_encoder.inverse_transform(result)

    print("\nPrediction:", prediction[0])

    if prediction[0] == "Yes":
        print("Result: You can PLAY.")
    else:
        print("Result: You should NOT PLAY.")


# --------------------------------------------------
# Step 5 : Calculate Accuracy
# --------------------------------------------------

def CheckAccuracy(X, Y):

    print("\nStep 5 : Calculating Accuracy")

    # Split data into training and testing data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("\nTraining records :", len(X_train))
    print("Testing records  :", len(X_test))

    # Try different values of K
    for K in range(1, 8):

        model = KNeighborsClassifier(n_neighbors=K)

        model.fit(X_train, Y_train)

        prediction = model.predict(X_test)

        accuracy = accuracy_score(Y_test, prediction)

        print(
            "K =", K,
            "Accuracy =", accuracy * 100, "%"
        )


# --------------------------------------------------
# Main Function
# --------------------------------------------------

def main():

    # Step 1
    df = GetData()

    # Step 2
    df, wether_encoder, temperature_encoder, play_encoder = \
        PrepareData(df)

    # Step 3
    model, X, Y = TrainData(df)

    # Step 4
    TestData(
        model,
        wether_encoder,
        temperature_encoder,
        play_encoder
    )

    # Step 5
    CheckAccuracy(X, Y)


# Program starts here
if __name__ == "__main__":
    main()