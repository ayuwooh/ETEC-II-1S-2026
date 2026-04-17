vcont,vnum,vsoma=0,0,0
while vcont<10:
    vnum=int(input(f"Entre com {vcont+1}º número : "))
    if vnum<=0:
        print("Favor digitar apenas números maiores do que zero !")
        continue

    vsoma+=vnum
    vcont+=1
    if vnum >300:
        break
else:
    print("A repetição foi executada completamente")



print("O valor da soma é:",vsoma)    


