# ================================
# IntelliMarket AI
# Step 6: Customer Segmentation
# ================================

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("customers.csv")

# Convert columns to numeric (VERY IMPORTANT)
df["age"] = pd.to_numeric(df["age"])
df["income"] = pd.to_numeric(df["income"])
df["spending"] = pd.to_numeric(df["spending"])

# Select features for clustering
X = df[["age", "income", "spending"]]

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df["Segment"] = kmeans.fit_predict(X_scaled)

# Output results
print("\nCustomer Segmentation Result")
print("============================")
print(df)

print("\nSegment-wise Average Values")
print("===========================")
print(df.groupby("Segment")[["age", "income", "spending"]].mean())

# Save segmented data
df.to_csv("customers_segmented.csv", index=False)
print("customers_segmented.csv file created successfully")
