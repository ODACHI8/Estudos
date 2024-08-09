def computador_escolhe_jogada(n,m):
    u = n%(m+1)
    if u != 0:
        return u
    else:
        u = m
        n = m - n
        print("\nO computador tirou",u,"peça(s)")
        if n == 0:
            print("\nFim de jogo! Voce ganhou!")
        else:
            print("Agora resta(m)",n,"peça(s) no tabuleiro")
            usuario_escolhe_jogada(n,m)


def usuario_escolhe_jogada(n,m):
    u = int(input("\nQuantas peças voce vai tirar? "))
    if u > o and u != 0 and u <= n and u <= m:
        return u
    else:
        print("Oops! Jogada invalida! Tente de novo.")
        usuario_escolhe_jogada(n,m)



def partida():
    n = int(input("\nQuantas peças?"))
    m = int(input("Limite de peças por jogada? "))
    if n%(m+1)==o:
        print("\nVoce comeca!")
    else:
        print("\nComputador comeca!")
    while n !=0:
        if n%(m+1)==0:
            n = n - u
            if n == 0:
                print("\nFim de jogo! Voce ganhou!")
            else:
                print("\nVoce tirou",u, "peça(s)")
                print("Agora resta(m)",n,"peça(s) no tabuleiro")
                computador_escolhe_jogada(n,m)
        else:

            u = computador_escolhe_jogada(n,m)
            n = n - u
            if n == 0:
                print("\nO computador tirou",u,"peça(s)")
                print("\nFim de jogo! O computador ganhou!")
            else:
                print("\nO computador tirou",u, "peça(s)")
                print("Agora resta(m)",n,"peça(s) no tabuleiro")
                usuario_escolhe_jogada(n,m)

def campeonato():
    i = 3
    x = 1
    while i > 0:
        print("\n****Rodada", x,"****")
        i = i - 1
        x += 1
        partida()
    else:
        print("\n****Final do campeonato! ****")
        print("\n Placar: Voce 0 x 3 Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha: \n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato\n")

    opcao = int(input("Opcao escolhida: "))
    while opcao != 1 and opcao != 2:
        print("\nOpcao invalida!")
        a = int(input("Digite uma opcao valida: "))
        opcao = a
    if opcao == 1:
        print("\nVoce esclheu uma partida isolada!")
        partida()
    else:
        print("\nVoce escolheu um campeonato!")
        campeonato()
main()
                
            
