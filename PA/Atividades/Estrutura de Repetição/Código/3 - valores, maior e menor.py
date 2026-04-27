num, count, lowest, highest = 0, 0, 0, 0

while count < 15:
    count += 1
    num = int(input(f"Qual o {count}º valor? "))
    if count == 1:
        lowest = num
        highest = num
    elif num > highest:
        highest = num
    elif num < lowest:
        lowest = num

print(f"O menor valor é {lowest}!")
print(f"O maior valor é {highest}!")
