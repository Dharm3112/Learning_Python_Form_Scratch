from enum import unique

items = ["apple", "banana", "cherry","orange", "grape", "apple"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Print Duplicate Item", item);
        break
    unique_items.add(item)
