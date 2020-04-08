'''
Deque in Python
'''

from collections import deque

queue = deque()

# appends element at the end
queue.append(1)
queue.append(5)
queue.append(13)
queue.append(8)
queue.append(9)
queue.append(4)


print(queue)

# Removes element from front (left end of queue)
queue.popleft()

# Queue after removing item from front
print(queue)

# rotate by x elements. -ve argument implies left rotation.
queue.rotate(-3)

print(queue)

