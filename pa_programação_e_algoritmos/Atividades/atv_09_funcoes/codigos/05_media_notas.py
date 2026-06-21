from functions import calc_grade


def media_notas():
    grades = []
    grade_type = ""
    i = 0
    final_grade = 0.0

    while i < 3:
        try:
            grades.append(float(input(f"Digite a {i + 1} nota: ")))
            i += 1
        except ValueError:
            print("Valor inválido.")

    while True:
        try:
            grade_type = str(input("Digite o tipo de média (A/P): ")).strip().upper()
        except ValueError:
            print("Valor inválido.")
        if grade_type in ("A", "P"):
            break
        else:
            print("Valor inválido.")
            continue

    final_grade = calc_grade(grades[0], grades[1], grades[2], grade_type)

    print(f"A média do aluno é {final_grade}.")
