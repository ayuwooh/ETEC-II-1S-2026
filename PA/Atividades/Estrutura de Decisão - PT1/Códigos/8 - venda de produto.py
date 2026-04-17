price,tax,state=0.0,0.0,""

price=float(input("Digite o valor da venda: "))
state=input("Digite a sigla do estado: ").strip().upper()

if state == "SP":
    tax = price * 0.25
elif state == "RJ":
    tax = price * 0.18
elif state == "PR":
    tax = price * 0.15
elif state == "SC":
    tax = price * 0.12
else:
    print("Estado não cadastrado!")
    tax = -1

if tax != -1:
    price = price + tax
    print("Valor do imposto:", tax)
    print("Valor total com imposto:", price)