import sys

###################################################################

a = float(input("Infome A: "))
b = float(input("Informe B: "))
c = float(input("Informe C: "))
p = float(c/a)
delta = float((b**2)-(4*a*c))
s = float((-b)/a)

###################################################################

if p > 0:
    print("Seu produto resultou em: "+ str(p) +", logo, a equação possue duas raízes de sinais iguais")
else:
    print("As raízes possuem sinais opostos")
    sys.exit(0)

###################################################################

if delta >= 0:
    print("Δ resultou em um valor positivo: "+ str(delta) +", consequentemente a soma resultou em: "+ str(s))
else:
    print("Δ resultou em um valor menor que 0 (negativo), o resultado obtido foi: "+ str(delta))
    sys.exit(0)

###################################################################

if s > 0:
    print("x1 e x2 são positivos (x1; x2 > 0)")
else:
    print("x1 e x2 são negativos (x1; x2 < 0)")
