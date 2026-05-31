count, age = 0
avgage = 0.0

for count in range(1, 21):
    age = int(input(f"Digite a idade da {count}º pessoa: "))
    avgage += age

avgage = avgage / 20

print("-" * 30)
print(f"Média de idade das pessoas: {avgage:.2f}")
