import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('student_performance_ml.csv')
plt.figure(figsize=(7, 4))
sns.barplot(data=df, x='AssignmentsCompleted', y='FinalResult', errorbar=None, palette='viridis')
plt.title('Pass Rate by Assignments Completed')
plt.xlabel('Number of Assignments Completed')
plt.ylabel('Pass Rate (Proportion)')
plt.tight_layout()
plt.show()