state, SP, MG, RJ= 0, 1, 2, 3
age, agesp, agemg, agerj = 0, 0, 0, 0
spcount, mgcount, rjcount = 0, 0, 0
oldestsp, oldestmg, oldestrj = 0, 0, 0

while True:
    print("Estados disponíveis: 1 - SP, 2 - MG, 3 - RJ")

    try:
        state = int(input("Digite o estado da pessoa: "))

        if state < 0:
            break

        elif state not in (SP, MG, RJ):
            print("--" * 30)
            print("Estado inválido. Use 1, 2, 3 ou -1 para sair.")
            print("--" * 30)
            continue
    except ValueError:
        print("--" * 30)
        print("Estado inválido. Digite um número.")
        print("--" * 30)
        continue

    try:
        age = int(input("Digite a idade da pessoa: "))

        if age <= 0:
            print("--" * 30)
            print("Idade inválida. Por favor, digite um número positivo.")
            print("--" * 30)
            continue
    except ValueError:
        print("--" * 30)
        print("Idade inválida. Por favor, digite um número.")
        print("--" * 30)
        continue

    if state == SP:
        agesp += age
        spcount += 1
        if age > oldestsp:
            oldestsp = age
    elif state == MG:
        agemg += age
        mgcount += 1
        if age > oldestmg:
            oldestmg = age
    elif state == RJ:
        agerj += age
        rjcount += 1
        if age > oldestrj:
            oldestrj = age

    print("-" * 30)

if spcount > 0:
    agesp = agesp / spcount
    print(f"Média de idade em SP: {agesp}")
    print(f"Pessoa mais velha em SP: {oldestsp}")

if mgcount > 0:
    agemg = agemg / mgcount 
    print(f"Média de idade em MG: {agemg}")
    print(f"Pessoa mais velha em MG: {oldestmg}")
if rjcount > 0:
    agerj = agerj / rjcount
    print(f"Média de idade em RJ: {agerj}")
    print(f"Pessoa mais velha em RJ: {oldestrj}")