# Write mode: Creates a new file or truncates an existing file
with open("file.txt", "w") as f:
    f.write("Created using write mode.")

f = open("file.txt","r")
print(f.read())

# Append mode: Creates a new file or appends to an existing file
with open("file.txt", "a") as f:
    f.write("Content appended to the file.")

f = open("file.txt","r")
print(f.read())

# Exclusive creation mode: Creates a new file, raises error if file exists
try:
    with open("file.txt", "x") as f:
        f.write("Created using exclusive mode.")
except FileExistsError:
    print("Already exists.")
