import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([
    [1, 7],
    [2, 6],
    [3, 7],
    [4, 6],
    [5, 8]
])

Y = np.array([50, 55, 60, 65, 70])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Print coefficients
print("Coefficient of Study Hours =", model.coef_[0])
print("Coefficient of Sleep Hours =", model.coef_[1])

# Print intercept
print("Intercept =", model.intercept_)