file_path = "info.txt"

try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read and display each line using a for...in loop
        for line in file:
            print(line.strip())  # Use strip() to remove trailing newline characters

except FileNotFoundError:
    print(f"The file {file_path} was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
