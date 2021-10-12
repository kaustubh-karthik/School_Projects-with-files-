import colorama
from colorama import Fore, Style
from os import system
from time import sleep
colorama.init(autoreset=True)

x = Fore.GREEN + Style.BRIGHT  + "x"
o = Fore.CYAN + Style.BRIGHT + "o"
empty = Style.RESET_ALL + "-"

rows = 3
columns = 3
inputs = [empty for _ in range(rows*columns)]
counter = 0
grid = '\n'.join(["{} " * columns for i in range(rows)])
def checker():
    for i in range(3):
        if inputs[i * 3] == inputs[(i * 3) + 1] == inputs[(i * 3)+ 2] and inputs[i * 3] != empty: return f"{inputs[i * 3]} wins!"
        elif inputs[i] == inputs[i+3] == inputs[i+6] and inputs[i] != empty: return f"{inputs[i]} wins!"
        elif inputs[0] == inputs[4] == inputs[8] and inputs[0] != empty: return f"{inputs[0]} wins!"
        elif inputs[2] == inputs[4] == inputs[6] and inputs[2] != empty: return f"{inputs[2]} wins!"

while counter < 9:
    system('clear')
    print(grid.format(*inputs))
    try:
        answer = int(input("Enter the square you want(1-9): "))
    except ValueError:
        system('clear')
        print("Sorry but that is not a valid square")
        sleep(1)
        continue

    if answer < 1 or answer > 9 or inputs[answer - 1] != empty: 
        system('clear')
        print("Sorry but that is not a valid square")
        sleep(1)
        continue
    
    inputs[answer - 1] = x if counter % 2 == 0 else o
    if checker():
        print(checker())
        break
    if counter == 8: print("It's a draw :(")
    counter += 1
