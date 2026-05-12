count, age, adult = 0, 0, 0

for count in range (1, 21):
    age = int (input(f"Digite a idade da {count}º pessoa: "))
    if age >= 18:
        adult += 1

print(f"-" * 30)
print(f"Quantidade de pessoas maiores de idade: {adult}")