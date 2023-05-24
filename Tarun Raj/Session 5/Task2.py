def remove_duplicates(strings):
    seen = set()
    subset = []
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in seen:
            seen.add(sorted_string)
            subset.append(string)
    return subset

#list of strings
input_list = ['def', 'fed', 'his', 'her', 'ehr', 'dog']
result = remove_duplicates(input_list)
print(result)
