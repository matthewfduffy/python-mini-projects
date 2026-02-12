import os

path_to_folder = "/home/md5/Code/coding-challenges-python/_Common_Snippets/files"

for filename in os.listdir(path_to_folder):
    # output list to terminal
    # print(filename)

    # creates a new file or raises an error if file already exists
    try:
        with open("file.txt", "x") as f:
            f.write("Created using exclusive mode.")
    except FileExistsError:
        print("Target file already exists.")
