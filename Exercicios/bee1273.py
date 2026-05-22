'''
Nós temos algumas palavras e queremos justificá-las à direita, ou seja, alinhar todas elas à direita. Crie um programa que, após ler várias palavras, reimprima estas palavras com suas linhas justificadas à direita.

Entrada
A entrada contém diversos casos de testes. A primeira linha de cada caso de teste conterá um inteiro N (1 ≤ N ≤ 50), que indicará o número de palavras que virão a seguir. Cada uma das N palavras contém no mínimo uma letra e no máximo 50 letras maiúsculas (‘A’-‘Z’). O fim da entrada é indicado por N = 0.

Saída
Para cada caso de teste imprima as palavras inserindo tantos espaços quanto forem necessários à esquerda de cada palavra, para que elas apareçam todas alinhadas à direita e na mesma ordem da entrada. Deixe uma linha em branco entre os casos de teste. Não deixe espaços sobrando no final de cada linha nem imprima espaços desnecessários à esquerda, de modo que pelo menos uma das linhas impressa em cada texto inicie com uma letra.
'''
primeiro_c = False
while True:
    qtd = int(input())
    if qtd == 0: #Quebra para entradas = 0.
        break

    nomes = []

    for c in range(qtd): #Lendo todos os nomes.
        nomes.append(input().strip())

    maior = nomes[0]

    for n in range(1, len(nomes)): #Verifica o maior.
        if len(nomes[n]) > len(maior):
            maior = nomes[n]

    if primeiro_c: #Verifica se é o primeiro caso pra dar o print.
        print()
    
    for j in range(0, len(nomes)): #Printa os nomes justificados à direita.
        diferença = len(nomes[j]) - len(maior)

        if diferença < 0: #Modulo
            diferença = -(diferença)
        
        print(f'{diferença * " "}{nomes[j]}')
    
    primeiro_c = True #Se ja passou transforma pra True e não executa o if.
    