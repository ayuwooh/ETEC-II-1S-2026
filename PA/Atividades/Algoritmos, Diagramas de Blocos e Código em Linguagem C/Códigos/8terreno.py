vlargura,vcomprimento,vprecometro,varea,vvalor=0.0,0.0,0.0,0.0,0.0
vlargura=float(input("Qual a largura do terreno? "))
vcomprimento=float(input("Qual o comprimento do terreno? "))
vprecometro=float(input("Qual o preço do metro quadrado? "))
varea=vlargura*vprecometro
vvalor=varea*vprecometro
print("A área do terreno é: ",varea)
print("O valor do terreno é de:",vvalor)