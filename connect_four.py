rows = 6
columns = 7
inputs = ['-' for _ in range(rows*columns)]
counter = 0
grid = '\n'.join(["{} " * columns for i in range(rows)])
def checker():
    for i in range(3):
        if inputs[i * 3] == inputs[(i * 3) + 1] == inputs[(i * 3)+ 2] and inputs[i * 3] != '-': return f"{inputs[i * 3]} wins!"
        elif inputs[i] == inputs[i+3] == inputs[i+6] and inputs[i] != '-': return f"{inputs[i]} wins!"
        elif inputs[0] == inputs[4] == inputs[8] and inputs[0] != '-': return f"{inputs[0]} wins!"
        elif inputs[2] == inputs[4] == inputs[6] and inputs[2] != '-': return f"{inputs[2]} wins!"
while counter < 42:
    print(grid.format(*inputs))
    try:
        answer = int(input("Enter the square you want(1-42): "))
    except ValueError:
        print("Sorry but that is not a valid square\n")
        continue

    if answer < 1 or answer > 42 or inputs[answer - 1] != '-': 
        print("Sorry but that is not a valid square\n")
        continue
    
    inputs[answer - 1] = 'x' if counter % 2 == 0 else 'o'
    if checker():
        print(checker())
        break
    if counter == 41: print("It's a draw :(")
    counter += 1
