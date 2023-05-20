import os

# Create a new folder called "code"
newfolder = "code"
os.mkdir(newfolder)

# Create the subfolders "p1" and "p2"
subfolders = ["p1", "p2"]
for folder in subfolders:
    folder_path = os.path.join(newfolder, folder)
    os.mkdir(folder_path)

# Create a text file called "a.py" and add content "hello world" under "p1"
file_path = os.path.join(newfolder, "p1", "a.py")
with open(file_path, "w") as file:
    file.write("hello world")

