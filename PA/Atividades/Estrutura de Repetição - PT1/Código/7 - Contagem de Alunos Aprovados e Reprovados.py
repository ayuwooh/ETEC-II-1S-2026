avg, student, grade, grades, spass, notpass = 0, 0, 0.0, 0, 0, 0

while student < 10:
    while grades < 4:
        try:
            grade = float(
                input(f"Digite a {grades + 1}ª nota do {student + 1}º aluno: ")
            )
            avg += grade
            grades += 1
        except ValueError:
            print(f"Este não é um número 🥹")
    print("-" * 20)
    avg = avg / 4
    if avg >= 7:
        spass += 1
    else:
        notpass += 1
    avg = 0
    grades = 0
    student += 1

print(f"Alunos aprovados: {spass}")
print(f"Alunos reprovados: {notpass}")
