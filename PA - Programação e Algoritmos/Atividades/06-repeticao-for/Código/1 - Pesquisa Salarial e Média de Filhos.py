sal, children, poor, rich = 0.0, 0.0, 0.0, 0.0
avgsal, avgchild = 0.0, 0.0
count = 0

for count in range(1, 21):
    sal = float(input(f"Qual o salário da {count}º pessoa? "))
    children = float(input("Quantos filhos ela possuí? "))
    if sal > rich:
        rich = sal
    if sal < 1200:
        poor += 1
    avgsal += sal
    avgchild += children

avgsal = avgsal / 20
avgchild = avgchild / 20
poor = poor / 20

print("-" * 30)
print(f"Média de salário: {avgsal:.2f}")
print(f"Média de filhos: {avgchild:.2f}")
print(f"Maior salário: R${rich:.2f}")
print(f"Pessoas com salário abaixo de R$1200.00: {poor:.2%}")
