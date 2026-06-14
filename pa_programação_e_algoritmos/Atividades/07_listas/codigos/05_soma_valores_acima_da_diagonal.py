matrix = []
sum = 0
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

for i in range(3):
    for j in range(3):
        if j > i:
            sum += matrix[i][j]

print("-" * 30)
print(f"Soma dos números acima da diagonal principal: {sum}")
