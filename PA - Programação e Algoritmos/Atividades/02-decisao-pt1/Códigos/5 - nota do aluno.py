vnota1,vnota2,vnota3,vnota4,vmedia,vpresenca,vaulas,vfaltas=0.0,0.0,0.0,0.0,0.0,0.0,0,0

vnota1=float(input("Insira a primeira nota: "))
vnota2=float(input("Insira a segunda nota: "))
vnota3=float(input("Insira a terceira nota: "))
vnota4=float(input("Insira a quarta nota: "))
vaulas=int(input("Insira a quantidade de aulas: "))
vfaltas=int(input("Insira a quantidade de faltas: "))

vpresenca=((vaulas-vfaltas)/vaulas)*100
print("Presença:",vpresenca)
vmedia=(vnota1+vnota2+vnota3+vnota4)/4
print("Média:",vmedia)

if vpresenca >= 75:
    if vmedia >= 7:
        print("Aluno aprovado.")
    elif vmedia >= 5 and vmedia < 7:
        print("Aluno em recuperação.")
    else:
        print("Aluno reprovado.")
else:
    print("Aluno reprovado por falta.")