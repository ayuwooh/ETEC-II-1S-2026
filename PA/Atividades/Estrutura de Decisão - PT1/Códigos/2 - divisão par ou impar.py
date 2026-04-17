vint,vdiv,vresult,vrest=0,0,0,0

vint=int(input("Digite um número: "))
vdiv=int(input("Digite outro número: "))

vresult=int(vint/vdiv)
vrest=int(vint % 2)
print(vint,"/",vdiv,"=",vresult,"(",vrest,")")
if vrest == 0:
    print(vrest,"é par.")
else:
    print(vrest,"é impar.")