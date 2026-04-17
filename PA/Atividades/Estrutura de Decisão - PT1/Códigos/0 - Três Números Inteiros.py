int1, int2, int3 = 0, 0, 0

int1=int(input("Qual o primeiro número? "))
int2=int(input("Qual o segundo número? "))
int3=int(input("Qual o terceiro número? "))

if int1 == int2 == int3: #Checa se os números são iguais primeiro, se forem, dá o resultado e não checa mais nada.
    print("Os números são iguais")
else:
    if int1 > int2 and int1 > int3: #Checa qual é o maior número entre os três números.
        print(int1, "é o maior número")
    elif int2 > int1 and int2 > int3:
        print(int2, "é o maior número")
    else:
        print(int3, "é o maior número")

    if int1 < int2 and int1 < int3: #Checa qual é o menor número entre os três números.
        print(int1, "é o menor número")
    elif int2 < int1 and int2 < int3:
        print(int2, "é o menor número")
    else:
        print(int3, "é o menor número")