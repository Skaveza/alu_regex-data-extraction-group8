#!/usr/bin/python3
import re
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py path_to_file")
    sys.exit(1)

# regex patterns
email = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
restau = r"[A-Za-z0-9\s'&.,-]+ - [A-Za-z0-9\s'&.,-]+"
rgb = "AA"
ingredient = "AA"
user_name = r"\b@[a-zA-Z]{1,}\b"
product_code = r"\b[A-Z]{3}+[0-9]{3}\b"
headline = r"\b[A-Z]{1}[a-z]{1,}:+\s+[A-Z]{1}[a-z]{1,}\b"
date = "AA"
regex = [email, restau, rgb, ingredient, user_name, product_code, headline, date]

# names, for formatting purpose
names = ['Email', 'Restaurant', 'RGB()', 'Ingredient', 'User Name', 'Product Code', 'Headline', 'Date']
my_list = [[] for i in range(len(regex))]

# generators for lines in file
def generate_line():
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        for line in file:
            yield line


lines = generate_line()

for line in lines:
    for i, rg in enumerate(regex):
        my_list[i] += re.findall(rg, line)

for i, output in enumerate(my_list):
    if output == []:
        print(f"No correspondance for {names[i]}\n")
    else:
        print(f"CORRESPONDANCE FOUND FOR {names[i]}: {output}\n")