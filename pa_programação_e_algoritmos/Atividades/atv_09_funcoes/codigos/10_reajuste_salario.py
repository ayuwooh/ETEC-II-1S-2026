from functions import calc_readj


def reajuste_salario():
    salary = float(input("Digite o slário do funcionário: "))
    children = int(input("Digite a quantidade de filhos que o funcionário possuí: "))
    print(f"Salário reajustado: {calc_readj(salary, children)}")
