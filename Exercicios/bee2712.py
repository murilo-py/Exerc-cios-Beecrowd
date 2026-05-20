'''
O rodízio municipal de veículos de São Paulo é uma restrição à circulação de veículos automotores na cidade. Implantado desde 1996 com o propósito de melhorar as condições ambientais reduzindo a carga de poluentes na atmosfera, se consolidou como um instrumento para reduzir congestionamentos nas principais vias da cidade, nos horários de maior movimento. Nas vias delimitadoras não é permitido o tráfego de caminhões e automóveis que estejam dentro da restrição. Há uma escala que determina em quais dias da semana quais veículos não podem circular. Essa escala é regida pelo último dígito da placa do veículo, sendo:

Segunda-feira, digito final da placa 1 e 2
Terça-feira, digito final da placa 3 e 4
Quarta-feira, digito final da placa 5 e 6
Quinta-feira, digito final da placa 7 e 8
Sexta-feira, digito final da placa 9 e 0
Os motoristas que são flagrados violando a restrição de circulação são autuados com multa e quatro pontos na carteira de habilitação.

Entrada
A primeira linha de entrada representa a quantidade de testes N (0 <= N < 1000) que deverão ser considerados. As demais entradas são cadeia de caracteres com tamanho máximo S (1 <= S <= 100) que representam cada placa que deverá ser analisada, de tal forma que, cada placa fique em uma única linha de entrada. O formato esperado para uma placa veicular válida em São Paulo é "AAA-9999", tal que A é um caracter válido em [A-Z], e 9 um dígito numérico válido em [0-9].

Saída
O conjunto de valores válidos como saída são: MONDAY, TUESDAY, WEDNESDAY, THURSDAY e FRIDAY, de acordo com a tabela de restrições predefinida, e FAILURE caso a placa não apresente o padrão definido.
'''
#"01234567"
#"AAA-9999"
qtd = int(input())
tabela = [
    [1, 2, 'MONDAY'],
    [3, 4, 'TUESDAY'],
    [5, 6, 'WEDNESDAY'],
    [7, 8, 'THURSDAY'],
    [9, 0, 'FRIDAY']
]

for q in range(qtd):
    placa = input()
    if len(placa) != 8:
        print('FAILURE')
    elif placa[3] != '-':
        print('FAILURE')
    else:
        try:
            numeros = int(placa[4:8])
            if 'A' <= placa[0] <= 'Z' and 'A' <= placa[1] <= 'Z' and 'A' <= placa[2] <= 'Z':
                for i in range(len(tabela)):
                    if int(placa[7]) == tabela[i][0] or int(placa[7]) == tabela[i][1]:
                        print(tabela[i][2])
            else:
                print('FAILURE')
        except ValueError:
            print('FAILURE')
