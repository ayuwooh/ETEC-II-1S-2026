sal,sex=0.0,1
sex=int(input("Qual o sexo do funcionário? 1 para Feminino e 2 para Masculino: "))
sal=float(input("Qual o salário do funcionário? "))

if sex == 1:
    if sal < 2000:
        sal = sal + (sal * 0.02)
    elif sal >= 2000:
        sal = sal + (sal * 0.05)
elif sex == 2:
    if sal < 2500:
        sal = sal + (sal * 0.04)
    else:
        sal = sal + (sal * 0.07)
        
print("O salário reajustado do funcionário é:", sal)