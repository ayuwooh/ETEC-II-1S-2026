num, sum = 0, 0

while True:
    num = int(input("Digite um valor: "))
    sum += num
    if num < 0:
        break
print(f"Soma de todos os valores: {sum}")
