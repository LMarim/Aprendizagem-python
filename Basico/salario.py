nome = "Lucas"
sal_bruto = 8756
ir = 0.08 * sal_bruto
inss = 0.05 * sal_bruto

sal_liq = sal_bruto - ir - inss

print(f"{nome}, o seu salário é: {sal_liq:.2f} ")
