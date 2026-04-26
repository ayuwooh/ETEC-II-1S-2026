num, sum, high, low, count, avg = 0, 0, None, None, 0, 0

while count < 5:
    try:
        num = int(input(f"Digite o {count + 1}º número: "))
        count += 1
        sum += num
        if high == None or num > high:
            high = num
        elif low == None or num < low:
            low = num
    except ValueError:
        print(f"Este não é um número 🥹")

sum = (sum - high) - low # type: ignore
avg = sum / 3

print(f"A média dos números sem o maior e menor é: {avg}")
