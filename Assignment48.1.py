# ============================================================
# Q1 : Simple Linear Regression Manually
# ============================================================

import numpy as np

# Dataset
X = np.array([1, 2, 3, 4, 5])
Y = np.array([3, 4, 2, 4, 5])

# Number of data points
n = len(X)

# Step 1 : Mean of X
X_mean = np.mean(X)

# Step 2 : Mean of Y
Y_mean = np.mean(Y)

# Step 3 : Calculate slope
numerator = np.sum((X - X_mean) * (Y - Y_mean))
denominator = np.sum((X - X_mean) ** 2)

m = numerator / denominator

# Step 4 : Calculate intercept
c = Y_mean - (m * X_mean)

# Step 5 : Regression equation
print("Mean of X =", X_mean)
print("Mean of Y =", Y_mean)

print("Slope (m) = ", m)
print("Intercept (c) = ", c)

print(" Regression Equation:")
print("Y =", m, "* X +", c)

# Step 6 : Predict Y for X = 6
X_new = 6

Y_pred = (m * X_new) + c  

print(" Predicted Y for X = 6:", Y_pred)

