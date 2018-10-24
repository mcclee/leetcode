i= [1, 2, 3, 4, 3, 4, 5,3 ,3 ]
from collections import deque
import time
q = time.time()
for j in range(100000):
    w = deque(i)
t = time.time()
print(t - q)