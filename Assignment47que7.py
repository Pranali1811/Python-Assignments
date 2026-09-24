from sklearn.linear_model import LinearRegression

# Data
X = [[1], [2], [3], [4], [5]]
y = [50, 55, 60, 65, 70]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Print coefficient
print("Coefficient:", model.coef_[0])

# Print intercept
print("Intercept:", model.intercept_)