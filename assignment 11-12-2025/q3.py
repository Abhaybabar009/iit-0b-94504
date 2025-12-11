import csv

# Read CSV file
filename = "products.csv"

products = []   # to store all rows

with open(filename, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append(row)

# a) Already read above

# b) Print each row in clean format
print("\n--- Product Details ---")
for p in products:
    print(f"ID: {p['ProductID']}, Name: {p['Name']}, Category: {p['Category']}, "
          f"Price: {p['Price']}, Quantity: {p['Quantity']}")

# c) Total number of rows
total_rows = len(products)
print("\nTotal number of rows:", total_rows)

# d) Total number of products priced above 500
count_above_500 = sum(1 for p in products if float(p['Price']) > 500)
print("Products priced above 500:", count_above_500)

# e) Average price of all products
average_price = sum(float(p['Price']) for p in products) / total_rows
print("Average price of products:", average_price)

# f) List all products from a specific category (user input)
user_category = input("\Enter category to filter: ")

print(f"\nProducts in category '{user_category}':")
for p in products:
    if p['Category'].lower() == user_category.lower():
        print(p['Name'], "-", p['Price'])

# g) Total quantity of all items
total_quantity = sum(int(p['Quantity']) for p in products)
print("\nTotal quantity of all items in stock:", total_quantity)
