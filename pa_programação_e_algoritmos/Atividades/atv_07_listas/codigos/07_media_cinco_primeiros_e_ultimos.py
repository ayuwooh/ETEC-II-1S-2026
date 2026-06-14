nums = []
count = 0
num = 0
sum_one, sum_two = 0, 0
avg_one, avg_two = 0.0, 0.0

while count < 10:
    try:
        num = int(input(f"Qual o {count + 1} valor? "))
    except ValueError:
        print("Este não é um valor válido, tente de novo.")
        continue
    nums.append(num)
    count += 1

sum_one = sum(nums[:5])
sum_two = sum(nums[5:])

avg_one = sum_one / 5
avg_two = sum_two / 5

print("-" * 30)
print(f"Média dos 5 primeiros números: {avg_one:.2f}")
print(f"Média dos 5 últimos números: {avg_two:.2f}")
