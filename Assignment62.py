# Employee Attrition Prediction using MLPClassifier

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

data = pd.read_csv("Employee_Attrition.csv")

print("Dataset:")
print(data.head())


# --------------------------------------------------
# 2. Shape, Columns and First 5 Records
# --------------------------------------------------

print("\nShape:")
print(data.shape)

print("\nColumns:")
print(data.columns)

print("\nFirst 5 Records:")
print(data.head())


# --------------------------------------------------
# 3. Check Missing Values
# --------------------------------------------------

print("\nMissing Values:")
print(data.isnull().sum())


# Fill missing numeric values
data = data.fillna(data.median(numeric_only=True))


# --------------------------------------------------
# 4. Numerical and Categorical Features
# --------------------------------------------------

print("\nData Types:")
print(data.dtypes)


# --------------------------------------------------
# 5. Convert OverTime into Numerical Form
# --------------------------------------------------

data["OverTime"] = data["OverTime"].map({
    "Yes": 1,
    "No": 0
})


# --------------------------------------------------
# 6. Convert Attrition into 0 and 1
# --------------------------------------------------

data["Attrition"] = data["Attrition"].map({
    "Yes": 1,
    "No": 0
})


# --------------------------------------------------
# 7. Separate Independent and Dependent Variables
# --------------------------------------------------

X = data.drop("Attrition", axis=1)

y = data["Attrition"]


# --------------------------------------------------
# 8. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# 9. Feature Scaling
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# --------------------------------------------------
# 10. Create MLP with Two Hidden Layers
# --------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)


# --------------------------------------------------
# 11. Train Network
# --------------------------------------------------

model.fit(X_train_scaled, y_train)


# --------------------------------------------------
# 12. Number of Iterations
# --------------------------------------------------

print("\nNumber of iterations:")
print(model.n_iter_)


# --------------------------------------------------
# 13. Training Accuracy
# --------------------------------------------------

train_pred = model.predict(X_train_scaled)

train_accuracy = accuracy_score(
    y_train,
    train_pred
)

print("\nTraining Accuracy:")
print(round(train_accuracy * 100, 2), "%")


# --------------------------------------------------
# 14. Testing Accuracy
# --------------------------------------------------

test_pred = model.predict(X_test_scaled)

test_accuracy = accuracy_score(
    y_test,
    test_pred
)

print("\nTesting Accuracy:")
print(round(test_accuracy * 100, 2), "%")


# --------------------------------------------------
# 15. Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(
    y_test,
    test_pred
)

print("\nConfusion Matrix:")
print(cm)


# --------------------------------------------------
# 16. Plot Loss Curve
# --------------------------------------------------

plt.plot(model.loss_curve_)

plt.title("MLP Training Loss Curve")
plt.xlabel("Iteration")
plt.ylabel("Loss")

plt.show()


# --------------------------------------------------
# 17. Prediction Function
# --------------------------------------------------

def PredictAttrition(employee_data):

    # Convert employee data into DataFrame
    employee_df = pd.DataFrame(
        [employee_data]
    )

    # Convert OverTime
    employee_df["OverTime"] = employee_df[
        "OverTime"
    ].map({
        "Yes": 1,
        "No": 0
    })

    # Scale input
    employee_scaled = scaler.transform(
        employee_df
    )

    # Prediction
    prediction = model.predict(
        employee_scaled
    )[0]

    if prediction == 1:
        return "Employee is likely to leave"

    else:
        return "Employee is likely to stay"


# --------------------------------------------------
# 18. Test Five New Employees
# --------------------------------------------------

employees = [

    {
        "Age": 25,
        "MonthlyIncome": 25000,
        "YearsAtCompany": 1,
        "TotalWorkingYears": 3,
        "DistanceFromHome": 20,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 2
    },

    {
        "Age": 35,
        "MonthlyIncome": 50000,
        "YearsAtCompany": 8,
        "TotalWorkingYears": 12,
        "DistanceFromHome": 5,
        "JobSatisfaction": 4,
        "WorkLifeBalance": 4,
        "OverTime": "No",
        "NumCompaniesWorked": 1,
        "TrainingTimesLastYear": 4
    },

    {
        "Age": 29,
        "MonthlyIncome": 30000,
        "YearsAtCompany": 3,
        "TotalWorkingYears": 6,
        "DistanceFromHome": 15,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 3,
        "TrainingTimesLastYear": 2
    },

    {
        "Age": 42,
        "MonthlyIncome": 70000,
        "YearsAtCompany": 15,
        "TotalWorkingYears": 20,
        "DistanceFromHome": 4,
        "JobSatisfaction": 4,
        "WorkLifeBalance": 4,
        "OverTime": "No",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 5
    },

    {
        "Age": 31,
        "MonthlyIncome": 40000,
        "YearsAtCompany": 5,
        "TotalWorkingYears": 8,
        "DistanceFromHome": 10,
        "JobSatisfaction": 3,
        "WorkLifeBalance": 3,
        "OverTime": "Yes",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 3
    }
]


print("\nFive Employee Predictions:")
print("--------------------------------")

for i, employee in enumerate(employees, 1):

    result = PredictAttrition(employee)

    print(
        "Employee", i, ":", result
    )


# --------------------------------------------------
# 19. Overfitting and Underfitting
# --------------------------------------------------

print("\nModel Analysis:")

difference = train_accuracy - test_accuracy

if difference > 0.10:

    print("Model may be overfitting.")

elif train_accuracy < 0.70 and test_accuracy < 0.70:

    print("Model may be underfitting.")

else:

    print("Model performance is reasonably balanced.")