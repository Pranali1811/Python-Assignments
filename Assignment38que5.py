import pandas as pd
df = pd.read_csv('student_performance_ml.csv')
study_corr = df['StudyHours'].corr(df['FinalResult'])
att_corr = df['Attendance'].corr(df['FinalResult'])
print(f"Correlation between StudyHours and FinalResult: {study_corr:.2f}")
print(f"Correlation between Attendance and FinalResult: {att_corr:.2f}")