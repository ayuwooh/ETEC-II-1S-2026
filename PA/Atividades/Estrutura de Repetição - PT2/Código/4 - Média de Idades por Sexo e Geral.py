count, age, sex = 0, 0, 0
allavg, maleavg, femavg = 0.0, 0.0, 0.0

for count in range (1, 13):
    try:
        age = int(input(f"Digite a idade da {count + 1}ª pessoa: "))
        sex = int(
            input(f"Digite o sexo da pessoa (1 para masculino, 2 para feminino): ")
        )
        if sex == 1:
            maleavg += age
        elif sex == 2:
            femavg += age
        allavg += age
        count += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"-" * 30)
print(f"A média das idades é: {allavg / 12:.2f}")
print(f"A média das idades dos homens é: {maleavg / 12:.2f}")
print(f"A média das idades das mulheres é: {femavg / 12:.2f}")
