linhas = 20 #variaveis abaixo são ultilizada para criar a matrix que será o tabuleiro
colunas = 20
tabuleiro = [0] * linhas
tabuleiro_jogador_2 = [0] * linhas
legenda_colunas = " 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19"
partes_caidas_avião = 0 #variaveis abaixo servem para identificar se um navio foi derrubado pelo jogador 2 e caso sim dar os devios pontos para ele
partes_caidas_cruzador = 0
partes_caidas_fragata = 0
pontos_do_jogador = 0
acabar_partida = 0
identificador_de_navios = 1 
jogador_2_jogada_linha = 0
jogador_2_jogada_coluna = 0

for linha in range(linhas): # esse bloco de comando forma a matriz necessária para o tabuleiro
    tabuleiro[linha] = [0] * linhas
    tabuleiro_jogador_2[linha] = [0] * linhas

#Legenda, dentro da matriz chamada tabuleiro, os numeros a seguir correspondem aos seguintes significados 0 = agua,1 a 3 = navios em pé. 4 = agua acertada, 5 a 7 navios acertados, 8 navio derrubado

#função para mostrar o tabuleiro paro o usuario
def printar_tabuleiro(tabuleiro_escolhido):
    if tabuleiro_escolhido == 1:
        print("","",legenda_colunas)
        for cont in range(20):
            print(chr(97+cont),tabuleiro[0 + cont])
    else: 
        print("","",legenda_colunas)
        for cont in range(20):
            print(chr(97+cont),tabuleiro_jogador_2[0 + cont])

#função para mostrar o nome de qual tipo de navio o usuario está colocando nas linhas do tabuleiro(matriz)
def definir_nome_navio_linha(navio_da_vez):
    if navio_da_vez < 4:
        nome_escolhido = input("jogador 1 por favor, digite uma letra da linha que será posicionado o porta aviões: ")
    elif navio_da_vez > 3 and navio_da_vez < 8:
        nome_escolhido = input("jogador 1 por favor, digite uma letra da linha que será posicionado o cruzador: ")
    elif navio_da_vez > 7 and navio_da_vez < 13:
        nome_escolhido = input("jogador 1 por favor, digite um  a letra da linha que será possicionado a fragata: ")
    return nome_escolhido

#função para mostrar o nome de qual tipo de navio o usuario está colocando nas colunas do tabuleiro(matriz)
def definir_nome_coluna(numero_definidor):
    if numero_definidor < 4:
        nome_escolhido = int(input("jogador 1 por favor, digite o numero da coluna que será posicionado o porta aviões: "))
    elif numero_definidor > 3 and numero_definidor < 8:
        nome_escolhido = int(input("jogador 1 por favor, digite o numero da coluna que será posicionado o cruzador: "))
    elif numero_definidor > 7 and numero_definidor < 13:
        nome_escolhido = int(input("jogador 1 por favor, digite o numero da coluna que será posicionado a fragata: "))
    return nome_escolhido

#a função abaixo posiciona os navios no tabuleiro, com base nos valores fornecidos pelo jogador 1. Ela também impede o jogador de colocar o barco em posições que não existem, que ja estão ocupadas ou que não tem espaço suficiente para o navio
def colocar_navios():
    identificador_de_navios = 1
    for contador in range(12):
        localização_linha_navios = definir_nome_navio_linha(identificador_de_navios)
        localização_linha_navios = ord(localização_linha_navios)
        localização_linha_navios -= 97
        while localização_linha_navios > 17: #esse codigo não permite  uma letra com numero  maior que 17
            localização_linha_navios = input("letra incoreta, o tabuleiro so vai até a letra (t), por favor digite uma letra anterior a (t)")
            localização_linha_navios = ord(localização_linha_navios)
            localização_linha_navios -= 97
        while localização_linha_navios > 19 or localização_linha_navios < 0: #esse codigo não permite a escolha de uma posição de linha que não exista no tabuleiro
            print("esse espaço não existe, escolha outro: ")
            localização_linha_navios = definir_nome_navio_linha(identificador_de_navios)             
            localização_linha_navios = ord(localização_linha_navios)
            localização_linha_navios -= 97
        localização_coluna_navios = definir_nome_coluna(identificador_de_navios)
        if identificador_de_navios < 4:
            while localização_coluna_navios > 16 or localização_coluna_navios < 0: #não permite colocar um porta-aviões em uma coluna que não caiba ele
                localização_coluna_navios = int(input("espaço insuficiente, digite outra coluna:"))
        elif identificador_de_navios > 3 and identificador_de_navios < 8:
            while localização_coluna_navios > 17 or localização_coluna_navios < 0:  #não permite colocar um cruzador em uma coluna que não caiba ele
                localização_coluna_navios = int(input("espaço insuficiente, digite outra coluna: "))
        elif identificador_de_navios > 8:
            while localização_coluna_navios >= 19 or localização_coluna_navios < 0: #não permite colocar um fragata em uma coluna que não caiba ele
                localização_coluna_navios = int(input("espaço insuficiente,escolha outra coluna: "))
        #o bloco de comando abaixo não permite colocar um navio numa posição que ja esteja ocupada
        while tabuleiro[localização_linha_navios][localização_coluna_navios] == 3 or tabuleiro[localização_linha_navios][localização_coluna_navios] == 2 or tabuleiro[localização_linha_navios][localização_coluna_navios] == 1:
            print("já exite um navio nesse local, por favor escolha outro") 
            localização_linha_navios = definir_nome_navio_linha(identificador_de_navios) 
            localização_linha_navios = ord(localização_linha_navios)
            localização_linha_navios -= 97
            localização_coluna_navios = int(input("jogador 1 por favor, digite em que coluna será possicionado o porta aviões: ")) 

        if identificador_de_navios < 4: # o bloco de comando abaixo posiciona o porta-aviões inteiro da esquerda pra direita
            tabuleiro[localização_linha_navios][localização_coluna_navios] = 3 
            tabuleiro[localização_linha_navios][localização_coluna_navios + 1] = 3
            tabuleiro[localização_linha_navios][localização_coluna_navios + 2] = 3
            tabuleiro[localização_linha_navios][localização_coluna_navios + 3] = 3

        elif identificador_de_navios > 3 and identificador_de_navios < 8:  # o bloco de comando abaixo posiciona o cruzador inteiro da esquerda pra direita
            tabuleiro[localização_linha_navios][localização_coluna_navios] = 2
            tabuleiro[localização_linha_navios][localização_coluna_navios + 1] = 2
            tabuleiro[localização_linha_navios][localização_coluna_navios + 2] = 2

        elif identificador_de_navios > 7 and identificador_de_navios < 13: # o bloco de comando abaixo posiciona a fragata inteira da esquerda pra direita
            tabuleiro[localização_linha_navios][localização_coluna_navios] = 1
            tabuleiro[localização_linha_navios][localização_coluna_navios + 1] = 1

        identificador_de_navios += 1

        printar_tabuleiro(1)

#o bloco de comando abaixo é responsavel pelo posicionamento de navios escolhidos pelo jogador 1
print("ola jogador 1, para posicionar os navios digite primeiro a LETRA em minusculo da linha que voçe quer, depois o NUMERO da coluna que voçe quer")
print()
print("no tabuleiro oque estiver como 0 é agua, oque estiver como 3 é porta aviões, 2 é cruzador e 1 é fragata")
printar_tabuleiro(1)
colocar_navios()

#o bloco de comando abaixo pega
print()
print("jogador 2, sua rodada começará agora, para parar de jogar digite z quando for pedido a letra das linhas ou 100 quando for pedido o numero das colunas")
print("No tabuleiro os valor 4 representa um lugar que voçe ja atirou e não tinha navio, 5 acertou um porta aviões, 6 acertou um cruzador e 7 acertou uma fragata ")
print()
while jogador_2_jogada_linha != "z" or jogador_2_jogada_coluna != 100:
    printar_tabuleiro(2)
    if acabar_partida == 12: #caso seje identificado 12 navios naufragados, o jogo acaba
        break
    jogador_2_jogada_linha = input("jogador 2 escolha a letra da linha em que o tiro irá acertar: ")
    if jogador_2_jogada_linha == "z": #caso jogador digite z o jogo acaba
        break
    jogador_2_jogada_linha = ord(jogador_2_jogada_linha)
    jogador_2_jogada_linha -= 97
    jogador_2_jogada_coluna = int(input("jogador 2 escolha o numero da  coluna em que o tiro irá acertar: "))
    
    if jogador_2_jogada_coluna == 100: #esse comando serve para caso o jogador digite 100 o jogo acabar
        break
    elif tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] == 0:
        print()
        print("putz, voçê acertou agua")
        print()
        tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] = 4 #ao acertar um espaço vazio, ele muda a o espaço para 4 que será o valor de quando acertou um espaço
    #o elif abaixo e para avisar ao jogador que ele esta atirando numa posição repetida
        tabuleiro_jogador_2[jogador_2_jogada_linha][jogador_2_jogada_coluna] = 4
    elif tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] == 4 or tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] == 5 or tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] == 6 or tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] == 7:
        print()
        print("voçê ja atirou aqui")
        print()
    elif tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] == 3:#ao acertar  um porta avioes, o valor 3 mudará para 5 no tabuleiro 
        print()
        print("parabens voçê acertou um porta-aviões")
        print()
        tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] = 5 
        tabuleiro_jogador_2[jogador_2_jogada_linha][jogador_2_jogada_coluna] = 5
    elif tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] == 2:#ao acertar  um cruzador,o valor 2 mudará para 6 no tabuleiro
        print()
        print("parabens voçê acertou um cruzador")
        print()
        tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] = 6 
        tabuleiro_jogador_2[jogador_2_jogada_linha][jogador_2_jogada_coluna] = 6
    elif tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] == 1:#ao acertar uma fragata, o 1 valor mudará para 7 no tabuleiro
        print()
        print("parabens voçê acertou uma fragata")
        print()
        tabuleiro[jogador_2_jogada_linha][jogador_2_jogada_coluna] = 7 
        tabuleiro_jogador_2[jogador_2_jogada_linha][jogador_2_jogada_coluna] = 7

    for cont in range(20):
        for cont2 in range(20):

            if tabuleiro[0+cont][0+cont2] == 5: # esse bloco de comando analiza partes derrubadas do porta aviões, se achar 4 partes seguidas ele da os pontos devidos ao jogador
                partes_caidas_avião += 1
                if partes_caidas_avião == 5: 
                    partes_caidas_avião = 1
                elif partes_caidas_avião == 4:
                    print()
                    print("parabens, voçê derrubou um porta aviões inteiro")
                    print()
                    pontos_do_jogador += 30
                    acabar_partida += 1
                    tabuleiro[0+cont][0+cont2] = 8               
            else: 
                partes_caidas_avião = 0
                

            if tabuleiro[0+cont][0+cont2] == 6: # esse bloco de comando analiza partes derrubadas do cruzador, se achar 3 partes seguidas ele da os pontos devidos ao jogador
                partes_caidas_cruzador += 1
                if partes_caidas_cruzador == 4: 
                    partes_caidas_cruzador = 1
                elif partes_caidas_cruzador == 3:
                    pontos_do_jogador += 20
                    acabar_partida += 1
                    print()
                    print("parabens, voçê derrubou um cruzador inteiro")
                    print()
                    tabuleiro[0+cont][0+cont2] = 8
            else: 
                partes_caidas_cruzador = 0

            if tabuleiro[0+cont][0+cont2] == 7:  # esse bloco de comando analiza partes derrubadas da fragata, se achar 2 partes seguidas ele da os pontos devidos ao jogador
                partes_caidas_fragata += 1
                if partes_caidas_fragata == 3: 
                    partes_caidas_fragata = 1
                elif partes_caidas_fragata == 2:
                    pontos_do_jogador += 10
                    acabar_partida += 1
                    print()
                    print("parabens, voçê derrubou uma fragata inteira")
                    print()
                    tabuleiro[0+cont][0+cont2] = 8                   
            else: 
                partes_caidas_fragata = 0     

            

print("O jogo acabou, a quantidade de pontos do jogador 2 foi:",pontos_do_jogador)
