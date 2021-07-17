import random

def fc_mostra_tabuleiro(br,ve):
    # mostra tabuleiro
    print ("pos branco == pos vermelho")
    for ibr in range(1,25):
        ive = 25 - ibr
        if ibr < 10:
            print('0',ibr,' - ',br[ibr],' == ',ive,' - ',ve[ive],sep="")
        elif ive < 10:
            print(ibr,' - ',br[ibr],' == ','0',ive,' - ',ve[ive],sep="")
        else:
            print(ibr,' - ',br[ibr],' == ',ive,' - ',ve[ive],sep="")


def fc_move_peca(br,ve,resDX,cor,veBar,brBar,movPc):

    # checa se existe movimento possivel

    resDXbar = 0 #marca que o dado nao foi usado na linha bar
    movPc = 1 #marca que o movimento da peca e possivel
    
    if cor == 'b':

        # esta saida da linha bar tem que ser testada ainda [ ]        
        if brBar != 0: # checa se existe peca na linha bar
            if ve[resDX] > 1: #checa se a casa de saida esta fechada
                movPc = 0 #marca que o dado nao podera ser usado
            elif ve[resDX] == 1: #checa se existe apenas uma peca adversaria na casa de saida
                ve[resDX] = 0
                veBar += 1
                brBar -= 1
            # checa se pode-se usar valor do dado para salvar a peca          
            if br[25 - resDX] >= 0: # checa se a casa esta apta do lado branco
                brBar -= 1
                br[25 - resDX] += 1
            else:
                movPc = 0
                #break

        # o bloco abaixo de codigo tem apenas que checar se o para o valor do dado existe lance possivel.
        i = 0       
        for indTab in range(1,25):
        #while i <= 24:
            print("entrei no for valor do i:")
            i += 1
            print(i)
            wait = input("")
            # br(indTab) != 0 - checa se a casa tem pecas brancas
            # (indTab - resDX) >=0 - checa se a casa destino eh valida
            if br(indTab) != 0:
            #and (indTab - resDX) >=0:
            #if br(i) != 0: #and (indTab - resDX) >=0:
                #print("entrei no if do for br(i)!=0")
                #print[br(indTab)]
                #wait = input("")
                # br(indTab - resDX) - checa se a casa destino eh branca
                # ve(25 - (indTab - resDX)) - checa se existe menos de duas pecas vermelhas na casa
                #if br(indTab - resDX) >= 0 or ve(25 - (indTab - resDX)) <= 1: 
                    #movPc = 1
    else:
        # checa se existe peca na linha bar
        if veBar != 0:
            # checa se pode-se usar valor do dado para salvar a peca
            if ve[resDX] >=0:
                brBar -= 1
                ve[resDX] += 1
            else:
                movPc = 0
                #break

    # escolhe peca a ser movida aleatoriamente se for possivel - DX

    if movPc == 1:
        naoEscolhi = 1
    else:
        naoEscolhi = 0		
	    
    tentativasEscolhas = 0

    while naoEscolhi:

        # Escolhe peca a ser movida
        if cor == 'b':
            ibr = random.choice(range(1,25,1))
            ive = 25 - ibr
        else:
            ive = random.choice(range(1,25,1))
            ibr = 25 - ive
            
        tentativasEscolhas += 1

        # checa valores invalidos
        if ibr == 25 or ibr == 0 or ive == 25 or ive == 0:
            print ('ibr igual a ',ibr)
            print ('ive igual a ',ive)
            naoEscolhi = 0
            
        # Calcula o movimento da peca
        if cor == 'b':
            ibrDX = ibr - resDX
            iveDX = 25 - ibrDX
        else:
            iveDX = ive - resDX
            ibrDX = 25 - iveDX
        
        # Checa se a peca calculada pode ser alterada
        # Checa que se a casa eh valida - [ibrDX  > 0]
        # Checa se na casa escolhida existe peca branca - [br[ibr] != 0]
        # Checa se a casa de destino esta vazia ou eh branca - [br[ibrDx] >= 0]
        # Checa se a casa de destino possui menos de uma peca vermelha ou nenhuma ve[ivrD1] <= 1
        if cor == 'b':
            if ibrDX  > 0 and br[ibr] != 0 and br[ibrDX] >= 0 and ve[iveDX] <= 1:
                naoEscolhi = 0
                # checa se peca foi tomada
                if ve[iveDX] == 1:
                    ve[iveDX] -= 1
                    veBar +=1
                br[ibr] -= 1
                br[ibrDX] += 1
                print ("Peça branca a ser movida: ",ibr)
                # mostra tabuleiro
                fc_mostra_tabuleiro(br,ve)
                movPc = 1
        else:
            if iveDX  > 0 and ve[ive] != 0 and br[iveDX] >= 0 and ve[ibrDX] <= 1:
                naoEscolhi = 0
                # checa se peca foi tomada
                if br[ibrDX] == 1:
                    br[ibrDX] -= 1
                    brBar +=1
                ve[ive] -= 1
                ve[iveDX] += 1
                print ("Peça vermelha a ser movida: ",ive)
                # mostra tabuleiro
                fc_mostra_tabuleiro(br,ve)
                movPc = 1

        if tentativasEscolhas > 10000:
            naoEscolhi = 0

    #print ("Sai do while depois de ",tentativasEscolhas," tentativas de escolha.")

#
# rotina principal
#

# d1 = [1,2,3,4,5,6]
d1 = range(1,6,1)
d2 = range(1,6,1)

# monta tabuleiro
br = [0]*25
ve = [0]*25

# posicao inicial do tabuleiro
br[24] = 2
br[13] = 5
br[8] = 3
br[6] = 5

ve[24] = 2
ve[13] = 5
ve[8] = 3
ve[6] = 5

veBar = 0
brBar = 0

movPc = 0 # verdadeiro se a peca pode ser movimentada
fimPartida = 0

# mostra tabuleiro
fc_mostra_tabuleiro(br,ve)

while not fimPartida:

    # joga os dados
    resD1 = random.choice(d1)
    resD2 = random.choice(d2)
    print("dado 1: ",resD1)
    print("dado 2: ",resD2)

    fc_move_peca(br,ve,resD1,'b',veBar,brBar,movPc)
    #fc_move_peca(br,ve,resD2,'b',veBar,brBar,movPc)

##    resD1 = random.choice(d1)
##    resD2 = random.choice(d2)
##    print("dado 1: ",resD1)
##    print("dado 2: ",resD2)
##
##    fc_move_peca(br,ve,resD1,'v',veBar,brBar,movPc)
##    fc_move_peca(br,ve,resD2,'v',veBar,brBar,movPc)

    fimPartida = 1

quit()



        




