from sklearn.metrics import classification_report

# Actual values
actual = [1, 1, 1, 1, 0, 0, 0, 0]

# Predicted values
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

# Generate classification report
report = classification_report(actual, predicted)

print(report)