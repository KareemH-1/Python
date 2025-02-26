import sys

file_path = input("Enter the text file path: ")
first_name = input("Enter the first name to count: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        count = sum(1 for line in lines if line.split(',')[0].split()[0] == first_name)
    print(f"The first name '{first_name}' appears {count} times in the file.")
except FileNotFoundError:
    print("Error: File not found.")
