import sys

default_file_path = "automation/Find First name in a .txt file/test.txt"
file_path = input("Enter the text file path (press Enter to use the default path): ").strip()

if not file_path:
    file_path = default_file_path

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        first_name = input("Enter the first name to count: ").strip()
        lines = file.readlines()
        
        count = 0
        print("\nMatching lines:")
        for i, line in enumerate(lines, start=1):
            if line.split(',')[0].split()[0] == first_name:
                print(f"line {i}. {line.strip()}")
                count += 1

    print(f"\nThe first name '{first_name}' appears {count} times in the file.")

except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'.")
