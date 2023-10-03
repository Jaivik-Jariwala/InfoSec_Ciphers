import os
import csv

# Function to read the product names mapping from "product_names.csv"
def read_product_mapping(filename):
    product_mapping = {}
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_mapping[row["Product ID"]] = row["Product Name"]
    return product_mapping

# Initialize a dictionary to store total sales for each product
product_sales = {}

# Directory containing the CSV files
data_directory = "sales_data"

# Read the product names mapping
product_mapping = read_product_mapping("product_names.csv")

# Traverse the directory and its subdirectories to process CSV files
for root, _, files in os.walk(data_directory):
    for file in files:
        if file.endswith(".csv"):
            filepath = os.path.join(root, file)
            with open(filepath, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product_id = row["Product ID"]
                    quantity_sold = int(row["Quantity sold"])
                    if product_id in product_sales:
                        product_sales[product_id] += quantity_sold
                    else:
                        product_sales[product_id] = quantity_sold

# Sort products by total quantity sold in descending order
sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

# Get the top 5 best-selling products
top_5_products = sorted_products[:5]

# Create a new CSV file "sales_summary.csv" and write the summary
with open("sales_summary.csv", "w", newline="") as csvfile:
    fieldnames = ["Product ID", "Product Name", "Total Quantity Sold", "Average Quantity Sold per Month"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    for product_id, total_quantity_sold in top_5_products:
        product_name = product_mapping.get(product_id, "Unknown")
        average_quantity_sold = total_quantity_sold / len(files)  # Assuming each file represents a month
        writer.writerow({
            "Product ID": product_id,
            "Product Name": product_name,
            "Total Quantity Sold": total_quantity_sold,
            "Average Quantity Sold per Month": average_quantity_sold
        })

print("Sales summary has been written to 'sales_summary.csv'")
