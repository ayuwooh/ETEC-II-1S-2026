loan,inst,sal,limit=0.0,0.0,0.0,0.0

loan=float(input("Qual o valor do empréstimo? "))
inst=float(input("Qual o número de parcelas? "))
sal=float(input("Qual o salário do solicitante? "))

inst=loan/inst
loan=loan*1.10
limit=sal*0.30

if inst <= limit:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")