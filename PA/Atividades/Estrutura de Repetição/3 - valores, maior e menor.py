num,count,lowest,highest=0,0,None,None

while count < 15:
    count+=1
    num=int(input(f"Qual o {count}º valor? "))
    if highest is None:
        highest=num
    elif num > highest:
        highest=num
    elif lowest is None:
        lowest=num
    else:
        if num < lowest:
            lowest=num
print(f"O menor valor é {lowest}!")
print(f"O maior valor é {highest}!")
