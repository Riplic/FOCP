file_path = "info.txt"

try:
    # Open the file in append mode
    with open(file_path, 'a') as file:
        # Write an extra line of text
        file.write("This is an extra line.\n")

except FileNotFoundError:
    print(f"The file {file_path} was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
