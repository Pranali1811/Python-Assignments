import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('student_performance_ml.csv')
plt.figure(figsize=(7, 4))
sns.histplot(df['StudyHours'], kde=True, color='skyblue', bins=10)
plt.title('Distribution of Study Hours')
plt.xlabel('Study Hours per Day')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()