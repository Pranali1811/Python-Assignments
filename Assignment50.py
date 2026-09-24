# ============================================================
# BREAST CANCER CLASSIFICATION USING MACHINE LEARNING
# ============================================================

# Step 1: Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# ============================================================
# Step 2: Load the dataset
# ============================================================

data = load_breast_cancer()

# Create DataFrame
df = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

# Add target column
df['target'] = data.target

print("First 5 rows:")
print(df.head())


# ============================================================
# Step 3: Explore the dataset
# ============================================================

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())


# ============================================================
# Step 4: Check missing values
# ============================================================

print("\nMissing Values:")
print(df.isnull().sum().sum())


# ============================================================
# Step 5: Check target values
# ============================================================

print("\nTarget Values:")
print(df['target'].value_counts())

print("\n0 = Malignant")
print("1 = Benign")


# ============================================================
# Step 6: Separate features and target
# ============================================================

X = df.drop('target', axis=1)
Y = df['target']


# ============================================================
# Step 7: Feature Correlation
# ============================================================

correlation = X.corr()

print("\nCorrelation Matrix:")
print(correlation)


# ============================================================
# Step 8: Display correlation heatmap
# ============================================================

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation,
    cmap="coolwarm"
)

plt.title("Feature Correlation Heatmap")
plt.show()


# ============================================================
# Step 9: Split dataset into training and testing
# ============================================================

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# ============================================================
# Step 10: Normalize / Scale Features
# ============================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

print("\nFeatures Scaled Successfully")


# ============================================================
# Step 11: Create classification model
# ============================================================

model = LogisticRegression(max_iter=1000)


# ============================================================
# Step 12: Train the model
# ============================================================

model.fit(X_train, Y_train)

print("Model Training Completed")


# ============================================================
# Step 13: Predict test values
# ============================================================

Y_pred = model.predict(X_test)

print("\nPredicted Values:")
print(Y_pred)


# ============================================================
# Step 14: Calculate Accuracy
# ============================================================

accuracy = accuracy_score(Y_test, Y_pred)

print("\nAccuracy =", accuracy)
print("Accuracy Percentage =", accuracy * 100, "%")


# ============================================================
# Step 15: Confusion Matrix
# ============================================================

cm = confusion_matrix(Y_test, Y_pred)

print("\nConfusion Matrix:")
print(cm)


# Display confusion matrix
plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()


# ============================================================
# Step 16: Classification Report
# ============================================================

print("\nClassification Report:")

print(
    classification_report(
        Y_test,
        Y_pred,
        target_names=["Malignant", "Benign"]
    )
)