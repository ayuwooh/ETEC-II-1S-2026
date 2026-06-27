nums = []
count = 0
first_batch, second_batch,third_batch = 0, 0, 0

while count < 10:
    try:
        num = int(input(f"Qual o {count + 1} valor? "))
    except ValueError:
        print("Este não é um valor válido, tente de novo.")
        continue
    nums.append(num)
    count += 1

for i in nums:
    if i <= 20:
        first_batch += i
    elif i <= 30:
        second_batch += i
    else:
        third_batch += i

print("-" * 30)
print(f"Soma dos números até 20: {first_batch}")
print(f"Soma dos números maior do que 20 até 30: {second_batch}")
print(f"Soma dos números maiores que 30: {third_batch}")
