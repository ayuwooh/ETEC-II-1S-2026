qty,value,revenue,cost=0,0.0,0.0,0.0

qty=int(input("Qual a quantidade de bolos vendidos no dia? "))

value=qty*70
revenue=value*0.30
cost=value-revenue

print("Custo de produção:",cost)
print("Valor das vendas:",value)
print("Lucro do dia:",revenue)