import os

# Create the main folder "code" if it doesn't exist
if not os.path.exists("code"):
    os.makedirs("code")

# Create the subfolders "python1" and "python2" inside the "code" folder
subfolders = ["python1", "python2"]
for folder in subfolders:
    folder_path = os.path.join("code", folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Create a text file "a.py" under the "python1" folder and add the content
file_path = os.path.join("code", "python1", "a.py")
content = "print('hello world!')"

with open(file_path, "w") as file:
    file.write(content)

print("Folder 'code', subfolders 'python1' and 'python2', and file 'a.py' have been created successfully!")

