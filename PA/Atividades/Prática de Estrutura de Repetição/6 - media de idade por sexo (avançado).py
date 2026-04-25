age,sex,count,maleavg,femavg,allavg=0,0,0,[],[],[]

while count < 10:
    while True:
        try:
            age=int(input(f"Qual a idade da pessoa? "))
            if age > 100:
                print("Idade muito alta!")
            else:
                break
        except ValueError:
            print("Entrada inválida!")
    while True:
        sex=str(input(f"Qual o sexo da pessoa? (M/F) ")).upper()
        if sex == "M":
            maleavg.append(age)
            break
        elif sex == "F":
            femavg.append(age)
            break
        else:
            print("Entrada inválida!")
    allavg.append(age)
    count+=1
maleavg=int(sum(maleavg)/len(maleavg))
femavg=int(sum(femavg)/len(femavg))
allavg=int(sum(allavg)/len(allavg))
print(f"Idade média de homens: {maleavg}")
print(f"Idade média de mulheres: {femavg}")
print(f"Idade média total: {allavg}")
