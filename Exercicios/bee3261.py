'''
Alguns vírus se replicam substituindo um pedaço de DNA em uma célula viva por um pedaço de DNA que o vírus carrega consigo. Isso faz com que a célula comece a produzir vírus idênticos ao original que infectou a célula. Um grupo de biólogos está interessado em saber quanto DNA um determinado vírus insere no genoma do hospedeiro. Para descobrir isso, eles sequenciaram o genoma completo de uma célula saudável, bem como o de uma célula idêntica infectada por um vírus.

O genoma acabou sendo muito grande, então agora eles precisam de sua ajuda na etapa de processamento de dados. Dada a sequência de DNA antes e depois da infecção do vírus, determine o comprimento do menor pedaço único e consecutivo de DNA que pode ter sido inserido na primeira sequência para transformá-lo na segunda. Um único pedaço consecutivo de DNA também pode ter sido removido da mesma posição na sequência em que o DNA foi inserido. Pequenas mudanças no DNA podem ter grandes efeitos, então o vírus pode inserir apenas algumas letras, ou mesmo nada.

Entrada
A entrada consiste em duas linhas contendo a sequência de DNA antes e depois da infecção do vírus, respectivamente. Uma sequência de DNA é fornecida como uma string contendo entre 1 e 10⁵ letras maiúsculas do alfabeto {A, G, C, T}.

Saída
Produza um inteiro, o comprimento mínimo do DNA inserido pelo vírus.
'''

original = input()
modificada = input()

if original == modificada:
    print(0)
else:
    indice_mc = len(original)
    for l in range(len(original)): 
        if l >= len(modificada):
            indice_mc = l
            break
        
        letra_o = original[l]
        letra_m = modificada[l]
        if letra_o != letra_m:
            indice_mc = l 
            break

    indice_md = len(modificada) 
    index_o = len(original)
    for y in range(len(modificada)-1, -1, -1): 
        index_o -= 1
        if index_o < indice_mc or y < indice_mc:
            break

        letra_o = original[index_o]
        letra_m = modificada[y]
        if letra_o != letra_m:
            indice_md = y + 1 
            break

    print(indice_md - indice_mc)