import numpy as np
from sklearn.preprocessing import StandardScaler

# Dataset
Dataset = np.array([
    [25, 200000],
    [30, 400000],
    [35, 800000]
])

# Select two points
P1 = Dataset[0]
P2 = Dataset[1]

# Distance before scaling
Distance_Before = np.linalg.norm(P1 - P2)

print("Distance Before Scaling =", Distance_Before)

# Create scaler
Scaler = StandardScaler()

# Scale dataset
scaled_data = Scaler.fit_transform(Dataset)

# Distance after scaling
Distance_After = np.linalg.norm(
    scaled_data[0] - scaled_data[1]
)

print("Distance After Scaling =", Distance_After)