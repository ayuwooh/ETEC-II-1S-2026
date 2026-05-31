vcont,vnum,vqtd1,vqtd2=0,0,0,0
while vcont<15:
    vnum=int(input(f"Entre com o {vcont+1}º número :"))
    if vnum<=5:
        vqtd1+=1
    else:
        vqtd2+=1
    vcont+=1

print("A quantidade de números menores ou iguais ao número 5 :",vqtd1)        
print("A quantidade de número maiores do que o número 5 : ",vqtd2)
