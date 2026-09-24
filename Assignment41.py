import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# --------------------------------------------------
# Border
# --------------------------------------------------

Border = "-" * 60

print(Border)
print("WINE CLASSIFICATION ML")
print(Border)


# ==================================================
# Step 1 : Get Data
# ==================================================


print(Border)
print("Step 1 : Get Data")
print(Border)


Datapath = "WinePredictor.csv"
df = pd.read_csv(Datapath)

print(df.head())
print("First 5 Records :")

print(df.tail())
print("Last 5 Records :")

print(df.shape)
print("Dataset Shape:")

print(df.columns)
print("Column Names:")

# ==================================================
# Step 2 : Clean, Prepare and Manipulate Data
# ==================================================

print("\n" + Border)
print("Step 2 : Clean, Prepare and Manipulate Data")
print(Border)

# Check missing values
print(df.isnull().sum())

print(" Check missing values :")

# Separate Independent and Dependent variables

# Independent Variables

X = df[[
    "Alcohol",
    "Malic acid",
    "Ash",
    "Alcalinity of ash",
    "Magnesium",
    "Total phenols",
    "Flavanoids",
    "Nonflavanoid phenols",
    "Proanthocyanins",
    "Color intensity",
    "Hue",
    "OD280/OD315 of diluted wines",
    "Proline"
]]

# Dependent Variables 

Y = df["Class"]

print("Independent Variables")
print(X.head())

print("Dependent Variables ")
print(Y.head())


# ==================================================
# Step 3 : Train Data
# ==================================================

print( Border)
print("Step 3 : Train Data")
print(Border)

X_train , X_test , Y_train ,Y_test = train_test_split( X, Y , test_size= 0.20 ,random_state= 42 )

print("lengeth of X train :", len(X_train))
print("lengeth of Y train :",len(Y_train))

#Create the Model 

model =DecisionTreeClassifier(random_state= 42)

# train the model 

model.fit(X_train,Y_train)
print("Decision Tree Model trained successfully")

# ==================================================
# Step 4 : Test Data
# ==================================================

print( Border)
print("Step 4 : Test Data")
print(Border)

Y_pred = model.predict(X_test)
print("Predicted Values:",Y_pred)


# ==================================================
# Step 5  : Calculate Accuracy
# ==================================================

print( Border)
print("Step 5 : Calculate Accuracy")
print(Border)

accuracy = accuracy_score(
    Y_test,
    Y_pred

)
print("Calculate Accuracy:",accuracy*100 , "%")


print(Border)
print("Program Completed ")
print(Border)




