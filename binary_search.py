numbers = sorted([int(x) for x in input("enter numbers: ").split()])
find_num = int(input())
for i in range(len(numbers)):
    half_num = (len(numbers) - 1) // 2
    print(numbers, len(numbers))
    if numbers[half_num] == find_num:
        print("found", numbers[half_num])
        break
    elif find_num < numbers[half_num]:
        del numbers[half_num:]
    else:
        del numbers[:half_num + 1]
