age, agesum, count, heavy = 0, 0, 0, 0
weight, avgage = 0.0, 0.0

for count in range (1,11):
    try:
        age = int(input(f"Digite a idade da {count + 1}ª pessoa: "))
        weight = float(input(f"Digite o peso da pessoa (em kg): "))
        count += 1
        agesum += age
        avgage = agesum / 10
        if weight > 80:
            heavy += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

print(f"-" * 30)
print(f"O número de pessoas com peso superior a 80 kg é: {heavy}")
print(f"A média das idades é: {avgage:.2f}")
