from cs50 import get_float

# Prompt user for input

while True:
    total = get_float("Change: ")
    if total >= 0:
        break

# Round to 100 and create change variables

total = round(total * 100)
print(total, f'This converts to {total:.2f}')

count = 0

# Increase coin count and subract total while true

while 25 <= total:
    count += 1
    total = total - 25

while 10 <= total:
    count += 1
    total = total - 10

while 5 <= total:
    count += 1
    total = total - 5

while 1 <= total:
    count += 1
    total = total - 1

# Return count to user

print(f"You will have {count} coins returned back")