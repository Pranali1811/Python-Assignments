import pandas as pd
df = pd.read_csv('student_performance_ml.csv')
print("First 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())
print("\nDataset Shape (Rows, Columns):", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)