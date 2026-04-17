vpesosaco,vracaogato,vpesogramas,vconsumo,vrestante=0.0,0.0,0.0,0.0,0.0
vpesosaco=float(input("Peso do saco: "))
vracaogato=float(input("Quantidade de ração que cada gato come diaramente em gramas: "))
vpesogramas=vpesosaco*1000
vconsumo=(vracaogato*2)*5
vrestante=vpesogramas-vconsumo
print("O restante de ração dos gatos é: ",vrestante)