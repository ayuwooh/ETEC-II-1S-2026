from funcoes import *

vlista=[]
vprocura=0
for i in range(10):
    vlista.append(int(input(f"Entre com o {i+1}º número para a lista :")))

vprocura=int(input("Entre com um número a ser procurado :"))

if fprocura(vlista,vprocura)==True:
    print("O número está na lista")
else:
    print("O número não está na lista !")

vnum1,vnum2=0,0
vnum1=int(input("Entre com o primeiro número :"))
vnum2=int(input("Entre com o segundo número :"))
print("A soma dos número é :",somar(vnum1,vnum2))

