import os
import time
import tabuleiro as tb

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

def preparar_tabuleiro():
    tb.imprimir_tabuleiro_bonito(tabuleiro)
    celula = input("Selecione uma célula (ex: A1): ").strip().upper()
    x = ord(celula[0]) - 65 
    y = int(celula[1])

    print(f"Você selecionou a célula: {input} (x={x}, y={y})")

    tabuleiro[y][x] = "X"
    tb.imprimir_tabuleiro_bonito(tabuleiro)

    limpar_terminal(1)

if __name__ == "__main__":
    limpar_terminal()

    escrever_linha()
    print("Bem-vindo ao Batalha Naval!".center(30)) 
    escrever_linha(quebra_antes=True)

    limpar_terminal(3)

    escrever_linha()
    jogador_nome = input("Digite seu nome: ").strip().capitalize()
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
        tabuleiro = tb.criar_tabuleiro()

        for i in range(5):
            escrever_linha()
            print("NAVIO DE 5 CÉLULAS")
            escrever_linha(True)
            preparar_tabuleiro()

        for i in range(4):
            escrever_linha()
            print("NAVIO DE 4 CÉLULAS")
            escrever_linha(True)
            preparar_tabuleiro()

        for i in range(6):
            escrever_linha()
            print("2 NAVIOS DE 3 CÉLULAS")
            escrever_linha(True)
            preparar_tabuleiro()

        for i in range(4):
            escrever_linha()
            print("2 NAVIOS DE 2 CÉLULAS")
            escrever_linha(True)
            preparar_tabuleiro()

        for i in range(3):
            escrever_linha()
            print("3 NAVIOS DE 1 CÉLULA")
            escrever_linha(True)
            preparar_tabuleiro()    
        
    elif escolha == 2:
        ...
    elif escolha == 3:
        ...

# Etica e dados 35N34
# IA aplicada a educação 35N12 das 6:40 ~ 22:10

# Apendrizado profundo
# Apendizado por refroço
# IA para jogos 1
