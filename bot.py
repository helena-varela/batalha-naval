import random
import tabuleiro as tb

def gerar_tabuleiro_bot() -> list[list[str]]: 
    """Gera um tabuleiro do inimigo bot"""
    tabuleiro_bot = tb.criar_tabuleiro()

    direcoes = ('cima', 'direita', 'baixo', 'esquerda')

    # Navio de 5 células
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        direcao = random.choice(direcoes)

        if direcao == 'cima':
            if linha >= 4:
                conta_passos = 0
                for i in range(4): 
                    if tabuleiro_bot[linha - i][coluna] == ' ':
                        conta_passos += 1
                if conta_passos == 4:
                    for i in range(5):
                        tabuleiro_bot[linha - i][coluna] = "✈"
                    break
        elif direcao == 'direita':
            if coluna <= 5:
                conta_passos = 0
                for i in range(4): 
                    if tabuleiro_bot[linha][coluna + i] == ' ':
                        conta_passos += 1
                if conta_passos == 4:
                    for i in range(5):
                        tabuleiro_bot[linha][coluna + i] = "✈"
                    break
        elif direcao == 'baixo':
            if linha <= 5:
                conta_passos = 0
                for i in range(4): 
                    if tabuleiro_bot[linha + i][coluna] == ' ':
                        conta_passos += 1
                if conta_passos == 4:
                    for i in range(5):
                        tabuleiro_bot[linha + i][coluna] = "✈"
                    break           
        else:
            if coluna >= 4:
                conta_passos = 0
                for i in range(4): 
                    if tabuleiro_bot[linha][coluna - i] == ' ':
                        conta_passos += 1
                if conta_passos == 4:
                    for i in range(5):
                        tabuleiro_bot[linha][coluna - i] = "✈"
                    break                    

    # Navio de 4 células
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        direcao = random.choice(direcoes)

        if direcao == 'cima':
            if linha >= 3:
                conta_passos = 0
                for i in range(4): 
                    if tabuleiro_bot[linha - i][coluna] == ' ':
                        conta_passos += 1
                if conta_passos == 4:
                    for i in range(4):
                        tabuleiro_bot[linha - i][coluna] = "☢"
                    break
        elif direcao == 'direita':
            if coluna <= 6:
                conta_passos = 0
                for i in range(4): 
                    if tabuleiro_bot[linha][coluna + i] == ' ':
                        conta_passos += 1
                if conta_passos == 4:
                    for i in range(4):
                        tabuleiro_bot[linha][coluna + i] = "☢"
                    break
        elif direcao == 'baixo':
            if linha <= 6:
                conta_passos = 0
                for i in range(4): 
                    if tabuleiro_bot[linha + i][coluna] == ' ':
                        conta_passos += 1
                if conta_passos == 4:
                    for i in range(4):
                        tabuleiro_bot[linha + i][coluna] = "☢"
                    break           
        else:
            if coluna >= 3:
                conta_passos = 0
                for i in range(4): 
                    if tabuleiro_bot[linha][coluna - i] == ' ':
                        conta_passos += 1
                if conta_passos == 4:
                    for i in range(4):
                        tabuleiro_bot[linha][coluna - i] = "☢"
                    break  

    # 2 Navios de 3 células 
    for _ in range(2):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            direcao = random.choice(direcoes)

            if direcao == 'cima':
                if linha >= 2:
                    conta_passos = 0
                    for i in range(3): 
                        if tabuleiro_bot[linha - i][coluna] == ' ':
                            conta_passos += 1
                    if conta_passos == 3:
                        for i in range(3):
                            tabuleiro_bot[linha - i][coluna] = "★"
                        break
            elif direcao == 'direita':
                if coluna <= 7:
                    conta_passos = 0
                    for i in range(3): 
                        if tabuleiro_bot[linha][coluna + i] == ' ':
                            conta_passos += 1
                    if conta_passos == 3:
                        for i in range(3):
                            tabuleiro_bot[linha][coluna + i] = "★"
                        break
            elif direcao == 'baixo':
                if linha <= 7:
                    conta_passos = 0
                    for i in range(3): 
                        if tabuleiro_bot[linha + i][coluna] == ' ':
                            conta_passos += 1
                    if conta_passos == 3:
                        for i in range(3):
                            tabuleiro_bot[linha + i][coluna] = "★"
                        break           
            else:
                if coluna >= 2:
                    conta_passos = 0
                    for i in range(3): 
                        if tabuleiro_bot[linha][coluna - i] == ' ':
                            conta_passos += 1
                    if conta_passos == 3:
                        for i in range(3):
                            tabuleiro_bot[linha][coluna - i] = "★"
                        break  

    for _ in range(2):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            direcao = random.choice(direcoes)

            if direcao == 'cima':
                if linha >= 1:
                    conta_passos = 0
                    for i in range(2): 
                        if tabuleiro_bot[linha - i][coluna] == ' ':
                            conta_passos += 1
                    if conta_passos == 2:
                        for i in range(2):
                            tabuleiro_bot[linha - i][coluna] = "✽"
                        break
            elif direcao == 'direita':
                if coluna <= 8:
                    conta_passos = 0
                    for i in range(2): 
                        if tabuleiro_bot[linha][coluna + i] == ' ':
                            conta_passos += 1
                    if conta_passos == 2:
                        for i in range(2):
                            tabuleiro_bot[linha][coluna + i] = "✽"
                        break
            elif direcao == 'baixo':
                if linha <= 8:
                    conta_passos = 0
                    for i in range(2): 
                        if tabuleiro_bot[linha + i][coluna] == ' ':
                            conta_passos += 1
                    if conta_passos == 2:
                        for i in range(2):
                            tabuleiro_bot[linha + i][coluna] = "✽"
                        break           
            else:
                if coluna >= 1:
                    conta_passos = 0
                    for i in range(2): 
                        if tabuleiro_bot[linha][coluna - i] == ' ':
                            conta_passos += 1
                    if conta_passos == 2:
                        for i in range(2):
                            tabuleiro_bot[linha][coluna - i] = "✽"
                        break 

    # 3 Navios de 1 célula
    for _ in range(3):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            direcao = random.choice(direcoes)

            if direcao == 'cima':
                if linha >= 0:
                    conta_passos = 0
                    for i in range(1): 
                        if tabuleiro_bot[linha - i][coluna] == ' ':
                            conta_passos += 1
                    if conta_passos == 1:
                        for i in range(1):
                            tabuleiro_bot[linha - i][coluna] = "✚"
                        break
            elif direcao == 'direita':
                if coluna <= 9:
                    conta_passos = 0
                    for i in range(1): 
                        if tabuleiro_bot[linha][coluna + i] == ' ':
                            conta_passos += 1
                    if conta_passos == 1:
                        for i in range(1):
                            tabuleiro_bot[linha][coluna + i] = "✚"
                        break
            elif direcao == 'baixo':
                if linha <= 9:
                    conta_passos = 0
                    for i in range(1): 
                        if tabuleiro_bot[linha + i][coluna] == ' ':
                            conta_passos += 1
                    if conta_passos == 1:
                        for i in range(1):
                            tabuleiro_bot[linha + i][coluna] = "✚"
                        break           
            else:
                if coluna >= 0:
                    conta_passos = 0
                    for i in range(1): 
                        if tabuleiro_bot[linha][coluna - i] == ' ':
                            conta_passos += 1
                    if conta_passos == 1:
                        for i in range(1):
                            tabuleiro_bot[linha][coluna - i] = "✚"
                        break
    return tabuleiro_bot