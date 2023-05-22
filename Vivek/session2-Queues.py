my_list=["Sunday","Monday","Tuesday","Wednesday"]
queue=[]
print(my_list)

for i in range(0,len(my_list)):
    queue.append(my_list[i])
    print(queue)
for i in range(0,len(queue)):
    queue.pop(0)
    print(queue)