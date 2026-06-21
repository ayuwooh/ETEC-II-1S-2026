from functions import find_concept


def conceito_notas():
    grades = []
    ma = 0.0
    i = 0

    while i < 3:
        try:
            grades.append(int(input(f"Digite a {i + 1} nota: ")))
            i += 1
        except ValueError:
            print("Este não é um valor válido.")

    ma = (grades[0] + grades[1] * 2 + grades[2] * 3) / 6
    concept = find_concept(ma)

    if concept == 1:
        print("Conceito A")
    elif concept == 2:
        print("Conceito B")
    elif concept == 3:
        print("Conceito C")
    elif concept == 4:
        print("Conceito D")
    else:
        print("Conceito E")
