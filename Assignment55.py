# Customer Loan Approval Using Voting Classification

import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
# 1. Load Dataset
data = pd.read_csv("Customer_Loan_Approval.csv")

print("Dataset:")
print(data.head())


# 2. Check Missing Values
print(" Missing Values:")
print(data.isnull().sum())

# Fill missing numeric values
data = data.fillna(data.median(numeric_only=True))

# 3. Separate Input and Output
X = data[["Age",
          "Income",
          "CreditScore",
          "ExistingLoan",
          "EmploymentExperience",
          "LoanAmount"]]

Y= data["LoanApproved"]


# 4. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)


# 5. Logistic Regression
LR= make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

LR.fit(X_train, y_train)
LR_pred = LR.predict(X_test)

LR_acc = accuracy_score(y_test, LR_pred)


# 6. Decision Tree
DT = DecisionTreeClassifier(
    random_state=42)

DT.fit(X_train, y_train)
dt_pred = DT.predict(X_test)

DT_acc = accuracy_score(y_test, dt_pred)

# 7. KNN
KNN= make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

KNN.fit(X_train, y_train)
KNN_pred = KNN.predict(X_test)

KNN_acc = accuracy_score(y_test, KNN_pred)


# 8. Hard Voting
Hard_voting = VotingClassifier(
    estimators=[
        ("lr", LR),
        ("dt", DT),
        ("knn", KNN)
    ],
    voting="hard"
)

Hard_voting.fit(X_train, y_train)
Hard_pred = Hard_voting.predict(X_test)

Hard_acc = accuracy_score(y_test, Hard_pred)


# 9. Soft Voting
Soft_voting = VotingClassifier(
    estimators=[
        ("lr", LR),
        ("dt", DT),
        ("knn", KNN)
    ],
    voting="soft"
)

Soft_voting.fit(X_train, y_train)
Soft_pred = Soft_voting.predict(X_test)

Soft_acc = accuracy_score(y_test, Soft_pred)


# 10. Display Results
print("\n-----------------------------")
print("MODEL ACCURACY")
print("-----------------------------")

print("Logistic Regression :", round(LR_acc * 100, 2), "%")
print("Decision Tree       :", round(DT_acc * 100, 2), "%")
print("KNN                 :", round(KNN_acc * 100, 2), "%")
print("Hard Voting         :", round(Hard_acc * 100, 2), "%")
print("Soft Voting         :", round(Soft_acc * 100, 2), "%")


# 11. Final Comparison Table
result = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],
    "Accuracy": [
        round(LR_acc * 100, 2),
        round(DT_acc * 100, 2),
        round(KNN_acc * 100, 2),
        round(Hard_acc * 100, 2),
        round(Soft_acc * 100, 2)
    ]
})

print("\nFinal Result:")
print(result.to_string(index=False))