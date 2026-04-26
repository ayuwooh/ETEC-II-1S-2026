num,lnum,count=0,None,0

while count < 5:
    count+=1
    num=int(input(f"Qual o {count}º valor? "))
    if lnum is None:
        lnum=num
    elif count == 5 and num > lnum:
        print(True)
    elif num > lnum:
        lnum=num
    else:
        if num < lnum:
            print(False)
            break