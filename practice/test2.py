marks = [90, 35, 67, 80, 80, 79]
print ("marks: ", marks)
print ("sum: ", sum(marks))
print ("count: ", len(marks))
average = sum(marks)/len(marks)
print ("average: ", average)

# Grading based on average
if min(marks) < 35:
    print ("Failed")
else:
    if average >= 90:
        print ("A")
    elif average >= 80:
        print ("B")
    elif average >= 70:
        print ("C")
    else:
        print ("F")

