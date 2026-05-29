vcont,vnum,vsoma=0,0,0
while  True:
    vnum=int(input(f"Entre com {vcont+1}º número : "))
    if vnum<=0:
        break
    vsoma+=vnum
    vcont+=1

print("O valor da soma é:",vsoma)    


