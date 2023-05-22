#Task 3
#Shallow copy 
List1=[1,2,3,4]
List2=List1.copy()
print(List2)
List2[1]=100
print(List2)
print(List1)

#Deep copy
import copy 
List1=[[1,2,3,4],[4,5,6,7],[8,9,10,11]]
List2=copy.deepcopy(List1)
print(List2)
List2[1][0]=100
print(List2)
print(List1)