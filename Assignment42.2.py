import math

# --------------------------------------------------
# Border
# --------------------------------------------------

Border = "-" * 50

print(Border)
print("Effect of K in KNN")
print(Border)


# --------------------------------------------------
# Dataset
# --------------------------------------------------

Data = [
    (1, 2, "Red"),
    (2, 3, "Red"),
    (3, 1, "Blue"),
    (6, 5, "Blue")
]


# --------------------------------------------------
# New Point
# --------------------------------------------------

X = float(input("Enter X coordinate: "))
Y = float(input("Enter Y coordinate: "))


# --------------------------------------------------
# Calculate Distances
# --------------------------------------------------

Distances = []

for point_x, point_y, label in Data:

    distance = math.sqrt(
        (X - point_x) ** 2 +
        (Y - point_y) ** 2
    )

    Distances.append((distance, label))


# Sort distances
Distances.sort()


# --------------------------------------------------
# Function for Prediction
# --------------------------------------------------

def Predict(K):

    Nearest = Distances[:K]

    Labels = [item[1] for item in Nearest]

    Red_Count = Labels.count("Red")
    Blue_Count = Labels.count("Blue")

    if Red_Count > Blue_Count:
        return "Red"
    else:
        return "Blue"


# --------------------------------------------------
# Predictions
# --------------------------------------------------

print("\nPrediction Results:")

for K in [1, 3, 5]:

    Result = Predict(K)

    print("K =", K, "->", Result)


print(Border)