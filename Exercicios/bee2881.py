'''
Tia Joana é uma respeitada professora e tem vários alunos. Em sua última aula, ela prometeu que iria sortear um aluno para ganhar um bônus especial na nota final: ela colocou N pedaços de papel numerados de 1 a N em um saquinho e sorteou um determinado número K; o aluno premiado foi o K-ésimo aluno na lista de chamada.

O problema é que a Tia Joana esqueceu o diário de classe, então ela não tem como saber qual número corresponde a qual aluno. Ela sabe os nomes de todos os alunos, e que os números deles, de 1 até N, são atribuídos de acordo com a ordem alfabética, mas os alunos dela estão muito ansiosos e querem logo saber quem foi o vencedor.

Dado os nomes dos alunos da Tia Joana e o número sorteado, determine o nome do aluno que deve receber o bônus.

Entrada
A primeira linha contém dois inteiros N e K separados por um espaço em branco (1 ≤ K ≤ N ≤ 100). Cada uma das N linhas seguintes contém uma cadeia de caracteres de tamanho mínimo 1 e máximo 20 representando os nomes dos alunos. Os nomes são compostos apenas por letras minúsculas de 'a' a 'z'.

Saída
Seu programa deve imprimir uma única linha, contendo o nome do aluno que deve receber o bônus.
'''

n_total, k = map(int, input().split())

lista_chamada = list()

for al in range(n_total): #coleta os nomes dos alunos
    aluno = input()
    lista_chamada.append(aluno)

alpabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for c in range(len(lista_chamada) * 2):
    for n in range(0, len(lista_chamada) - 1): #ordena os nomes em ordem alpabetica

        nome = lista_chamada[n] # Coloca os nomes e seus respectivos indices.
        i_nome = n 
       
        proximo_n = lista_chamada[n + 1]
        i_prox = n + 1

        if (alpabeto.index(nome[0]) > alpabeto.index(proximo_n[0])): 
            
            lista_chamada.pop(i_prox)
            lista_chamada.insert(i_nome, proximo_n)

        
        elif (alpabeto.index(nome[0]) == alpabeto.index(proximo_n[0]) and alpabeto.index(nome[1]) > alpabeto.index(proximo_n[1])): 
            
            lista_chamada.pop(i_prox)
            lista_chamada.insert(i_nome, proximo_n)

print(lista_chamada[k-1])