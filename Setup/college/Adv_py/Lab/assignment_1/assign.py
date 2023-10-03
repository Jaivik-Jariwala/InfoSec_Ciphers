'''#Assignment 1: Product Review from text file

Consider a scenario where you are working as a data scientist for a large e-commerce company. Your
team is responsible for analyzing customer feedback data, which is stored in multiple text files. Each
text file contains customer reviews for different product categories. Your task is to write a Python
script that performs the following operations:

Read the contents of all the text files in a given directory.
For each review, extract the following information:
 Customer ID (a 6-digit alphanumeric code)
 Product ID (a 10-digit alphanumeric code)
 Review date (in the format "YYYY-MM-DD")
 Review rating (an integer between 1 and 5)
 Review text (the actual feedback provided by the customer)
Calculate the average review rating for each product and store it in a dictionary where the product ID
is the key and the average rating is the value.
Determine the top 3 products with the highest average review ratings.

Create a new text file named "summary.txt" and write the following information into it:
 The total number of reviews processed.
 The total number of valid reviews (reviews with all required information extracted
successfully).
 The total number of invalid reviews (reviews with missing or incorrect information).
 The product ID and average rating of the top 3 products with the highest average ratings.

Your Python script should be robust, handling any potential errors or exceptions during the file
handling process. Additionally, you should implement efficient algorithms to handle large volumes of
data without consuming excessive memory or processing time.

Write the Python script to achieve the above objectives and provide detailed comments explaining
each step of your implementation.'''
'''----------------------------------------------------------'''

# 1st iteration 

'''
#importing Dependencies
import os

# Function to extract review from reveiw files
def extract(review):
    cust_id = review[0].split(":")[1].strip()
    prod_id = review[1].split(":")[1].strip()
    re_date = review[2].split(":")[1].strip()
    re_rate = review[3].split(":")[1].strip()
    return cust_id, prod_id, re_date,re_rate

# Function to read and extract review information
def review(file_path):
    with open(file_path, "r") as fr:
        lines = fr.readlines()
        if len(lines) >= 4:
            return review(lines[:4])
        return None
    
# Function to process reviews in a directory
def process_reviews(directory):
    total_reviews = 0
    valid_reviews = 0
    invalid_reviews = 0
    prod_rate = {}

    # Process each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            review_info = review(os.path.join(directory, filename))
            if review_info:
                cust_id, prod_id, _, re_rate = review_info
                
                # Update product ratings
                if prod_id in prod_rate:
                    prod_rate[prod_id].append(re_rate)
                else:
                    prod_rate[prod_id] = [re_rate]

                valid_reviews += 1
            else:
                invalid_reviews += 1

            total_reviews += 1

        return total_reviews, valid_reviews, invalid_reviews , prod_rate
    
# Function to calculate Average rating for products
def calculate(prod_rate):
    return{prod_id: sum(ratings) / len(ratings) for prod_id, ratings in prod_rate.items()}

# determine top 3 
def determine_top3(avg_rate):
    return sorted(avg_rate.items(), key=lambda item: item[1], reverse=True)[:3]

# Function to write summary information to a file
def write_summary(total_reviews, valid_reviews, invalid_reviews, top_products):
    with open("summary.txt", "w") as summary_file:
        summary_file.write("Total Reviews Processed: {}\n".format(total_reviews))
        summary_file.write("Total Valid Reviews: {}\n".format(valid_reviews))
        summary_file.write("Total Invalid Reviews: {}\n".format(invalid_reviews))
        summary_file.write("\nTop 3 Products with Highest Average Ratings:\n")
        for product_id, avg_rating in top_products:
            summary_file.write("Product ID: {}, Average Rating: {}\n".format(prod_id, avg_rate))

# Specify the directory containing review files
reviews_directory = "/path/to/reviews"


# Call the functions to process reviews and generate summary
total, valid, invalid, ratings = process_reviews(reviews_directory)
average_ratings = calculate_average_ratings(ratings)
top_products = determine_top_products(average_ratings)
write_summary(total, valid, invalid, top_products)
'''


# 2nd iteration 

'''added txt_gen.py for text file generation 
optimised and Debug the error 2,3,4
added file output function'''

import os

# Function to extract review from review files
def extract(review_lines):
    cust_id = review_lines[0].split(":")[1].strip()
    prod_id = review_lines[1].split(":")[1].strip()
    re_date = review_lines[2].split(":")[1].strip()
    re_rate = review_lines[3].split(":")[1].strip()
    return cust_id, prod_id, re_date, re_rate

# Function to read and extract review information
def read_review(file_path):
    with open(file_path, "r") as fr:
        lines = fr.readlines()
        if len(lines) >= 4:
            return extract(lines[:4])
        return None

# Function to process reviews in a directory
def process_reviews(directory):
    total_reviews = 0
    valid_reviews = 0
    invalid_reviews = 0
    prod_rate = {}

    # Process each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            review_info = read_review(os.path.join(directory, filename))
            if review_info:
                cust_id, prod_id, re_rate = review_info
                # Convert re_rate to integer // error 4
                re_rate = int(re_rate)
                # Update product ratings // error 3
                if prod_id in prod_rate:
                    prod_rate[prod_id].append(re_rate)
                else:
                    prod_rate[prod_id] = [re_rate]
                valid_reviews += 1
            else:
                invalid_reviews += 1
    return total_reviews, valid_reviews, invalid_reviews , prod_rate

# Function to calculate Average rating for products
def calculate(prod_rate):
    return{prod_id: sum(ratings) / len(ratings) for prod_id, ratings in prod_rate.items()}

# determine top 3 
def determine_top3(avg_rate):
    return sorted(avg_rate.items(), key=lambda item: item[1], reverse=True)[:3]

# Function to write summary information to a file
def write_summary(total_reviews, valid_reviews, invalid_reviews, top_products):
    with open("summary.txt", "w") as summary_file:
        summary_file.write("Total Reviews Processed: {}\n".format(total_reviews))
        summary_file.write("Total Valid Reviews: {}\n".format(valid_reviews))
        summary_file.write("Total Invalid Reviews: {}\n".format(invalid_reviews))
        summary_file.write("\nTop 3 Products with Highest Average Ratings:\n")
        for product_id, avg_rating in top_products:
            summary_file.write("Product ID: {}, Average Rating: {}\n".format(product_id, avg_rating))

# Specify the directory containing review files
reviews_directory = "/home/jaivikjariwala/Desktop/Advanced_py/test_reviews"

# Call the functions to process reviews and generate summary
total, valid, invalid, ratings = process_reviews(reviews_directory)
average_ratings = calculate(ratings)
top_products = determine_top3(average_ratings)
write_summary(total, valid, invalid, top_products)

# Function to create an output text file and display outputs
def create_output_file(total_reviews, valid_reviews, invalid_reviews, top_products, average_ratings):
    with open("output.txt", "w") as output_file:
        output_file.write("Total Reviews Processed: {}\n".format(total_reviews))
        output_file.write("Total Valid Reviews: {}\n".format(valid_reviews))
        output_file.write("Total Invalid Reviews: {}\n".format(invalid_reviews))
        output_file.write("\nTop 3 Products with Highest Average Ratings:\n")
        for product_id, avg_rating in top_products:
            output_file.write("Product ID: {}, Average Rating: {}\n".format(product_id, avg_rating))        
        output_file.write("\nAverage Ratings for All Products:\n")
        for product_id, avg_rating in average_ratings.items():
            output_file.write("Product ID: {}, Average Rating: {}\n".format(product_id, avg_rating))

    # Display outputs on the console
    print("Total Reviews Processed:", total_reviews)
    print("Total Valid Reviews:", valid_reviews)
    print("Total Invalid Reviews:", invalid_reviews)
    print("\nTop 3 Products with Highest Average Ratings:")
    for product_id, avg_rating in top_products:
        print("Product ID:", product_id, "Average Rating:", avg_rating)
    
    print("\nAverage Ratings for All Products:")
    for product_id, avg_rating in average_ratings.items():
        print("Product ID:", product_id, "Average Rating:", avg_rating)

# Call the functions to process reviews and generate summary
total, valid, invalid, ratings = process_reviews(reviews_directory)
average_ratings = calculate(ratings)
top_products = determine_top3(average_ratings)

# Call the function to create the output text file and display outputs
create_output_file(total, valid, invalid, top_products, average_ratings)
