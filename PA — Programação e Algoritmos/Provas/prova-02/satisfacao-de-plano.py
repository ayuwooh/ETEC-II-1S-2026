count, satisfaction, age, age_sum = 0, 0, 0, 0
great, good, bad = 0, 0, 0
age_avg = 0.0

for count in range(1,21):

    print("-" * 30)
    print(f"Graus de satisfação")
    print(f"1 - Ótimo | 2 - Bom | 3 - Ruim")
    print("-" * 30)

    try:
        satisfaction = int(input("Digite seu grau de satisfação: "))
    except ValueError:
        print("Este não é um valor válido.")
        continue

    if satisfaction not in range(1,4):
        print("Este não é um valor válido.")
        continue
    elif satisfaction == 1:
        great += 1
    elif satisfaction == 2:
        good += 1
    elif satisfaction == 3:
        bad += 1

    try:
        age = int(input("Digite sua idade: "))
    except ValueError:
        print("Este não é um valor válido.")
        continue
    
    age_sum += age

age_avg = age_sum / 20

print("-" * 30)
print("Avaliações:")
print(f"Ótimo: {great}")
print(f"Bom: {good}")
print(f"Ruim: {bad}")
print("-" * 15)
print(f"Idade média: {age_avg}")
print("-" * 15)