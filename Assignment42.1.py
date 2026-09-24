import math

# --------------------------------------------------
# Border
# --------------------------------------------------

Border = "-" * 50

print(Border)
print("KNN Classification - Manual")
print(Border)


# --------------------------------------------------
# Dataset
# --------------------------------------------------

Data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]


# --------------------------------------------------
# Accept New Point
# --------------------------------------------------

X = float(input("Enter the X coordinate: "))
Y = float(input("Enter the Y coordinate: "))


# --------------------------------------------------
# Calculate Euclidean Distance
# --------------------------------------------------

Distances = []

for Point, X_point, Y_point, label in Data:

    distance = math.sqrt(
        (X - X_point) ** 2 +
        (Y - Y_point) ** 2
    )

    Distances.append((distance, Point, label))


# --------------------------------------------------
# Sort Distances
# --------------------------------------------------

Distances.sort()


# --------------------------------------------------
# Select K = 3 Nearest Neighbours
# --------------------------------------------------

K = 3

Nearest = Distances[:K]


# --------------------------------------------------
# Display Nearest Neighbors
# --------------------------------------------------

print("\nNearest Neighbors:")

for distance, Point, label in Nearest:

    print(
        Point,
        "- Distance:",
        round(distance, 2),
        "- Label:",
        label
    )


# --------------------------------------------------
# Majority Voting
# --------------------------------------------------

Labels = [item[2] for item in Nearest]

Red_Count = Labels.count("Red")
Blue_Count = Labels.count("Blue")


if Red_Count > Blue_Count:
    Prediction = "Red"
else:
    Prediction = "Blue"


# --------------------------------------------------
# Final Prediction
# --------------------------------------------------

print("\nRed Votes:", Red_Count)
print("Blue Votes:", Blue_Count)

print("\nPredicted Class:", Prediction)

print(Border)