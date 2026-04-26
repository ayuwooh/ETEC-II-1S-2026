nums,value,lowest=[],0,0

for i in range(1,6):
    value=int(input(f"Qual o {len(nums)+1}º valor? "))
    nums.append(value)
    if len(nums)==5:
        break
lowest=nums[0]
for n in nums:
    if n < lowest:
        lowest = n
print(f"O menor número é {lowest}!")
