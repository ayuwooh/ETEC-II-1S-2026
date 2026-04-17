int1,int2,int3=0,0,0

int1=int(input("Digite o primeiro número: "))
int2=int(input("Digite o segundo número: "))
int3=int(input("Digite o terceiro número: "))

if int1 == int2 == int3:
    print("Todos os números são iguais.")
elif int1 == int2:
    print("Dois números são iguais.", int1)
    if int1 > int3:
        print("Eles são maiores que:", int3)
    else:
        if int1 < int3:
            print("Eles são menores que:", int3)
elif int2 == int3:
    print("Dois números são iguais.", int2)
    if int2 > int1:
        print("Eles são maiores que:", int1)
    else:
        if int2 < int1:
            print("Eles são menores que:", int1)
elif int1 == int3:
    print("Dois números são iguais.", int1)
    if int1 > int2:
        print("Eles são maiores que:", int2)
    else:
        if int1 < int2:
            print("Eles são menores que:", int2)
else:
    if int1 > int2 and int1 > int3:
        print(int1, "é o maior número.")
    elif int2 > int1 and int2 > int3:
        print(int2, "é o maior número.")
    else:
        print(int3, "é o maior número.")
    if int1 < int2 and int1 < int3:
        print(int1, "é o menor número.")
    elif int2 < int1 and int2 < int3:
        print(int2, "é o menor número.")
    else:
        print(int3, "é o menor número.")