# ==============================
# IntelliMarket AI
# Step 3: CSV File Handling
# ==============================

import csv

# Open CSV file
with open("customers.csv", mode="r") as file:
    reader = csv.DictReader(file)

    print("Customer Data from CSV")
    print("----------------------")

    for row in reader:
        print(row)
