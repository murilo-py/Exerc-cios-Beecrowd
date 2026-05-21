'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
'''

x = int(input())
y = int(input())

soma = 0

if x > y:  #Tem maneiras melhores de resolver? Sim, mas aq é a moda pratica! :) (LISTA QUE NÃO ACABA MAISSSSS)
    maior = x
    menor = y
elif y > x:
    maior = y
    menor = x
else:
    menor = x
    maior = menor

for c in range(menor + 1, maior):
    if c % 2 != 0:
        soma += (c)

print(soma)

    
