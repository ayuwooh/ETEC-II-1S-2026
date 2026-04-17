prod=0.0

prod=float(input("Insira o valor do produto: "))

if prod < 20:
    prod = prod + (prod * 0.45)
else:
    prod = prod + (prod * 0.30)
print("Novo valor do produto:", prod)