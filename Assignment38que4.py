import pandas as pd
df = pd.read_csv('student_performance_ml.csv')
counts = df['FinalResult'].value_counts()
percentages = df['FinalResult'].value_counts(normalize=True) * 100
print("--- Class Distribution Counts ---")
print(counts)
print("\n--- Class Distribution Percentages ---")
print(percentages)
pass_ratio = percentages.get(1, 0)
if 40 <= pass_ratio <= 60:
    print("\nConclusion: The dataset is BALANCED because Pass and Fail classes have a similar proportion.")
else:
    print("\nConclusion: The dataset is IMBALANCED because one class significantly outweighs the other.")