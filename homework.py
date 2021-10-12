'''months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
bills = [int(input(f'{month}: ')) for month in months]
maxscore = 0
for i in range(12):
    if bills[i] > maxscore:
        maxscore = bills[i]

print(f'{months[bills.index(maxscore)]}: {maxscore}')'''


n = 0
while n < 5 or n > 20:
    n = int(input("enter the number of temperatures: "))
temps = []
for i in range(n):
    temps.append(int(input("enter temperature: ")))
#temps = [int(input("enter temperature: ")) for i in range(n)]
print(sum(temps)/len(temps))