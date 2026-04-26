num,sum=0,0

while True:
    num=int(input(f"Digite um valor: "))
    sum+=num
    if num < 0:
        break
print(f"Soma de todos os valores: {sum}")
