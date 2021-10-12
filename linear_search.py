from random import randint
import math
from functools import lru_cache

# Linear search
num = randint(1, 100)
print("Original number:", num)
for i, nums in enumerate(range(1, 1001), 1): 
    if nums == num: 
        print("Linear search:", i)
        break

# Binary search
@lru_cache(maxsize=1000)
def search(count_num = 100, counter = 0, diff = 0):
    print(count_num)
    diff = count_num - search()
    counter += 1
    if count_num == num:
        return counter
    elif count_num > num:
        return search(math.ceil(count_num / 2))
    elif count_num < num:
        return search(math.floor(count_num * (150/100)))

search()
# print("Binary search:", search())
