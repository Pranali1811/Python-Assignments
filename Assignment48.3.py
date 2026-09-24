import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset 
X = np.array([[1], [2], [3],[4], [5]])           # independent Variavle 

Y = np.array([20000,25000,30000,35000,40000])

# create the model 

model = LinearRegression()

# Train the model

model.fit(X,Y)

#Predict salary for 6 years
Prediction =model.predict([[6]])
print("Predicted Salary for 6 Years Experience: ₹", int(Prediction[0]))

# Predict values for regression line
y_pred = model.predict(X)

# plot data point 
plt.scatter (X,Y, label ="Regression Line ")
plt.scatter (X,Y, label ="Data point")
plt.xlabel("Years of Expriences ")
plt.ylabel("Salary")
plt.title("Expriences VS Salary ")
plt.legend()
plt.show()