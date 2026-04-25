age,agesum,agesummale,agesumfem,count,maleavg,femavg,allavg,sex=0,0,0,0,0,0,0,0,""

while count < 10:
    while True:
        try:
            age=int(input(f"Qual a idade da pessoa? "))
            if age > 100:
                print("Idade muito alta!")
            else:
                agesum+=age
                break
        except ValueError:
            print("Entrada inválida!")
    while True:
        sex=str(input(f"Qual o sexo da pessoa? (M/F) ")).upper()
        if sex == "M":
            maleavg+=1
            agesummale+=age
            break
        elif sex == "F":
            femavg+=1
            agesumfem+=age
            break
        else:
            print("Entrada inválida!")
    count+=1
maleavg=agesummale/maleavg
femavg=agesumfem/femavg
allavg=agesum/10
print(f"Idade média de homens: {maleavg}")
print(f"Idade média de mulheres: {femavg}")
print(f"Idade média total: {allavg}")
