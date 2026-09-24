import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('student_performance_ml.csv')
X = df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
y = df['FinalResult']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
train_acc = accuracy_score(y_train, model.predict(X_train)) * 100
test_acc = accuracy_score(y_test, model.predict(X_test)) * 100
print(f"Training Accuracy: {train_acc:.2f}%")
print(f"Testing Accuracy: {test_acc:.2f}%")
if train_acc > 95 and (train_acc - test_acc) > 10:
    print("\nObservation: The model is OVERFITTING because training accuracy is very high compared to testing accuracy.")
elif train_acc < 70 and test_acc < 70:
    print("\nObservation: The model is UNDERFITTING because both training and testing accuracies are low.")
else:
    print("\nObservation: The model is BALANCED with good generalization performance.")