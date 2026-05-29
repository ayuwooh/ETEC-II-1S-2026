sal,time,readj=0.0,0,0.0

sal=float(input("Digite o salário do funcionário: "))
time=int(input("Digite o tempo de serviço do funcionário em anos: "))

if sal > 3000 and time > 5:
    readj = sal * (9/100)
elif sal <= 3000:
    if time > 5:
        readj = sal * (12/100)
    elif time <= 5:
        readj = sal * (10/100)

sal = sal + readj
print("Reajuste:",readj)
print("Salário final:",sal)