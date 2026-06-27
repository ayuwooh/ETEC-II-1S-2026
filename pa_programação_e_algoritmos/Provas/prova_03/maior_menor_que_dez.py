nums = []
i = 0
for i in range(0, 20):
    nums.append(int(input(f"Digite o {i+1} número: ")))

j = 0
bignums = 0
lownums = 0
for j in range(0, 20):
    if nums[j] >= 10:
        bignums += 1
    else:
        lownums += 1

print(f"Números maiores ou igual a 10: {bignums}")
print(f"Números menores que 10: {lownums}")
