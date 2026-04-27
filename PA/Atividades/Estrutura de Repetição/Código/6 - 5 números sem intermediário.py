num, sum, high, low, count, avg = 0, 0, 0, 0, 0, 0

while count < 5:
    try:
        num = int(input(f"Digite o {count + 1}º número: "))
        count += 1
        sum += num
        if count == 1:
            high = num
            low = num
        elif num > high:
            high = num
        elif num < low:
            low = num
    except ValueError:
        print(f"Este não é um número 🥹")

sum = (sum - high) - low
avg = sum / 3

print(f"A média dos números sem o maior e menor é: {avg}")
