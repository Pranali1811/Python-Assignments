# Loan Default Prediction using Multi-Layer Perceptron

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

data = pd.read_csv("Loan_Default.csv")

print("Dataset:")
print(data.head())

# --------------------------------------------------
# 2. Exploratory Analysis
# --------------------------------------------------

print("\nShape:")
print(data.shape)

print("\nColumns:")
print(data.columns)

print("\nData Types:")
print(data.dtypes)

print("\nStatistics:")
print(data.describe())

# --------------------------------------------------
# 3. Check Missing Values
# --------------------------------------------------

print("\nMissing Values:")
print(data.isnull().sum())

# Fill missing numerical values
numeric_columns = data.select_dtypes(
    include="number"
).columns

data[numeric_columns] = data[numeric_columns].fillna(
    data[numeric_columns].median()
)

# Fill missing categorical values
categorical_columns = data.select_dtypes(
    include="object"
).columns

for column in categorical_columns:
    data[column] = data[column].fillna(
        data[column].mode()[0]
    )

# --------------------------------------------------
# 4. Check Target Balance
# --------------------------------------------------

print("\nDefault Class Distribution:")
print(data["Default"].value_counts())

print("\nDefault Percentage:")
print(data["Default"].value_counts(normalize=True) * 100)

# --------------------------------------------------
# 5. Encode Categorical Variables
# --------------------------------------------------

print("\nCategorical Features:")
print(data.select_dtypes(include="object").columns)

# --------------------------------------------------
# 6. Separate X and y
# --------------------------------------------------

X = data.drop("Default", axis=1)

y = data["Default"]

# --------------------------------------------------
# 7. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# --------------------------------------------------
# 8. Explain Stratified Sampling
# --------------------------------------------------

print("\nStratified sampling keeps approximately")
print("the same class proportion in train and test data.")

# --------------------------------------------------
# 9. Feature Scaling and Encoding
# --------------------------------------------------

numeric_features = X.select_dtypes(
    include="number"
).columns

categorical_features = X.select_dtypes(
    include="object"
).columns

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numeric_features
        ),
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False
            ),
            categorical_features
        )
    ]
)

# --------------------------------------------------
# 10. Create MLPClassifier
# --------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

# Create complete pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

# --------------------------------------------------
# 11. Train Model
# --------------------------------------------------

pipeline.fit(X_train, y_train)

print("\nModel Training Completed.")

# --------------------------------------------------
# 12. Accuracy
# --------------------------------------------------

train_pred = pipeline.predict(X_train)
test_pred = pipeline.predict(X_test)

train_accuracy = accuracy_score(
    y_train,
    train_pred
)

test_accuracy = accuracy_score(
    y_test,
    test_pred
)

print("\nTraining Accuracy:")
print(round(train_accuracy * 100, 2), "%")

print("\nTesting Accuracy:")
print(round(test_accuracy * 100, 2), "%")

# --------------------------------------------------
# 13. Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(
    y_test,
    test_pred
)

print("\nConfusion Matrix:")
print(cm)

# --------------------------------------------------
# 14. Classification Report
# --------------------------------------------------

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        test_pred
    )
)

# --------------------------------------------------
# 15. Precision, Recall and F1 Score
# --------------------------------------------------

precision = precision_score(
    y_test,
    test_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    test_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    test_pred,
    zero_division=0
)

print("\nPerformance:")
print("Precision :", round(precision, 3))
print("Recall    :", round(recall, 3))
print("F1 Score  :", round(f1, 3))

# --------------------------------------------------
# 16. Plot Loss Curve
# --------------------------------------------------

import matplotlib.pyplot as plt

mlp_model = pipeline.named_steps["model"]

plt.plot(mlp_model.loss_curve_)

plt.title("MLP Loss Curve")
plt.xlabel("Iteration")
plt.ylabel("Loss")

plt.show()

# --------------------------------------------------
# 17. Predict New Loan Applicant
# --------------------------------------------------

def PredictDefault(applicant_data):

    applicant = pd.DataFrame(
        [applicant_data]
    )

    prediction = pipeline.predict(
        applicant
    )[0]

    probability = pipeline.predict_proba(
        applicant
    )[0][1]

    if prediction == 1:
        result = "High default risk"
    else:
        result = "Low default risk"

    print("\nPrediction:", result)

    print(
        "Default Probability:",
        round(probability * 100, 2),
        "%"
    )

# --------------------------------------------------
# Test New Applicants
# --------------------------------------------------

applicant1 = {
    "Age": 30,
    "Income": 45000,
    "LoanAmount": 200000,
    "CreditScore": 650,
    "EmploymentYears": 5,
    "ExistingLoans": 2,
    "MonthlyDebt": 15000,
    "LoanTerm": 60,
    "PreviousDefault": "No",
    "HomeOwnership": "Own"
}

PredictDefault(applicant1)

# --------------------------------------------------
# Hyperparameter Experiment Function
# --------------------------------------------------

def TestModel(parameter_name, values):

    print("\n==============================")
    print(parameter_name)
    print("==============================")


    for value in values:

        if parameter_name == "activation":

            test_model = MLPClassifier(
                hidden_layer_sizes=(32, 16),
                activation=value,
                solver="adam",
                max_iter=1000,
                random_state=42
            )


        elif parameter_name == "hidden_layers":

            test_model = MLPClassifier(
                hidden_layer_sizes=value,
                activation="relu",
                solver="adam",
                max_iter=1000,
                random_state=42
            )


        elif parameter_name == "learning_rate":

            test_model = MLPClassifier(
                hidden_layer_sizes=(32, 16),
                activation="relu",
                solver="adam",
                learning_rate_init=value,
                max_iter=1000,
                random_state=42
            )


        test_pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("model", test_model)
        ])


        test_pipeline.fit(
            X_train,
            y_train
        )


        prediction = test_pipeline.predict(
            X_test
        )


        accuracy = accuracy_score(
            y_test,
            prediction
        )


        print(
            value,
            "→",
            round(accuracy * 100, 2),
            "%"
        )
# --------------------------------------------------
# Experiment 1: Activation Function
# --------------------------------------------------

TestModel(
    "activation",
    [
        "identity",
        "logistic",
        "tanh",
        "relu"
    ]
)

# --------------------------------------------------
# Experiment 2: Hidden Layers
# --------------------------------------------------

TestModel(
    "hidden_layers",
    [
        (10,),
        (20, 10),
        (50, 25),
        (100, 50, 25)
    ]
)

# --------------------------------------------------
# Experiment 3: Learning Rate
# --------------------------------------------------

TestModel(
    "learning_rate",
    [
        0.0001,
        0.001,
        0.01,
        0.1
    ]
)