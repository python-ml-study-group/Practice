def rec_fun(inp,value):
    count=0
    if isinstance(inp,dict):
        for key in inp:
            count=count+rec_fun(inp[key],value)
    elif isinstance(inp,list):
        for key in inp:
            count=count+rec_fun(key,value)


    else:
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
