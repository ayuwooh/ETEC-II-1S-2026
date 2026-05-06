val, number, result = 0, 0, 0

val = int(input("Digite um número para ver sua tabuada: "))

print("-" * 30)

while number < 10:
    number += 1
    result = val * number
    print(f"{val}x{number}={result}")

print("-" * 30)
