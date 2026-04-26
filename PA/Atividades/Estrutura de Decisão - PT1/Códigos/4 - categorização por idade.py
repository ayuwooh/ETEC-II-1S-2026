vage=0

vage=int(input("Qual a idade da pessoa? "))

if vage <= 12:
    print("Categoria Infantil")
elif vage > 12 and vage <= 18:
    print("Categoria Juvenil")
else:
    print("Categoria Adulto")