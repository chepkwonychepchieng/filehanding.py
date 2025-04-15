# File Handling in Python
input_filename = input("Enter the input filename: ")
file = open(input_filename, "r")
data = file.read()
print(data)


file = open(input_filename, "w")
data = file.write("This is a new line of text.\n")

file = open(input_filename, "r")
data = file.read()
print(data)

