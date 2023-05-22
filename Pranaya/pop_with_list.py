#What are the types used to implement Stacks and queues in Python? What happens if you use Pop()function with a list?
#Pop() can be used to implement stacks in python as it will remove the las element by default just as Stack which follows LIFO.

stack = [1, 2, 3, 4, 5]

# Remove and return the top element of the stack
top_element = stack.pop()
#If we use Pop() with a list, it removes last element from the list if index isn’t specified.
print( top_element)  # Output: 5
print(stack)  # Output: [1, 2, 3, 4]

queue = [4,3,2]
#Queue follows FIFO(First In First Out) . Pop(0) can be used to implement queues in python.
x = queue.pop(0)
print(queue)

