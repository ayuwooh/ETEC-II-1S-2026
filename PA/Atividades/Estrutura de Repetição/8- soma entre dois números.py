num1, num2, sum, mid = 0, 0, 0, 0

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
except ValueError:
    print("Este não é um número. 🥹")
sum = num1 + num2
mid = num1
while True:
    mid += 1
    if mid == num2:
        break
    else:
        sum += mid

print(f"A soma dos números entre {num1} e {num2} é: {sum}")
