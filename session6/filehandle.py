"""
#-------------------------------------------
f1 = open("C:/Projects/Practice-1/session6/example.txt", "r")
v1 = f1.read()
print(v1)
f1.close()
#-------------------------------------------
with open("C:/Projects/Practice-1/session6/example.txt", "r") as f2:
    v2 = f2.read()
    print(v2)
print (f2)
#-------------------------------------------

# Append 1 line 
with open ("C:/Projects/Practice-1/session6/example.txt", "a") as f1:
    f1.write("\n\n\none more line")

# Tell method to find where am I?
f1 = open("C:/Projects/Practice-1/session6/example.txt", "r")
print (f1.tell())
v1 = f1.readline()
print (f1.tell())
v1 = f1.readline()
print (f1.tell())


# seek method
with open("C:/Projects/Practice-1/session6/example.txt", "r") as f1:
    f1.seek(25)
    v1 = f1.readline()
    print (v1)
"""
with open ("C:/Projects/Practice-1/session6/example.txt", "r+") as f1:
    f1.seek(5)
    f1.write(".")
