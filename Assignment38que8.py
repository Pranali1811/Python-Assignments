import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('student_performance_ml.csv')
plt.figure(figsize=(7, 4))
sns.boxplot(x=df['Attendance'], color='orange')
plt.title('Boxplot of Attendance')
plt.xlabel('Attendance (%)')
plt.tight_layout()
plt.show()
q1 = df['Attendance'].quantile(0.25)
q3 = df['Attendance'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df['Attendance'] < lower_bound) | (df['Attendance'] > upper_bound)]

if len(outliers) > 0:
    print(f"Outliers detected ({len(outliers)} students):")
    print(outliers[['Attendance']])
else:
    print("No statistical outliers present in the Attendance column.")