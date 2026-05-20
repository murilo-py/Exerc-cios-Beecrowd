'''
Vasya e Petya estão visitando o museu virtual 3D da história da capital da Nlogônia. No meio de tanta diversão, decidiram pregar uma peça. A peça consiste em danificar M modelos dentre os N expostos. Vasya baixa ilegalmente o arquivo do modelo, Petya o abre em um editor 3D e subtitui detalhes históricos por números na sequência de Fibonacci, e o coloca de volta no museu.

Toda vez que um modelo é danificado, seu valor se torna nulo. Como a dupla é extremamente malvada, decidiram causar o maior dano possível. Dados N, M e o valor de todas os modelos expostos, faça um programa que calcule o maior prejuízo que pode ser causado.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso contém dois número inteiros, N (0 ≤ N ≤ 103) e M (0 ≤ M ≤ N), respectivamente. A segunda linha contém N inteiros (entre 0 e 1000), os valores de cada modelo (em dólares nlogônios), em ordem não decrescente.

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima uma linha com um único número indicando o maior prejuízo a ser causado.
'''

while True:
    try:
        total_d = 0
        total_ex, dano = map(int, input().split())
        prices = list(map(int, input().split()))

        for ciclo in range(total_ex - 1, total_ex- dano - 1, -1):
            objeto = prices[ciclo]
            
            total_d += objeto
        
        print(int(total_d))
    except EOFError:
        break
