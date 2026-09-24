import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv('student_performance_ml.csv')
X = df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
y = df['FinalResult']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
new_student = pd.DataFrame([{
    'StudyHours': 6,
    'Attendance': 85,
    'PreviousScore': 66,
    'AssignmentsCompleted': 7,
    'SleepHours': 7
}])
prediction = model.predict(new_student)[0]
result_str = "PASS" if prediction == 1 else "FAIL"

print(f"Predicted Result for the student: {result_str} (Value: {prediction})")