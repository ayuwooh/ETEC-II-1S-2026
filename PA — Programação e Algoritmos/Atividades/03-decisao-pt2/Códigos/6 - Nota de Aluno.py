nota1,nota2,media=0.0,0.0,0.0

nota1=float(input("Qual a primeira nota? "))
nota2=float(input("Qual a segunda nota? "))

media=(nota1+nota2)/2
print("Nota:", media)

if media > 9.0 and media <= 10.0:
    print("A")
    print("APROVADO")
elif media > 7.5 and media < 9.0:
    print("B")
    print("APROVADO")
elif media > 6.0 and media < 7.5:
    print("C")
    print("APROVADO")
elif media > 4.0 and media < 6.0:
    print("D")
    print("REPROVADO")
else:
    print("E")
    print("REPROVADO")