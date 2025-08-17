def criar_tabuleiro(linhas=10, colunas=10):
    """Cria uma matriz 10x10 preenchida com pontos"""
    return [[' ' for _ in range(colunas)] for _ in range(linhas)]

def imprimir_tabuleiro_bonito(tabuleiro):
    """Versão com bordas estilizadas"""
    letras = [chr(i) for i in range(65, 75)]
    
    print("   +" + "---+" * 10)
    print("   | " + " | ".join(letras) + " |")
    print("   +" + "---+" * 10)
    
    for i, linha in enumerate(tabuleiro):
        print(f"{i:2} | " + " | ".join(linha) + " |")
        print("   +" + "---+" * 10)