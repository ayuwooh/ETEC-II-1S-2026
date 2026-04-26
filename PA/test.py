def calclucro():
    vlt,vltgasto,vkminicial,vkmfinal,vdinheirop,vkml,vlucro=0.0,0.0,0.0,0.0,0.0,0.0,0.0
    
    vlt=float(input("Quantidade de litro de combustível: "))
    vltgasto=float(input("Quantidade de litros gastos: "))
    vkminicial=float(input("Qual o KM inicial do veículo? "))
    vkmfinal=float(input("Qual o KM final do veículo? "))
    vdinheirop=float(input("Qual a quantidade de dinheiro recebida dos passageiros? "))
    
    vkml=(vkmfinal-vkminicial)/vltgasto
    vlucro=vdinheirop-(vlt*vltgasto)
    
    print("O KM por litro é: ",vkml) #," e o lucro é de: ",vlucro)
    print("E o lucro é de: ",vlucro)
    
    if vlucro >= 500.0:
        print("O lucro foi bom!")
    elif vlucro < 500.0 <= 0.0:
        print("O lucro foi menor que o esperado.")
    elif vlucro <= 0.0:
        print("NÃO TIVEMOS LUCRO!!11 >:(")