def add(var1, var2):
    sum = var1 + var2
    return sum


def find_concept(var):
    if var >= 9:
        result = 1
    elif var >= 7.5:
        result = 2
    elif var >= 6:
        result = 3
    elif var >= 4:
        result = 4
    else:
        result = 5
    return result


def find_max(var):
    biggest = var[0]
    for i in var[1:]:
        if i > biggest:
            biggest = i
    return biggest


def get_installment_rate(var):
    if var == 1:
        installment = -5.0  # %
    elif var == 2:
        installment = 1.0  # %
    elif var == 3:
        installment = 4.5  # %
    elif var == 4:
        installment = 7.5  # %
    else:
        installment = 10.0  # %
    return installment


def calc_percentage(amount, percentage):
    value = (amount * percentage) / 100
    return value


def calc_grade(grade1, grade2, grade3, grade_type):
    if grade_type == "A":
        grade = (grade1 + grade2 + grade3) / 3
    elif grade_type == "P":
        grade = ((grade1 * 5) + (grade2 * 3) + (grade3 * 2)) / 10
    return grade


def age_category(age):
    if age < 5:
        return "Inválido"
    elif age >= 5 and age <= 7:
        return "Infantil A"
    elif age <= 10:
        return "Infantil B"
    elif age <= 13:
        return "Juvenil A"
    elif age <= 17:
        return "Juvenil B"
    else:
        return "Adulto"


def positive_or_negative(var):
    if var < 0:
        return False
    else:
        return True


def even_or_uneven(var):
    if var % 2 == 0:
        return True
    else:
        return False


def fatorial(var):
    result = 1
    for i in range(1, var + 1):
        result *= i
    return result


def calc_readj(sal, children):
    if sal < 1000:
        readj = 9.0
    elif sal < 3000:
        readj = 7.0
    else:
        readj = 1.0
    if children < 3:
        readj += 1.0
    else:
        readj += 2.0
    readj_sal = (sal * readj) / 100
    sal += readj_sal
    return sal
