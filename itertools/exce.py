a = 2
b = 1
try:
    result = a/b
    with open("con", "w") as file:
        file.write("Result: " + str(result))
except ZeroDivisionError as e:
    print ("Divide by zero error, update the parameters properly")
except FileNotFoundError as e:
    print ("File not found, check the file path")
except Exception as e:
    print ("There is some other issue")


try:
    bring 100 pages ruled notebook.
except 100pages_is_not_there:
    bring 200 pages ruled notebook.
except ruled_is_not_there:
    bring 200 pages unruled notebook.
except notebook_is_not_there:
    come back home.
except:
    come back home.
