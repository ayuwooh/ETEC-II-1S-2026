num,count,count2=0,0,0

while count < 10:
    count+=1
    num=int(input(f"Qual o {count}º valor? "))
    if num in range(10,51): #if num >= 10 or <= 50: #Alternativa baseada no que aprendemos anteriormente, mas in range é mais eficiente e simples de ler.
        count2+=1
print(f"Quantidade de números entre 10 e 50: {count2}")
