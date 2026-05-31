matrix = []
rows = 3
count_one, count_two, num = 0, 0, 0

for count_one in range(rows):
    row = []
    while count_two < 3:
        try:
            num = int(input(f"Qual o {count_two + 1} valor? "))
        except ValueError:
            print("Este não é um valor válido, tente de novo.")
            continue
        row.append(num)
        count_two += 1
rows.append[row]
matrix.append[row]

print(matrix)
