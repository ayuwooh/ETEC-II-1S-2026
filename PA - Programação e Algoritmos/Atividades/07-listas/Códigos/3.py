nums = []
count, num = 0, 0

while count < 10:
    try:
        num = int(input(f"Qual o {count+1} valor? "))
    except ValueError:
        print("Este não é um valor válido, tente de novo.") 
        continue
    nums.append(num)
    count += 1

max_num = nums[0]
pos = 0
index = 1

while index < len(nums):
    if nums[index] > max_num:
        max_num = nums[index]
        pos = index
    index += 1

print("-" * 30)
print(f"A posição do maior valor na lista é: {pos}")