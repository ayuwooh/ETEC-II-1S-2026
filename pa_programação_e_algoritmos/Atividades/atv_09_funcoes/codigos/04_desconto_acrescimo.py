from functions import get_installment_rate, calc_percentage

sell_val = 0.0
installment_qty = 0
installment = 0.0
discount = 0.0

sell_val = float(input("Digite o valor de venda do produto: "))
installment_qty = int(input("Digite o valor de parcelas da compra: "))

installment = get_installment_rate(installment_qty)
discount = calc_percentage(sell_val, installment)

print(f"Valor do desconto/acréscimo: {discount}")
print(f"Valor final com desconto/acréscimo: {sell_val + discount}")
