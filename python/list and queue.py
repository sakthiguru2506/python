"""
stack and queue
stack
first in last out
queue
first in first out
"""
liststack=[3,2,1]
print(liststack)

liststack.append(5)
print(liststack)

liststack.append(6)
print(liststack)

liststack.pop()
print(liststack)

#list oueue
from collections import deque
queue=deque(["apple","orange","kiwi"])
print(queue)

queue.append("banana")
print(queue)

queue.popleft()
print(queue)
