#defined a recursive function
def rec_fun(inp,value):

    count=0
    #checks if the input is a dictionary
    if isinstance(inp,dict):
        #loops through the values and compares with the specified value
        for key in inp:
            #increments the count if the value matches with the specified value
            count=count+rec_fun(inp[key],value)

    #checks if the value of the dictionary is a list        
    elif isinstance(inp,list):
        #loops through all the elements of the list 
        for key in inp:
            #increments the count if the value matches with the specified value
            count=count+rec_fun(key,value)


    else:
        #implements for values that are not dictionary and list
        if inp==value:
            count+=1

    return count

data = {
    'key1': [1, 2, 3],
    'key2': {
        'key3': [4, 5, 6],
        'key4': [7, 8, 9]
    },
    'key5': 10
}

value = 5
occurrences = rec_fun(data, value)
print(f"The value {value} occurs {occurrences} times.")        
