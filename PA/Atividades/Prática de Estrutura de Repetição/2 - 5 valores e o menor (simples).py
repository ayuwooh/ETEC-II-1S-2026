num,count,lowest=0,0,None

while count < 5:
    count+=1
    num=int(input(f"Qual o {count}º valor? "))
    if lowest is None:
        lowest=num
    else:
        if num < lowest:
            lowest=num
print(f"O menor valor é {lowest}!")
