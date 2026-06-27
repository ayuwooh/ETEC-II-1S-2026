matrix = []
count_greater = 0
i, j = 0, 0

for i in range(3):
    row = []
    for j in range(3):
        while True:
            try:
                num = int(input(f"Qual o valor para posição [{i}][{j}]? "))
                break
            except ValueError:
                print("Este não é um valor válido, tente de novo.")
        row.append(num)
    matrix.append(row)

for row in matrix:
    for num in row:
        if num > 10:
            count_greater += 1

print("-" * 30)

for row in matrix:
    print(row)

print(f"Quantidade de números maiores que 10: {count_greater}")
