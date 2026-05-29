review, yesorno = 0, 0
ruim, razoavel, satisf, bom, otimo = 0, 0, 0, 0, 0

print(f"Você foi selecionado para avaliar o atendimento de nossa loja!\nPor favor, leia a tabela abaixo e digite o número indicando seu nível de satisfação.")
while True:
    print ("-" * 30)
    print ("1-Ruim\n2-Razoável\n3-Satisfatório\n4-Bom\n5-Ótimo")
    print ("-" * 30)
    review = int (input(f"Digite sua avaliação: "))
    if review not in range (1, 6):
        print("Avaliação inválida, tente novamente.")
        continue
    elif review == 1:
        ruim += 1
    elif review == 2:
        razoavel += 1
    elif review == 3:
        satisf += 1
    elif review == 4:
        bom += 1
    elif review == 5:
        otimo += 1
    yesorno = int (input(f"Você deseja continuar avaliando?\nDigite 1 para Sim ou 0 para Não. "))
    if yesorno == 1:
        continue
    else:
        break

print("-" * 30)
print("Grau de satisfação:")
print(f"Ruim:         {ruim}")
print(f"Razoável:     {razoavel}")
print(f"Satisfatório: {satisf}")
print(f"Bom:          {bom}")
print(f"Ótimo:        {otimo}")