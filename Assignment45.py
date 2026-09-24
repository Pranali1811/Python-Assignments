import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


# ============================================================
# Create DataFrame
# ============================================================

Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(Data)

print(" Data is :")
print(df)

# ============================================================
# Q1 : Normalize Math scores using Min-Max Scaling
# ============================================================

scaler = MinMaxScaler()

df['Math_Normalized'] = scaler.fit_transform(
    df[['Math']]
)

print(" Math scores after Min-Max Scaling is :")
print(df[['Name', 'Math', 'Math_Normalized']])


# ============================================================
# Q2 : Create Gender column and perform One-Hot Encoding
# ============================================================

df['Gender'] = [
    'Male',
    'Male',
    'Female'
]

print(" Gender Column is :")
print(df[['Name', 'Gender']])


# One-Hot Encoding

df = pd.get_dummies(
    df,
    columns=['Gender'],
    dtype=int
)

print("After One-Hot Encoding:")
print(df)

# ============================================================
# Q3 : Group students by Gender and calculate average marks
# ============================================================

# Create Gender column again for grouping
df['Gender'] = [
    'Male',
    'Male',
    'Female'
]

Average_marks = df.groupby('Gender')[
    ['Math', 'Science', 'English']
].mean()

print(" Average Marks by Gender is :")
print(Average_marks)


# ============================================================
# Q4 : Pie chart of subject marks for Sagar
# ============================================================

sagar = df[df['Name'] == 'Sagar'].iloc[0]

subjects = [
    'Math',
    'Science',
    'English'
  ]

marks = [
    sagar['Math'],
    sagar['Science'],
    sagar['English']
  ]

plt.figure()

plt.pie(
    marks,
    labels=subjects,
    autopct='%1.1f%%'
  )

plt.title("Subject Marks of Sagar")

plt.show()


# ============================================================
# Q5 : Add Status column
# ============================================================

df['Total'] = (
    df['Math'] + df['Science'] + df['English']
)

df['Status'] = df['Total'].apply(
    lambda x: 'Pass' if x >= 250 else 'Fail'
)

print(" Student Status is :")
print(df[['Name', 'Math', 'Science','English', 'Total', 'Status']])

# ============================================================
# Q6 : Count how many students passed
# ============================================================

passed_count = (
    df['Status'] == 'Pass'
).sum()

print(" Number of Students Passed is :")
print(passed_count)


# ============================================================
# Q7 : Export final DataFrame to CSV
# ============================================================

df.to_csv(
    'Final_Student_Data.csv',
    index=False
)

print(" Data exported successfully is ")
print("File: Final_Student_Data.csv")


# ============================================================
# Q8 : Histogram of Math marks
# ============================================================

plt.figure()

plt.hist(
    df['Math'],
    bins=3,
    edgecolor='black'
)

plt.xlabel('Math Marks')
plt.ylabel('Number of Students')

plt.title('Histogram of Math Marks')

plt.show()


# ============================================================
# Q9 : Rename Math column to Mathematics
# ============================================================

df.rename(
    columns={
        'Math': 'Mathematics'
    },
    inplace=True
)

print(" After Renaming Math to Mathematics is :")
print(df)


# ============================================================
# Q10 : Boxplot for English marks
# ============================================================

plt.figure()

plt.boxplot(
    df['English']
)

plt.ylabel('English Marks')

plt.title('Boxplot of English Marks is ')

plt.show()












