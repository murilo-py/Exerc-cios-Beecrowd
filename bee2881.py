'''
Tia Joana é uma respeitada professora e tem vários alunos. Em sua última aula, ela prometeu que iria sortear um aluno para ganhar um bônus especial na nota final: ela colocou N pedaços de papel numerados de 1 a N em um saquinho e sorteou um determinado número K; o aluno premiado foi o K-ésimo aluno na lista de chamada.

O problema é que a Tia Joana esqueceu o diário de classe, então ela não tem como saber qual número corresponde a qual aluno. Ela sabe os nomes de todos os alunos, e que os números deles, de 1 até N, são atribuídos de acordo com a ordem alfabética, mas os alunos dela estão muito ansiosos e querem logo saber quem foi o vencedor.

Dado os nomes dos alunos da Tia Joana e o número sorteado, determine o nome do aluno que deve receber o bônus.

Entrada
A primeira linha contém dois inteiros N e K separados por um espaço em branco (1 ≤ K ≤ N ≤ 100). Cada uma das N linhas seguintes contém uma cadeia de caracteres de tamanho mínimo 1 e máximo 20 representando os nomes dos alunos. Os nomes são compostos apenas por letras minúsculas de 'a' a 'z'.

Saída
Seu programa deve imprimir uma única linha, contendo o nome do aluno que deve receber o bônus.
'''

n, k = map(int, input().split()) #n sera a quantidade de vezes que vamos contar, e k a posição na lista da chamada.

lista_chamada = list()

for al in range(n): #coleta os nomes dos alunos
    aluno = input()
    lista_chamada.append(aluno)

alpabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for c in range(len(lista_chamada)):
    for n in range(len(lista_chamada)): #ordena os nomes em ordem alpabetica

        nome = lista_chamada[n]

        if n != lista_chamada.index(lista_chamada[-1]): #se o ultimo da chamada n for o ultimo ele coloca o proximo como o nome mais 1
            proximo_n = lista_chamada[n + 1]
        else: #senão ele coloca como o proximo sendo o ultimo
            proximo_n = lista_chamada[-1]
        
        i_nome = lista_chamada.index(nome) #pega os inidices na chamada do nome e do depois do nome
        i_prox = lista_chamada.index(proximo_n)

        if alpabeto.index(nome[0]) > alpabeto.index(proximo_n[0]): #troca de lugar na lista, com referencia no indice do alpabeto
            lista_chamada.pop(i_nome)
            lista_chamada.insert(i_nome, proximo_n)

            lista_chamada.pop(i_prox)
            lista_chamada.insert(i_prox, nome)

print(lista_chamada[k-1])