year,val,tax=0,0.0,0.0

year=int(input("Qual o ano do carro? "))
val=float(input("Qual o valor do carro? "))

if year < 2000:
    tax=val*0.01
else:
    tax=val*0.015

print("Imposto a pagar: R$",tax)