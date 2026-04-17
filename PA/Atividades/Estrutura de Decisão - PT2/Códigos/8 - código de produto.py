pcode=0

pcode=int(input("Qual o código do produto? "))

if pcode == 1:
    print("Alimento não-perecível")
elif pcode == 2 or pcode ==  3 or pcode == 4:
    print("Alimento perecível")
elif pcode == 5 or pcode == 6:
    print("Vestuário")
elif pcode == 7:
    print("Higiene Pessoal")
elif pcode == 8 or pcode == 9 or pcode == 10:
    print("Utensílios Domésticos")
else:
    print("Produto Inválido")