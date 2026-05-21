'''
O Carnaval é um feriado celebrado normalmente em fevereiro; em muitas cidades brasileiras, a principal atração são os desfiles de escolas de samba. As várias agremiações desfilam ao som de seus sambas-enredos e são julgadas pela liga das escolas de samba para determinar a campeã do Carnaval.

Cada agremiação é avaliada em vários quesitos; em cada quesito, cada escola recebe cinco notas que variam de 5,0 a 10,0. A nota final da escola em um dado quesito é a soma das três notas centrais recebidas pela escola, excluindo a maior e a menor das cinco notas.

Como existem muitas escolas de samba e muitos quesitos, o presidente da liga pediu que você escrevesse um programa que, dadas as notas da agremiação, calcula a sua nota final num dado quesito.

Entrada
A entrada contém uma única linha, contendo cinco números Ni (1 ≤ i ≤ 5) e (5.0 ≤ Ni ≤ 10.0), todos com uma casa decimal, indicando as notas recebidas pela agremiação em um dos quesitos.

Saída
Seu programa deve imprimir uma única linha, contendo um único número com exatamente uma casa decimal, a nota final da escola de samba no quesito considerado.
'''

lista = list(map(float, input().split()))

menor = lista[0]
maior = lista[0]
for indice in range(1, len(lista)):
    item = lista[indice]
    if item > maior:
        maior = item
    if item < menor:
        menor = item

lista.remove(menor)
lista.remove(maior)

soma = 0
for valor in range(len(lista)):
    soma += lista[valor]
print(f"{soma:.1f}")