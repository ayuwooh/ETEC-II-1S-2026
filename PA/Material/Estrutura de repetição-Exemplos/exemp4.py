vnum,vcont,vsoma=0,0,0
while vcont<10:
    vnum=int(input(f"Digite o {vcont+1}º número : "))
    if vcont==4:
        break
    vsoma+=vnum
    vcont+=1
else:
    print("A estrutura de repetição foi executada até o seu final")    
print("A soma dos números é :",vsoma)