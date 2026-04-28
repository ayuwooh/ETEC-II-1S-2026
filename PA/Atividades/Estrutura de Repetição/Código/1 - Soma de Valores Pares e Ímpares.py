num, sumeven, sumuneven, count, evenoruneven = 0, 0, 0, 0, 0

while count < 10:
    count += 1
    num = int(input(f"Digite um valor: "))
    evenoruneven = num % 2
    if evenoruneven == 0:
        sumeven += num
    else:
        sumuneven += num
print(f"Soma dos valores pares: {sumeven}")
print(f"Soma dos valores ímpares: {sumuneven}")
