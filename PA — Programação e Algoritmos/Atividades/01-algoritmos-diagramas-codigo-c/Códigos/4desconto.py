vvalorcompra,vdesconto,vvalordesconto,vvalorfinal=0.0,0.0,0.0,0.0
vvalorcompra=float(input("Qual o valor da compra? "))
vdesconto=float(input("Qual o valor percentual do desconto? "))
vvalordesconto=(vvalorcompra*vdesconto)/100
vvalorfinal=vvalorcompra-vvalordesconto
print("O valor do desconto é de: ",vvalordesconto)
print("O valor final é de:",vvalorfinal)