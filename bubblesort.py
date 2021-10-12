# bubblesort.py
lists = [int(x) for x in input("What numbers would you like to sort: ").split()]
passes = 0

while True:
    passes += 1
    count = 0
    for i in range(len(lists) - 1):
        if lists[i] > lists[i + 1]:
            lists[i], lists[i + 1] = lists[i + 1], lists[i]
            count += 1
    if count == 0: break
print(lists)
