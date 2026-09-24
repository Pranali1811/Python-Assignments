import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

# --------------------------------------------------
# Q1 : Create DataFrame and print basic information
# --------------------------------------------------

Data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
}

df = pd.DataFrame(Data)

print("========== Q2: print Descriptive Statistics using .describe()  ==========")

print("first 5 Records :")
print(df.head())

print("Last recodes :")
print(df.tail())

print("Check Messing value in datase :")
print(df.isnull().sum())

print("Shape of Dataset :")
print(df.shape)

print("Data type of Dataset is :")
print(df.dtypes)

print("Colunms in Dtaset is :")
print(df.columns)

# --------------------------------------------------
# Q2 : Descriptive Statistics
# --------------------------------------------------
print("Descriptive Statistics is :")
print(df.describe())


# --------------------------------------------------
# Q3 : Add Total column
# --------------------------------------------------

df["Total"] = df["Math"] + df["Science"] + df["English"]
print("DataFrame after adding Total is :")
print(df)

# --------------------------------------------------
# Q4 : Students scoring more than 85 in Science
# --------------------------------------------------
Result = df[df["Science"] >85 ]
print("Students who scored more than 85 in Science:")
print(Result)

# --------------------------------------------------
# Q5 : Replace Pooja with Puja
# --------------------------------------------------
df['Name'] = df["Name"].replace("Pooja", "Puja")

print("DataFrame after replacing Pooja with Puja is :")
print(df)

# --------------------------------------------------
# Q6 : Sort by Total in descending order
# --------------------------------------------------
df = df.sort_values(by ="Total",ascending= False)
print("DataFrame sorted by Total marks is :")
print(df)


# --------------------------------------------------
# Q7 : Bar Plot of Name vs Total
# --------------------------------------------------

plt.bar(df["Name"], df["Total"])

plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.title("Student Names vs Total Marks")

plt.show()
# --------------------------------------------------
# Q8 : Line chart of Amit's marks
# --------------------------------------------------


amit = df[df["Name"] == "Amit"].iloc[0]

subjects = ["Math", "Science", "English"]
marks = [
    amit["Math"],
    amit["Science"],
    amit["English"]
]

plt.plot(subjects, marks, marker="o")

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Amit's Marks Across All Subjects")

plt.show()

# --------------------------------------------------
# Q9 : Missing values and fill with column mean
# --------------------------------------------------

# Created Dataframe 2
data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

# Create DataFrame with missing values

df2 = pd.DataFrame(data2)

print("DataFrame with missing value is :")
print(df2)

# Fill missing Math values with Math mean
df2["Math"] = df2["Math"].fillna(df2["Math"].mean())

# Fill missing Science values with Science mean
df2["Science"] = df2["Science"].fillna(df2["Science"].mean())

print("DataFrame after filling missing values:")
print(df2)



# --------------------------------------------------
# Q10 : Drop English column
# --------------------------------------------------


df_without_english = df.drop("English", axis=1)

print("DataFrame after dropping English column:")
print(df_without_english)