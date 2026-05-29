value,disc=0.0,0.0

value=float(input("Digite o valor da compra: "))

if value > 0 and value < 100:
    disc = value * (2/100)
elif value > 100 and value < 300:
    disc = value * (5/100)
elif value > 300 and value < 700:
    disc = value * (9/100)
elif value > 700 and value < 1200:
    disc = value * (12/100)
else:
    if value > 1200:
        disc = value * (15/100)
        
value = value - disc
print("Desconto:",disc)
print("Valor final da compra:",value)