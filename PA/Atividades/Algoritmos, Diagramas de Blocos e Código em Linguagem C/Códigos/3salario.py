vsalariomin,vcarrosvend,vvalorvendas,vsalariototal=0.0,0.0,0.0,0.0
vsalariomin=float(input("Qual o salário mínimo? "))
vcarrosvend=float(input("Qual a quantidade de carros vendidos? "))
vvalorvendas=float(input("Qual o valor total de vendas? "))
vsalariototal=(vsalariomin*2)+(vcarrosvend*50)+(vvalorvendas*0.05)
print("O salário total do vendedor é de: ",vsalariototal)