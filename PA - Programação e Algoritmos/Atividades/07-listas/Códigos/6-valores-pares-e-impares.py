nums = []
count = 0
num = 0
even, odd = 0, 0
i = 0

while count < 20:
    try:
        num = int(input(f"Qual o {count + 1} valor? "))
    except ValueError:
        print("Este não é um valor válido, tente de novo.")
        continue
    nums.append(num)
    count += 1

for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("-" * 30)
print(f"Quantidade de números pares: {even}")
print(f"Quantidade de números ímpares: {odd}")
