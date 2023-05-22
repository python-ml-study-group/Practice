my_list=["Sunday","Monday","Tuesday","Wednesday"]
stack=[]
print(my_list)

for i in range(0,len(my_list)):
    stack.append(my_list[i])
    print(stack)
for i in range(0,len(stack)):
    stack.pop()
    print(stack)