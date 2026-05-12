count, age, review, regularsum = 0, 0, 0, 0
greatavg, greatage, goodpercent = 0.0, 0.0, 0.0

for count in range (1, 16):
    print(f"1 - Regular\n2 - Bom\n3 - Ótimo")
    age = int (input(f"Digite sua idade: "))
    review = int (input(f"Digite sua avaliação: "))
    if review == 1:
        regularsum += 1
    elif review == 2:
        goodpercent += 1
    elif review == 3:
        greatage += age
        greatavg += 1
        
greatavg = greatage / greatavg
goodpercent = goodpercent / 15

print(f"-" * 30)
print(f"Quantidade de avaliações regulares: {regularsum}")
print(f"Percentual de avaliações boas: {goodpercent:.2%}")
print(f"Média de idade das pessoas que avaliaram como ótimo: {greatavg:.2f}")