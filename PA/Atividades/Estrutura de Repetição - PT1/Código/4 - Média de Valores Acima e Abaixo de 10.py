num, count, counthigh, countlow, sumhigh, sumlow, highavg, lowavg = 0, 0, 0, 0, 0, 0, 0, 0

while count < 10:
    count += 1
    num = int(input(f"Qual o {count}º valor? "))
    if num >= 10:
        counthigh += 1
        sumhigh += num
    else:
        countlow += 1
        sumlow += num
        
highavg = sumhigh / counthigh
lowavg = sumlow / countlow

print(f"Média dos valores iguais ou acima de 10: {highavg}")
print(f"Média dos valores abaixo de 10: {lowavg}")
