import numpy as np
from sklearn.preprocessing import StandardScaler

# Dataset
Dataset = np.array([
    [25, 200000],
    [30, 400000],
    [35, 800000]
])

# Create StandardScaler
scaler = StandardScaler()

# Apply scaling
Scaled_Data = scaler.fit_transform(Dataset)

print("Scaled Dataset:")
print(Scaled_Data)