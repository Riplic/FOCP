# Open the file in read mode
file_path = "info.txt"

try:
    with open(file_path, 'r') as file:
        # Read and print the contents of the file
        file_contents = file.read()
        print(file_contents)

except FileNotFoundError:
    print(f"The file {file_path} was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
