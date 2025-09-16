import csv

data = [
    ["Item", "Quantity", "Price"],
    ["PC", 100, 25.50],
    ["Keyboard", 200, 45.00],
]

with open("new.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
