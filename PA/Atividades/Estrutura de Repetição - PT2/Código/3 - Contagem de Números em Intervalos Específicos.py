count, num, biggerthan10, lessthan5, btwn7n15 = 0, 0, 0, 0, 0

for count in range (1, 10):
    try:
        num = int(input(f"Digite o {count + 1}º número: "))
        count += 1
        if num > 10:
            biggerthan10 += 1
        if num < 5:
            lessthan5 += 1
        if num >= 7 and num <= 15:
            btwn7n15 += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"-" * 30)
print(f"Números maiores que 10: {biggerthan10}")
print(f"Números menores que 5: {lessthan5}")
print(f"Números entre 7 e 15: {btwn7n15}")