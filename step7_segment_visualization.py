# ==============================
# IntelliMarket AI
# Step 7: Segment Visualization
# ==============================

import pandas as pd
import matplotlib.pyplot as plt

# Load segmented dataset (IMPORTANT)
df = pd.read_csv("customers_segmented.csv")

print(df.columns)  # check columns once

# Scatter plot for customer segments
plt.figure()
plt.scatter(
    df["income"],
    df["spending"],
    c=df["Segment"]
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation Visualization")

plt.savefig("customer_segments.png")
plt.show()
