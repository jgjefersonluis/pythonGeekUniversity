"""
Complexo (complex)
Tipo de dado usado para representar números complexos
(isso mesmo, aquilo que provavelmente estudou no terceiro ano do ensino médio).
Esse tipo normalmente é usado em cálculos geométricos e científicos.
Um tipo complexo contem duas partes: a parte real e a parte imaginária,
sendo que a parte imaginária contem um j no sufixo.
A função complex(real[, imag]) do Python possibilita a criação de números imaginários passando como argumento:
real, que é a parte Real do número complexo e o argumento opcional imag, representando
a parte imaginária do número complexo.
"""

a = 5+2j
b = 20+6j

print(a)
print(b)
print(type(a))
print(type(b))
print(complex(2, 5))
