import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([50, 55, 60, 65, 70])

# Create model
model = LinearRegression()

# Train model
model.fit(X, Y)

# Predict marks for 6 study hours
prediction = model.predict([[6]])

print("Predicted Marks for 6 Study Hours:", int(prediction[0]))