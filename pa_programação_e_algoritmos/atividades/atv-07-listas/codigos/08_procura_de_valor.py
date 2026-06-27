import random

nums = [random.randint(1, 50) for _ in range(20)]
num = 0

while True:
    try:
        num = int(input("Qual o número que deseja procurar? "))
        break
    except ValueError:
        print("Este não é um valor válido, tente de novo.")

if num in nums:
    print(f"O número {num} está presente na lista.")
else:
    print(f"O número {num} não está presente na lista.")

print(nums)
