# ==============================
# IntelliMarket AI
# Step 2: Customer List & Loop
# ==============================

# List of customers (dictionary inside list)
customers = [
    {"name": "Pramod", "age": 24, "income": 45000, "spending": 78},
    {"name": "Pranit", "age": 30, "income": 60000, "spending": 45},
    {"name": "Kiran", "age": 23, "income": 30000, "spending": 85},
    {"name": "Neha", "age": 22, "income": 52000, "spending": 60}
]

print("Customer Analysis")
print("------------------")

# Loop through customers
for customer in customers:
    print("\nName:", customer["name"])
    print("Age:", customer["age"])
    print("Income:", customer["income"])
    print("Spending Score:", customer["spending"])

    # Simple logic
    if customer["spending"] >= 70:
        print("Category: High Spender")
    else:
        print("Category: Low/Medium Spender")
