import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('student_performance_ml.csv')
plt.figure(figsize=(7, 4))
sns.boxplot(data=df, x='FinalResult', y='SleepHours', palette={1: 'green', 0: 'red'})
plt.title('Sleep Hours vs Final Result')
plt.xlabel('Final Result (0 = Fail, 1 = Pass)')
plt.ylabel('Sleep Hours per Day')
plt.tight_layout()
plt.show()