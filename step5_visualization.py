# ==============================
# IntelliMarket AI
# Step 5: Data Visualization
# ==============================

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customers.csv")

# Scatter plot: Income vs Spending
plt.figure()
plt.scatter(df["income"], df["spending"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Income vs Spending Analysis")
plt.show()

# Bar chart: Average spending by age
avg_spending_by_age = df.groupby("age")["spending"].mean()

plt.figure()
avg_spending_by_age.plot(kind="bar")
plt.xlabel("Age")
plt.ylabel("Average Spending")
plt.title("Average Spending by Age")
plt.show()

