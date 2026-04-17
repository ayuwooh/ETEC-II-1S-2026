sal,rval,rsal,rperc=0.0,0.0,0.0,""

sal=float(input("Qual o salário do colaborador? "))

if sal <= 1000:
    rval=sal*0.20
    rperc="20%"
elif sal > 1000 and sal < 1500:
    rval=sal*0.15
    rperc="15%"
elif sal > 1500 and sal < 2500:
    rval=sal*0.10
    rperc="10%"
else:
    rval=sal*0.05
    rperc="5%"

rsal=sal+rval

print("Salário antes do reajuste:",sal)
print("Porcentagem do reajuste:",rperc)
print("Valor do reajuste:",rval)
print("O novo salário:",rsal)