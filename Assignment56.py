# Fraudulent Transaction Detection
# Machine Learning Assignment

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

data = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("Dataset:")
print(data.head())


# --------------------------------------------------
# 2. Convert Categorical Data
# --------------------------------------------------

le = LabelEncoder()

data["DeviceType"] = le.fit_transform(data["DeviceType"])


# --------------------------------------------------
# 3. Separate Input and Target
# --------------------------------------------------

X = data.drop("Fraud", axis=1)
Y = data["Fraud"]


# --------------------------------------------------
# 4. Split Dataset
# --------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42,
    stratify=Y
)


# --------------------------------------------------
# 5. Create Models
# --------------------------------------------------

DT = DecisionTreeClassifier(
    random_state=42,
    max_depth=5
)

Bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=50,
    random_state=42
)

RF = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

AdaBoost = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)


# Voting Classifier
Voting = VotingClassifier(
    estimators=[
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("rf", RandomForestClassifier(n_estimators=100, random_state=42)),
        ("ada", AdaBoostClassifier(n_estimators=100, random_state=42))
    ],
    voting="hard"
)


# --------------------------------------------------
# 6. Store Models
# --------------------------------------------------

models = {
    "Decision Tree": DT,
    "Bagging": Bagging,
    "Random Forest": RF,
    "AdaBoost": AdaBoost,
    "Voting": Voting
}


# --------------------------------------------------
# 7. Train and Evaluate
# --------------------------------------------------

results = []

for name, model in models.items():

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    # Train
    model.fit(X_train, Y_train)

    # Prediction
    Y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(Y_test, Y_pred)
    precision = precision_score(Y_test, Y_pred, zero_division=0)
    recall = recall_score(Y_test, Y_pred, zero_division=0)
    f1 = f1_score(Y_test, Y_pred, zero_division=0)

    # Display
    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))

    print("\nConfusion Matrix:")
    print(confusion_matrix(Y_test, Y_pred))

    # Store results
    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])


# --------------------------------------------------
# 8. Final Comparison
# --------------------------------------------------

comparison = pd.DataFrame(
    results,
    columns=[
        "Algorithm",
        "Accuracy",
        "Precision",
        "Recall",
        "F1"
    ]
)

print("\n\nFINAL COMPARISON")
print("=" * 80)
print(comparison.round(4).to_string(index=False))


# --------------------------------------------------
# 9. Find Model with Highest F1 Score
# --------------------------------------------------

best_model = comparison.loc[
    comparison["F1"].idxmax(),
    "Algorithm"
]

print("\nMost suitable model based on F1 Score:")
print(best_model)