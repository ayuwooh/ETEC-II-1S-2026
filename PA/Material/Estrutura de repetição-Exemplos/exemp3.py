vnum,vcont,vsoma=0,0,0
while vcont<10:
    vnum=int(input(f"Digite o {vcont+1}º número : "))
    if vnum<=0:
        print("Digite apenas números maiores do que o número zero !")
        continue
    vsoma+=vnum
    vcont+=1
    
print("A soma dos números é :",vsoma)    