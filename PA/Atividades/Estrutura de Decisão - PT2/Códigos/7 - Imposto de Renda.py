hvalue,hmonth,gsalary,ir,sind,inss,fgts,dtotal,liquids=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0

hvalue=float(input("Qual o valor da hora trabalhada? "))
hmonth=float(input("Qual a quantidade de horas trabalhas no mês? "))

gsalary=hvalue*hmonth

if gsalary > 2500:
    ir=gsalary*0.20
elif gsalary > 1500 and gsalary < 2500:
    ir=gsalary*0.10
elif gsalary > 900 and gsalary < 1500:
    ir=gsalary*0.05
else:
    ir=0

sind=gsalary*0.03
inss=gsalary*0.10
fgts=gsalary*0.01
dtotal=ir+sind+inss
liquids=(((gsalary-ir)-sind)-inss)

print("Salário Bruto:",gsalary)
print("IR:",ir)
print("Síndicato:",sind)
print("INSS:",inss)
print("FGTS:",fgts)
print("Total de Descontos:",dtotal)
print("Salário Líquido:",liquids)
