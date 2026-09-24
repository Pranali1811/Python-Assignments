import pandas as pd
df = pd.read_csv('student_performance_ml.csv')
total_students = len(df)
passed_students = (df['FinalResult'] == 1).sum()
failed_students = (df['FinalResult'] == 0).sum()
print(f"Total number of students in dataset: {total_students}")
print(f"Number of students who Passed (FinalResult = 1): {passed_students}")
print(f"Number of students who Failed (FinalResult = 0): {failed_students}")