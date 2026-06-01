nums = []
num, avg = 0.0, 0.0
count = 0
sum = 0

while count < 20:
    try:
        num = float(input(f"Qual o {count + 1} valor? "))
    except ValueError:
        print("Este não é um valor válido, tente de novo.")
        continue
    nums.append(num)
    count += 1

for i in nums:
    sum += i

avg = sum / count

print("-" * 30)
print(f"Média dos números: {avg:.2f}")
print("-" * 30)

for i in nums:
    if i > avg:
        print(f"{i} está acima da média.")