tri1,tri2,tri3=0.0,0.0,0.0

tri1=float(input("Primeiro lado do triangulo: "))
tri2=float(input("Segundo lado do triangulo: "))
tri3=float(input("Terceiro lado do triangulo: "))

if tri1 == tri2 == tri3:
    print("Triângulo Equilátero")
elif tri1 == tri2 and tri1 != tri3 or tri1 == tri3 and tri1 != tri2 or tri2 == tri3 and tri2 != tri1:
    print("Triângulo Isóceles")
else:
    print("Triângulo Escaleno")