import os

# rename all .txt extension files in a directory
directory = "./example_folder"

for count, filename in enumerate(os.listdir(directory)):
    if filename.endswith(".txt"):
        new_name = f"file_{count + 1}.txt"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

        print(f"Renamed {filename} to (new_name)")