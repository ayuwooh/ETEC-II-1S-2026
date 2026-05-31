height, shortmale, tallfemale = 0.0, 0.0, 0.0
count, sex = 0, 0

for count in range (1, 21):
    height = float (input(f"Digite a altura da {count}º pessoa: "))
    sex = int (input(f"Digite o sexo da pessoa (1 - Feminino, 2 - Masculino): "))
    if sex == 1 and height > tallfemale:
        tallfemale = height
    elif sex == 2 and shortmale == 0.0 or height < shortmale:
        shortmale = height

print(f"-" * 30)
print(f"Mulher mais alta: {tallfemale:.2f}m")
print(f"Homem mais baixo: {shortmale:.2f}m")