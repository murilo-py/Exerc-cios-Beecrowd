'''
O Grande herói Chapolout vai ajudar um inventor, e lá encontra com o genro dele, que tinha más intenções. Para tentá-lo fazer mudar de ideia, Chapolout conta a estória de Tausfo e Mefistótriste. Tausfo era um senhor com idade bem avançada, e era apaixonado por uma mulher bem mais jovem que ele. Um dia, ele recebe a visita de Mefistótriste, um demônio que lhe oferece uma ferramenta, chamada Chirrin Chirrion, que trazia ou afastava coisas conforme era dito. Para trazer algo, precisava dizer o que queria, seguido da palavra Chirrin, e para afastar algo, precisava dizer o que não queria, seguido da palavra Chirrion. Qualquer outra palavra dita, não iria fazer efeito. Depois de tanto usar, Mefistótriste volta e diz que irá levar a sua alma consigo, a menos que devolvesse tudo o que havia pedido. Ajude Tausfo!

Escreva um programa que, - dadas as utilizações da ferramenta -, reúna tudo o que Tausfo adquiriu com o Chirrin Chirrion.

Entrada
O primeiro valor a ser lido é um inteiro C, indicando o número de casos de teste. Cada caso de teste inicia com um inteiro N, informando quantas utilizações foram feitas. Considere que antes ele não possuía nada, que um Chirrion só terá efeito se ele possuir tal coisa dita, e que um Chirrin só terá efeito se ele ainda não possuir tal coisa, ou seja, não tem como ele possuir dois exemplares de uma mesma coisa.

Saída
Para cada caso de teste, imprima a palavra TOTAL, seguida da relação de coisas que Tausfo tem, em ordem alfabética.
'''

def meuIn(valor, verificado): #Função que substitui o metodo "In".
    '''
    Função criada com o objetivo de substituir comandos nativos do python
    a fim de progamar em padrão C para fins didaticos.
    '''

    for v in range(len(verificado)):
        v_testado = verificado[v]
        if v_testado == valor:
            return True
    return False

#Progama principal.

qtd = int(input())

for x in range(qtd): #Loop que faz as listas.
    listaitens = [] #Para cada caso de teste cria uma lista vazia.
    qtd_itens = int(input()) 
    
    for y in range(qtd_itens):
        comando = input().split() #le o comando de forma separada entre os espaços.

        if comando[1] == 'chirrin' and not meuIn(comando[0], listaitens): #Adiciona se ele não tiver na lista.
            listaitens.append(comando[0])
        elif comando[1] == 'chirrion' and meuIn(comando[0], listaitens): #Remove se ele tiver na lista.
            listaitens.remove(comando[0]) 


            #COLOCAR EM ORDEM ALFABETICA AQ
        
    print('TOTAL')

    for i in range(len(listaitens)):
        item = listaitens[i]

        print(item)