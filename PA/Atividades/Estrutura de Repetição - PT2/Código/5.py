num, sum, count = 0, 0, 0

while True:
    try:
        num = int(input("Digite um número inteiro positivo: "))
        if num < 0:
            print(f"-" * 30)
            print("Programa encerrado.")
            break
        sum += num
        count += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"-" * 30)
print(f"A média dos números digitados é: {sum / count:.2f}")
