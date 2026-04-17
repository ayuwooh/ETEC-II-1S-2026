sal,time,readj=0.0,0,0.0

sal=float(input("Digite o salário do funcionário: "))
time=int(input("Digite o tempo de serviço do funcionário em anos: "))

if time >= 5:
    readj=sal*0.20
else:
    readj=sal*0.10

sal=sal+readj

print("Bônus:",readj)
print("Salário final:",sal)

# Muito similar a "PT1 - 9"
# Acabei copiando o código e só reajustando as necessidades dessa questão.