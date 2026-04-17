vnum,vcont,vsoma=0,0,0
print("Programa de soma de números, digite números para a soma e digite número negativo para parar !")
while True:
    vnum=int(input(f"Digite o {vcont+1}º número : "))
    if vnum<0:
        break
    vsoma+=vnum
    vcont+=1

    
print("A soma dos números é :",vsoma)    