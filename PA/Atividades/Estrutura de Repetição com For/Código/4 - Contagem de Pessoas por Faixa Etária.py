pegi1, pegi2, pegi3, pegi4, pegi5 = 0.0, 0.0, 0.0, 0.0, 0.0
count, age = 0, 0

for count in range (1, 16):
    age = int (input(f"Digite a idade da {count}º pessoa: "))
    if age in range (0, 16):
        pegi1 += 1
    elif age in range (16, 31):
        pegi2 += 1
    elif age in range (31, 46):
        pegi3 += 1
    elif age in range (46, 61):
        pegi4 += 1
    else:
        pegi5 += 1
        
print(f"-" * 30)
print(f"Quantidade de pessoas por faixa etária:")
print(f"Até 15 anos: {pegi1}")
print(f"16 a 30: {pegi2}")
print(f"31 a 45: {pegi3}")
print(f"46 a 60: {pegi4}")
print(f"Acima de 61: {pegi5}")
print(f"")

pegi1 = pegi1 / 15
pegi5 = pegi5 / 15

print(f"Quantia de pessoas até 15 anos:      {pegi1:.2%}")
print(f"Quantia de pessoas acima de 60 anos: {pegi5:.2%}")