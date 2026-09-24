import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([50, 55, 60, 65, 70])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Print coefficient
print("Coefficient =", model.coef_[0])

# Print intercept
print("Intercept =", model.intercept_)