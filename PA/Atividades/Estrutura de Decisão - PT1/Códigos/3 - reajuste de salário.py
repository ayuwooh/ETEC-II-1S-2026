vsal,vreaj=0.0,0.0

vsal=float(input("Digite o salário: "))

if vsal < 2000.00:
    vreaj=vsal*(15/100)
elif vsal >= 2000.00 and vsal <= 5000.00:
    vreaj=vsal*(10/100)
else:
    vreaj=vsal*(5/100)
vsal=vsal+vreaj
print("O salário reajustado é:",vsal)
print("E o valor de reajuste é:",vreaj)