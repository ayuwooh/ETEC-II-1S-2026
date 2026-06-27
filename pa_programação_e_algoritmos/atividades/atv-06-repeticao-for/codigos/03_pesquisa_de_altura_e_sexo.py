count, height, sex, women, tall, short = 0, 0, 0, 0, 0, 0
wsum, hsum = 0.0, 0.0

for count in range(1, 51):
    height = float(input(f"Digite a altura da {count}º pessoa: "))
    sex = int(input("Digite o sexo da pessoa: "))
    if tall == 0 or height > tall:
        tall = height
    elif short == 0 or height < short:
        short = height
    if sex == 2:
        women += 1
        wsum += height
    hsum += height

wsum = wsum / women
hsum = hsum / 50

print("-" * 30)
print(f"Maior altura:                 {tall}")
print(f"Menor altura:                 {short}")
print(f"Média de altura das mulheres: {wsum:.2f}")
print(f"Média de altura da turma:     {hsum:.2f}")
