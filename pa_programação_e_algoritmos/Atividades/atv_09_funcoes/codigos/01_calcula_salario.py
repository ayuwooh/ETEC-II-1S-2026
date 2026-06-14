from atv_09_funcoes.codigos.functions import add

salary = 0.0
readj = 0.0
result = 0.0

print("-" * 30)
print("Para parar o programa, digite qualquer valor negativo.")
print("-" * 30)

while True:
    try:
        salary = float(input("Digite o valor do salário: "))
        if salary < 0:
            break
        readj = float(input("Digite o reajuste: "))
        if readj < 0:
            break
    except ValueError:
        print("Este não é um valor válido.")

    result = add(salary, readj)

    if result < 1400:
        print(f"{result} - Salário abaixo da média.")
    elif result <= 1800:
        print(f"{result} - Salário dentro da média.")
    else:
        print(f"{result} - Salário acima da média.")
