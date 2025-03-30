dias = int(input("Digite o número de dias de aluguel: "))
km = float(input("Digite o total de quilômetros rodados: "))
custo_diario = dias * 90
if km > 100:
    km_extras = km - 100
    taxa_extra = km_extras * 12
else:
    taxa_extra = 0
valor_total = custo_diario + taxa_extra
print(f"O valor total a ser pago é de R$ {valor_total:.2f}.")