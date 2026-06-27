notas = []
count = 0
avg, nota = 0.0, 0.0

while count < 5:
    try:
        nota = float(input(f"Qual a {count + 1} nota do aluno? "))
    except ValueError:
        print("Este não é um valor válido, tente de novo.")
        continue
    notas.append(nota)
    count += 1

avg = sum(notas) / len(notas)

print("-" * 30)
if avg >= 7:
    print("Aluno aprovado.")
elif avg >= 5:
    print("Aluno está em recuperação.")
else:
    print("Aluno reprovado.")
