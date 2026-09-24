import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('student_performance_ml.csv')
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, 
    x='StudyHours', 
    y='PreviousScore', 
    hue='FinalResult', 
    palette={1: 'green', 0: 'red'}, 
    s=80
)
plt.title('Study Hours vs Previous Score (Colored by Pass/Fail)')
plt.xlabel('Study Hours')
plt.ylabel('Previous Score')
plt.legend(title='Final Result', labels=['Pass (1)', 'Fail (0)'])
plt.tight_layout()
plt.show()