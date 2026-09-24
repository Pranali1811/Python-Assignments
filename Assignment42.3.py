import math

# --------------------------------------------------
# Border
# --------------------------------------------------

Border = "-" * 50

print(Border)
print("Student Pass/Fail using KNN")
print(Border)


# --------------------------------------------------
# Dataset
# --------------------------------------------------

Data = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]


# --------------------------------------------------
# Accept Student Input
# --------------------------------------------------

StudyHours = float(input("Enter Study Hours: "))
Attendance = float(input("Enter Attendance: "))


# --------------------------------------------------
# Calculate Euclidean Distance
# --------------------------------------------------

Distances = []

for hours, attendance, result in Data:

    distance = math.sqrt(
        (StudyHours - hours) ** 2 +
        (Attendance - attendance) ** 2
    )

    Distances.append(
        (distance, result)
    )


# --------------------------------------------------
# Sort Distances
# --------------------------------------------------

Distances.sort()


# --------------------------------------------------
# Select K Neighbors
# --------------------------------------------------

K = 3

Nearest = Distances[:K]


print("\nNearest Neighbors:")

for distance, result in Nearest:

    print(
        "Distance:",
        round(distance, 2),
        "Result:",
        result
    )


# --------------------------------------------------
# Majority Voting
# --------------------------------------------------

Results = [item[1] for item in Nearest]

Pass_Count = Results.count("Pass")
Fail_Count = Results.count("Fail")


if Pass_Count > Fail_Count:
    Prediction = "Pass"
else:
    Prediction = "Fail"


# --------------------------------------------------
# Final Prediction
# --------------------------------------------------

print("\nPredicted Result:", Prediction)

print(Border)