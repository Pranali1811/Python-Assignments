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

# Step 6 : Predict Y values

Y_pred = m*X + c

print("Predicted Y values:")

for i in range(n):
    print("X =", X[i],
          "Actual Y =", Y[i],
          "Predicted Y =", Y_pred[i])





# Step 7 : Calculate MSE



# MSE
MSE = np.mean((Y - Y_pred) ** 2)


print("Mean Squared Error (MSE) =", MSE)

# Step 8 : Calculate R² Score
#
# R² = 1 - (SSres / SStot)


SS_res = np.sum((Y - Y_pred) ** 2)

SS_tot = np.sum((Y - Y_mean) ** 2)

R2 = 1 - (SS_res / SS_tot)

print("\nSS_res =", SS_res)
print("SS_tot =", SS_tot)
print("R² Score =", R2)