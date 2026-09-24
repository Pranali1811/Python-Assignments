import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
print("Step 1: Loading Dataset...")
df = pd.read_csv('student_performance_ml.csv')
print("Dataset loaded successfully.\n")
print("Step 2: Basic Data Analysis...")
print(f"Total Rows & Columns: {df.shape}")
print(df.describe())
print("\nTarget Class Distribution:")
print(df['FinalResult'].value_counts())
print("-" * 40)
print("Step 3: Generating Visualizations...")
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='FinalResult', palette='Set2')
plt.title("Distribution of Pass (1) and Fail (0)")
plt.show()
print("Step 4: Splitting Data into Train and Test sets...")
X = df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
y = df['FinalResult']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Step 5: Training DecisionTreeClassifier Model...")
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
print("Step 6: Predicting on Test Data...")
y_pred = model.predict(X_test)
print("Step 7: Calculating Model Accuracy...")
acc = accuracy_score(y_test, y_pred) * 100
print(f"Testing Accuracy: {acc:.2f}%\n")
print("Step 8: Generating Confusion Matrix...")
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Fail', 'Pass'])
disp.plot(cmap=plt.cm.Greens)
plt.title("Confusion Matrix")
plt.show()
print("Step 9: Final Conclusion")
print("The Decision Tree model effectively predicts student performance.")
print("Key features such as StudyHours, Attendance, and PreviousScore serve as vital metrics for early academic risk evaluation.")