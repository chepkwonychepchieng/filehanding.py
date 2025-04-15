fileName =input("Enter the file name: ")
try:
        file = open(fileName, "r")
        data = file.read()
        print(data)
except NameError:
    print("Error: The file name is not defined.")
except FileNotFoundError:
    print(f"Error: The file '{fileName}' was not found.")
# finally:
#     print("Execution completed.")