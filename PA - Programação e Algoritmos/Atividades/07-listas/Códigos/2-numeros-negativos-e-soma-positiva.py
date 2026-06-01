nums = []
count, nqty = 0, 0
num, sum = 0.0, 0.0

while count < 20:
    try:
        num = float(input(f"Qual o {count + 1} valor? "))
    except ValueError:
        print("Este não é um valor válido, tente de novo.")
        continue
    nums.append(num)
    count += 1

for num in nums:
    if num < 0:
        nqty += 1
    elif num > 0:
        sum += num

print("-" * 30)
print(f"Quantidade de números negativos: {nqty}")
print(f"Soma de números positivos: {sum}")
