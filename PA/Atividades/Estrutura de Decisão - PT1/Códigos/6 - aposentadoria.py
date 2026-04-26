vage,vcont=0,0

vage=int(input("Digite a idade do trabalhador: "))
vcont=int(input("Digite o tempo de contribuição do trabalhador em anos: "))

if vage >= 65 or vcont >= 30 or (vage >= 60 and vcont >= 25):
    print("O trabalhador já pode se aposentar.")
else:
    print("O trabalhador ainda não é qualificado a aposentadoria.")