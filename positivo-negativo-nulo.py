"""
Faça um programa para ler um inteiro x.
Imprima a mensagem "positivo" se o valor for positivo.
Imprima a mensagem "negativo" caso o valor seja negativo.
Imprima a mensagem "nulo" se o valor for zero.

Entrada
A entrada consiste de uma linha contendo um inteiro.

Saída
A saída consiste de uma linha contendo uma mensagem.
"""

x = int(input())

if x < 0:
    print("negativo")
elif x > 0:
    print("positivo")
else:
    print("nulo")
