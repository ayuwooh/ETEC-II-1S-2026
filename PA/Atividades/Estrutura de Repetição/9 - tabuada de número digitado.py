val,number,result=0,1,0

val = int(input("Digite um número para ver sua tabuada: "))
print("-" * 30)
while True:
    result=val*number
    print(f"{val}x{number}={result}")
    if number == 10:
        break
    number+=1
print("-" * 30)
