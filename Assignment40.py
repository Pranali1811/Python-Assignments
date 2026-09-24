# ============================================================
# STUDENT PERFORMANCE ML DATASET
# DECISION TREE CLASSIFIER - ADVANCED ANALYSIS
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score


# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv("student_performance_ml.csv")

print("=" * 70)
print("          STUDENT PERFORMANCE ML DATASET")
print("=" * 70)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


# ------------------------------------------------------------
# 3. DEFINE FEATURES AND TARGET
# ------------------------------------------------------------

features = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[features]
y = df["FinalResult"]


# ------------------------------------------------------------
# 4. TRAIN-TEST SPLIT
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ------------------------------------------------------------
# 5. TRAIN DECISION TREE MODEL
# ------------------------------------------------------------

model = DecisionTreeClassifier(
    random_state=42
)

model.fit(X_train, y_train)


# ------------------------------------------------------------
# 6. PREDICTION
# ------------------------------------------------------------

y_pred = model.predict(X_test)


# ------------------------------------------------------------
# 7. ORIGINAL MODEL ACCURACY
# ------------------------------------------------------------

original_accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 70)
print("ORIGINAL MODEL ACCURACY")
print("=" * 70)

print("Testing Accuracy = {:.2f}%".format(
    original_accuracy * 100
))


# ============================================================
# QUESTION 1
# FEATURE IMPORTANCE
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 1 - FEATURE IMPORTANCE")
print("=" * 70)

importance = model.feature_importances_

feature_importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

# Sort from highest to lowest
feature_importance_df = feature_importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance_df)


# Most important feature
most_important = feature_importance_df.iloc[0]

# Least important feature
least_important = feature_importance_df.iloc[-1]

print("\nMost Important Feature:")
print(
    most_important["Feature"],
    "->",
    most_important["Importance"]
)

print("\nLeast Important Feature:")
print(
    least_important["Feature"],
    "->",
    least_important["Importance"]
)

print("""
Observation:
The feature having the highest feature importance contributes
the most to predicting the FinalResult.

The feature having the lowest feature importance contributes
the least.
""")


# ============================================================
# QUESTION 2
# REMOVE SLEEP HOURS
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 2 - REMOVE SLEEP HOURS")
print("=" * 70)

features_without_sleep = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
]

X_no_sleep = df[features_without_sleep]

X_train_ns, X_test_ns, y_train_ns, y_test_ns = train_test_split(
    X_no_sleep,
    y,
    test_size=0.20,
    random_state=42
)

model_no_sleep = DecisionTreeClassifier(
    random_state=42
)

model_no_sleep.fit(
    X_train_ns,
    y_train_ns
)

y_pred_ns = model_no_sleep.predict(X_test_ns)

accuracy_no_sleep = accuracy_score(
    y_test_ns,
    y_pred_ns
)

print("Original Accuracy     = {:.2f}%".format(
    original_accuracy * 100
))

print("Without SleepHours    = {:.2f}%".format(
    accuracy_no_sleep * 100
))

print("Accuracy Difference   = {:.2f}%".format(
    (accuracy_no_sleep - original_accuracy) * 100
))

if accuracy_no_sleep > original_accuracy:

    print("\nObservation:")
    print("Removing SleepHours improved the model accuracy.")

elif accuracy_no_sleep < original_accuracy:

    print("\nObservation:")
    print("Removing SleepHours reduced the model accuracy.")

else:

    print("\nObservation:")
    print("Removing SleepHours did not change the accuracy.")


# ============================================================
# QUESTION 3
# USE ONLY STUDY HOURS AND ATTENDANCE
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 3 - STUDY HOURS + ATTENDANCE ONLY")
print("=" * 70)

two_features = [
    "StudyHours",
    "Attendance"
]

X_two = df[two_features]

X_train_two, X_test_two, y_train_two, y_test_two = train_test_split(
    X_two,
    y,
    test_size=0.20,
    random_state=42
)

model_two = DecisionTreeClassifier(
    random_state=42
)

model_two.fit(
    X_train_two,
    y_train_two
)

y_pred_two = model_two.predict(X_test_two)

accuracy_two = accuracy_score(
    y_test_two,
    y_pred_two
)

print("Full Feature Accuracy      = {:.2f}%".format(
    original_accuracy * 100
))

print("StudyHours + Attendance    = {:.2f}%".format(
    accuracy_two * 100
))

print("\nObservation:")

if accuracy_two >= original_accuracy:
    print("""
The model is still performing well using only StudyHours
and Attendance. These two features contain useful information
for predicting student performance.
""")
else:
    print("""
The accuracy decreased when only StudyHours and Attendance
were used. This indicates that the other features also provide
useful information for prediction.
""")


# ============================================================
# QUESTION 4
# PREDICT 5 NEW STUDENTS
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 4 - PREDICTION FOR 5 NEW STUDENTS")
print("=" * 70)


# Create DataFrame containing 5 new students
new_students = pd.DataFrame({

    "StudyHours": [2, 4, 6, 8, 10],

    "Attendance": [60, 70, 85, 90, 95],

    "PreviousScore": [45, 55, 66, 78, 88],

    "AssignmentsCompleted": [3, 5, 7, 9, 10],

    "SleepHours": [6, 7, 7, 8, 8]
})


# Predict using original trained model
new_predictions = model.predict(new_students)


# Add prediction column
new_students["PredictedResult"] = new_predictions


# Convert 0/1 into Fail/Pass
new_students["Result"] = new_students["PredictedResult"].map({
    0: "Fail",
    1: "Pass"
})


print("\nPrediction of 5 New Students:")
print(new_students)


# ============================================================
# QUESTION 5
# MANUALLY CALCULATE ACCURACY
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 5 - MANUAL ACCURACY CALCULATION")
print("=" * 70)


# Count correct predictions
correct_predictions = 0

for actual, predicted in zip(y_test, y_pred):

    if actual == predicted:
        correct_predictions += 1


total_predictions = len(y_test)

manual_accuracy = (
    correct_predictions / total_predictions
)


print("Total Test Samples       :", total_predictions)

print("Correct Predictions      :", correct_predictions)

print("Incorrect Predictions    :",
      total_predictions - correct_predictions)

print("Manual Accuracy          = {:.2f}%".format(
    manual_accuracy * 100
))

print("Sklearn Accuracy         = {:.2f}%".format(
    original_accuracy * 100
))


if manual_accuracy == original_accuracy:

    print("\nVerification:")
    print("Manual accuracy MATCHES sklearn accuracy.")

else:

    print("\nVerification:")
    print("Manual accuracy does NOT match sklearn accuracy.")


# ============================================================
# QUESTION 6
# IDENTIFY MISCLASSIFIED STUDENTS
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 6 - MISCLASSIFIED STUDENTS")
print("=" * 70)


# Create a copy of test data
misclassified = X_test.copy()

# Add actual and predicted results
misclassified["ActualResult"] = y_test

misclassified["PredictedResult"] = y_pred


# Select only incorrectly classified students
misclassified = misclassified[
    misclassified["ActualResult"] !=
    misclassified["PredictedResult"]
]


print("\nMisclassified Students:")

if len(misclassified) > 0:

    print(misclassified)

else:

    print("No students were misclassified.")


print("\nNumber of Misclassified Students:",
      len(misclassified))


print("""
Observation:
Misclassified students are students for whom the model's
prediction is different from their actual FinalResult.

Common patterns can be identified by looking at their
StudyHours, Attendance, PreviousScore, AssignmentsCompleted
and SleepHours values.
""")


# ============================================================
# QUESTION 7
# COMPARE DIFFERENT RANDOM STATES
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 7 - RANDOM STATE COMPARISON")
print("=" * 70)


random_states = [0, 10, 42]

for state in random_states:

    X_train_rs, X_test_rs, y_train_rs, y_test_rs = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=state
    )

    model_rs = DecisionTreeClassifier(
        random_state=state
    )

    model_rs.fit(
        X_train_rs,
        y_train_rs
    )

    prediction_rs = model_rs.predict(X_test_rs)

    accuracy_rs = accuracy_score(
        y_test_rs,
        prediction_rs
    )

    print(
        "Random State {} -> Testing Accuracy = {:.2f}%".format(
            state,
            accuracy_rs * 100
        )
    )


print("""
Observation:
Changing random_state changes how the dataset is divided into
training and testing data.

Therefore, testing accuracy may change.

A model can perform slightly differently depending on which
students are included in the training and testing sets.
""")


# ============================================================
# QUESTION 8
# DECISION TREE VISUALIZATION
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 8 - DECISION TREE VISUALIZATION")
print("=" * 70)


plt.figure(figsize=(20, 10))

plot_tree(
    model,
    feature_names=features,
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True
)

plt.title("Decision Tree - Student Performance")

plt.show()


# ------------------------------------------------------------
# FIND ROOT NODE
# ------------------------------------------------------------

root_feature_index = model.tree_.feature[0]

root_feature = features[root_feature_index]

print("\nRoot Node Feature:")
print(root_feature)

print("""
Explanation:
The root node is the first feature used by the Decision Tree.

Decision Trees select a feature that gives the best split of
the training data according to the splitting criterion.

Therefore, the feature at the root generally provides the
strongest separation between Pass and Fail students at the
first decision.
""")


# ============================================================
# QUESTION 9
# PERFORMANCE INDEX
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 9 - PERFORMANCE INDEX")
print("=" * 70)


# Create a copy of dataset
df_index = df.copy()


# PerformanceIndex formula
df_index["PerformanceIndex"] = (
    (df_index["StudyHours"] * 2)
    + df_index["Attendance"]
)


print("\nDataset with PerformanceIndex:")
print(
    df_index[
        [
            "StudyHours",
            "Attendance",
            "PerformanceIndex"
        ]
    ].head()
)


# Features including new PerformanceIndex
features_index = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "PerformanceIndex"
]


X_index = df_index[features_index]

y_index = df_index["FinalResult"]


# Train-test split
X_train_index, X_test_index, y_train_index, y_test_index = train_test_split(
    X_index,
    y_index,
    test_size=0.20,
    random_state=42
)


# Train model
model_index = DecisionTreeClassifier(
    random_state=42
)

model_index.fit(
    X_train_index,
    y_train_index
)


# Prediction
y_pred_index = model_index.predict(
    X_test_index
)


# Accuracy
accuracy_index = accuracy_score(
    y_test_index,
    y_pred_index
)


print("\nOriginal Model Accuracy = {:.2f}%".format(
    original_accuracy * 100
))

print("PerformanceIndex Model  = {:.2f}%".format(
    accuracy_index * 100
))


if accuracy_index > original_accuracy:

    print("\nObservation:")
    print("Adding PerformanceIndex IMPROVED the accuracy.")

elif accuracy_index < original_accuracy:

    print("\nObservation:")
    print("Adding PerformanceIndex DECREASED the accuracy.")

else:

    print("\nObservation:")
    print("Adding PerformanceIndex DID NOT CHANGE the accuracy.")


# ============================================================
# QUESTION 10
# MAX_DEPTH = NONE
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 10 - MAX_DEPTH = NONE")
print("=" * 70)


model_none = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)


# Train model
model_none.fit(
    X_train,
    y_train
)


# Training prediction
train_prediction_none = model_none.predict(
    X_train
)


# Testing prediction
test_prediction_none = model_none.predict(
    X_test
)


# Calculate training accuracy
training_accuracy_none = accuracy_score(
    y_train,
    train_prediction_none
)


# Calculate testing accuracy
testing_accuracy_none = accuracy_score(
    y_test,
    test_prediction_none
)


print("\nTraining Accuracy = {:.2f}%".format(
    training_accuracy_none * 100
))

print("Testing Accuracy  = {:.2f}%".format(
    testing_accuracy_none * 100
))


# ------------------------------------------------------------
# OVERFITTING CHECK
# ------------------------------------------------------------

accuracy_difference = (
    training_accuracy_none -
    testing_accuracy_none
)


print("\nAccuracy Difference = {:.2f}%".format(
    accuracy_difference * 100
))


if training_accuracy_none == 1.0 and testing_accuracy_none < 1.0:

    print("""
CONCLUSION:
The model has 100% training accuracy but lower testing
accuracy.

This indicates OVERFITTING.

The Decision Tree has learned the training data extremely
well, including patterns/noise that may not generalize to
unseen students.

As a result, it performs perfectly on training data but
makes some errors on testing data.
""")

elif training_accuracy_none > testing_accuracy_none:

    print("""
CONCLUSION:
Training accuracy is higher than testing accuracy.

This indicates that the model may be overfitting to some
extent. The model performs better on data it has already
seen than on unseen data.
""")

else:

    print("""
CONCLUSION:
Training and testing accuracy are relatively similar.

There is no strong indication of overfitting based only
on these accuracy values.
""")


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("                         FINAL SUMMARY")
print("=" * 70)

print("""
1. Feature importance was calculated using
   model.feature_importances_.

2. The most and least important features were identified.

3. SleepHours was removed and the new accuracy was compared.

4. A model using only StudyHours and Attendance was trained.

5. Five new students were created and their results were
   predicted.

6. Accuracy was manually calculated and compared with
   sklearn accuracy_score.

7. Misclassified students were identified.

8. Different random states (0, 10 and 42) were compared.

9. The Decision Tree was visualized using plot_tree().

10. The root node feature was identified.

11. PerformanceIndex was created and its effect on accuracy
    was evaluated.

12. A Decision Tree with max_depth=None was trained and
    training/testing accuracy were compared.

The project demonstrates how Decision Tree Machine Learning
can be used to predict student Pass/Fail results.
""")

print("=" * 70)
print("                 PROGRAM EXECUTION COMPLETED")
print("=" * 70)