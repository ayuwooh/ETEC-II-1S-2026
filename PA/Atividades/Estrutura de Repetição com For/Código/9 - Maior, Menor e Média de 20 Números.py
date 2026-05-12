count, num, sum, biggest, smallest = 0, 0, 0, 0, 0
avg = 0.0

for count in range (1, 21):
    num = int (input(f"Digite o {count}º número: "))
    sum += num
    if smallest == 0 or num < smallest:
        smallest = num
    elif num > biggest:
        biggest = num

avg = sum / 20

print(f"-" * 30)
print(f"Maior número: {biggest}")
print(f"Menor número: {smallest}")
print(f"Média dos números: {avg:.2f}")