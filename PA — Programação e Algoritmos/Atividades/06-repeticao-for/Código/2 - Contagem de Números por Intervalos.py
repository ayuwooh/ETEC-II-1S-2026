range1, range2, range3, range4 = 0, 0, 0, 0
count, num = 0, 0

for count in range (1, 21):
    num = int (input(f"Digite o {count}º número: "))
    if num in range (0, 26):
        range1 += 1
    elif num in range (26, 51):
        range2 += 1
    elif num in range (51, 76):
        range3 += 1
    elif num in range (76, 100):
        range4 += 1

print(f"-" * 30)
print(f"Quantidade de números por intervalos:")
print(f"0-25: {range1}")
print(f"26-50: {range2}")
print(f"51-75: {range3}")
print(f"76-100: {range4}")