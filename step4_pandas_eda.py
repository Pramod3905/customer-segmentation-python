# ==============================
# IntelliMarket AI
# Step 4: Pandas EDA
# ==============================

import pandas as pd

# Load CSV using Pandas
df = pd.read_csv("customers.csv")

print("Customer DataFrame")
print("------------------")
print(df)

# Basic information
print("\nData Info:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Average income & spending
print("\nAverage Income:", df["income"].mean())
print("Average Spending Score:", df["spending"].mean())

# High spenders
high_spenders = df[df["spending"] >= 70]
print("\nHigh Spenders:")
print(high_spenders)
