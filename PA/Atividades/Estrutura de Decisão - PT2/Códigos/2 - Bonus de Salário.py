time,child,marriage,extrah,sal=0,0,0,0,3000.0

time=int(input("Tempo do funcionário na empresa: "))
child=int(input("Quantidade de filhos: "))
marriage=int(input("Tempo de casamento: "))
extrah=int(input("Horas extras feitas: "))

if time > 5:
    if child > 2:
        if marriage > 2:
            if extrah > 10:
                sal = sal + (sal * 0.05)
                print("O salário reajustado é de:", sal)
else:
    print("O funcionário não terá o salário reajustado.")