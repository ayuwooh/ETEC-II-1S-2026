from functions import age_category


def categoria_idade():
    age = int(input("Digite a idade: "))
    print(age_category(age))
