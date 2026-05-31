num, count, sum = 0, 0, 0
avg = 0.0

for count in range(1, 16):
    try:
        num = int(input(f"Digite o {count}º número: "))
        sum += num
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

avg = sum / 15

print("-" * 30)
print(f"A soma dos números digitados é: {sum}")
print(f"A média dos números digitados é: {avg}")
