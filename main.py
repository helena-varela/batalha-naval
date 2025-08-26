import os
import time
import tabuleiro as tb
import bot 
import random

TAM_LINHA_TERMINAL=30

def escrever_linha(quebra_antes=False):
    """Escreve uma linha de separação no terminal"""
    if quebra_antes:
        print("\n", end="")
    print("-"*TAM_LINHA_TERMINAL, "\n")

def limpar_terminal(tempo=0):
    """Limpa o terminal"""
    time.sleep(tempo)
    
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

def preparar_tabuleiro(tabuleiro, simbolo):
    tb.imprimir_tabuleiro_bonito(tabuleiro)
    celula = input("Selecione uma célula (ex: A1): ").strip().upper()
    x = ord(celula[0]) - 65 
    y = int(celula[1])

    print(f"Você selecionou a célula: {celula} (x={x}, y={y})")

    tabuleiro[y][x] = simbolo
    tb.imprimir_tabuleiro_bonito(tabuleiro)

    limpar_terminal()

if __name__ == "__main__":
    limpar_terminal()

    escrever_linha()
    print("Bem-vindo ao Batalha Naval!".center(30)) 
    escrever_linha(quebra_antes=True)

    limpar_terminal(3)

    escrever_linha()
    jogador_nome = input("Digite seu nome: ").strip().title()
    escrever_linha(quebra_antes=True)

    limpar_terminal(1)

    escrever_linha()
    print(f"Olá, {jogador_nome}, vamos jogar!\n")
    print("Qual modo de jogo:\n")
    print("1 - Jogar contra um bot")
    print("2 - Criar uma partida") 
    print("3 - Entrar em uma partida")
    escrever_linha(True)
    escolha = int(input("Selecione uma opção: "))
    escrever_linha(quebra_antes=True)

    limpar_terminal(1)
    
    if escolha == 1:
        escrever_linha()
        print("Você deseja montar seu próprio tabuleiro caso contrário criaremos um pra você (s/n)")
        escrever_linha(True)
        opcao = input().lower()
        if opcao == "s":
            tabuleiro_jogador = tb.criar_tabuleiro() # tabuleiro do jogador

            for i in range(5):
                escrever_linha()
                print("NAVIO DE 5 CÉLULAS")
                escrever_linha(True)
                preparar_tabuleiro(tabuleiro_jogador, "✈")

            for i in range(4):
                escrever_linha()
                print("NAVIO DE 4 CÉLULAS")
                escrever_linha(True)
                preparar_tabuleiro(tabuleiro_jogador, "☢")

            for i in range(6):
                escrever_linha()
                print("2 NAVIOS DE 3 CÉLULAS")
                escrever_linha(True)
                preparar_tabuleiro(tabuleiro_jogador, "★")

            for i in range(4):
                escrever_linha()
                print("2 NAVIOS DE 2 CÉLULAS")
                escrever_linha(True)
                preparar_tabuleiro(tabuleiro_jogador, "✽")

            for i in range(3):
                escrever_linha()
                print("3 NAVIOS DE 1 CÉLULA")
                escrever_linha(True)
                preparar_tabuleiro(tabuleiro_jogador, "✚")
        elif opcao == "n":
            tabuleiro_jogador = bot.gerar_tabuleiro_bot()
        
        tabuleiro_inimigo = bot.gerar_tabuleiro_bot() # tabuleiro do bot
        tabuleiro_espelho_inimigo = tb.criar_tabuleiro() # tabuleiro sem nenhuma peça do bot
        tabuleiro_espelho_jogador = tb.criar_tabuleiro() # tabuleiro sem nenhuma peça do jogador

        # Iniciando o jogo
        escrever_linha(True)
        print("Começando a partida!")
        escrever_linha(True)

        navios_jogador = 0
        navios_bot = 0
        while navios_jogador != 22 and navios_bot != 22:
            limpar_terminal()
            print("Tabuleiro espelho jogador")
            tb.imprimir_tabuleiro_bonito(tabuleiro_espelho_jogador)
            print("\nNavios derrubados: ", navios_bot)

            # Round do bot
            acertou = False
            while not acertou:
                linha = random.randint(0, 9)
                coluna = random.randint(0, 9)
                if (tabuleiro_jogador[linha][coluna] == " "):
                    tabuleiro_espelho_jogador[linha][coluna] = "O"
                    acertou = True
                else:
                    if (tabuleiro_espelho_jogador[linha][coluna] == " "):
                        tabuleiro_espelho_jogador[linha][coluna] = tabuleiro_jogador[linha][coluna]
                        acertou = True
                        navios_bot += 1

            print("Tabuleiro espelho inimigo")
            tb.imprimir_tabuleiro_bonito(tabuleiro_espelho_inimigo)
            print("\nNavios derrubados: ", navios_jogador)

            celula = input("Selecione uma célula (ex: A1): ").strip().upper()
            x = ord(celula[0]) - 65 
            y = int(celula[1])
                
            if (tabuleiro_inimigo[y][x] == " "):
                tabuleiro_espelho_inimigo[y][x] = "O"
            else:
                if tabuleiro_espelho_inimigo[y][x] == " ":  # ele verifica novamente que está vazio, para evitar que seja marcado novamente e conte pontos
                    tabuleiro_espelho_inimigo[y][x] = tabuleiro_inimigo[y][x]
                    navios_jogador += 1     

        if navios_bot == 22 and navios_jogador == 22:
            print("Empate!") 
        elif navios_bot == 22:
            print("O bot ganhou a partida D:")
        elif navios_jogador == 22:
            print("Parabéns você ganhou a partida! :D")

    elif escolha == 2:
        ...

    elif escolha == 3:
        ...
