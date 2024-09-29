import random
def colorir(texto,codigo_cor):
    return f"\033[{codigo_cor}m{texto}\033[0m"

def print_tabuleiro(tabuleiro):
    coordenadas =  [
        colorir("7","32"),colorir("8","32"),colorir("9","32"),
        colorir("4","32"),colorir("5","32"),colorir("6","32"),
        colorir("1","32"),colorir("2","32"),colorir("3","32")
    ]
    for i in range(3):
        linhas_display = []
        for j in range(3):
            valor_celula = tabuleiro[i][j] if tabuleiro[i][j] != " " else coordenadas[i * 3 + j]
            linhas_display.append(f" {valor_celula} ")
        print("┃".join(linhas_display))
        if i < 2:
            print("━" * 13)

def check_tabuleiro(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return tabuleiro[i][0]
        elif tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return tabuleiro[0][i]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]
    return None

def empate(tabuleiro):
    return all(celula != " " for linhas in tabuleiro for celula in linhas)

def movimento_computador(tabuleiro):
    while True:
        movimento = random.randint(0, 8)
        linha, coluna = divmod(movimento, 3)
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = "O"
            break

def movimento_jogador(tabuleiro, jogador):
    while True:
        try:
            movimento = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
            if movimento < 0 or movimento > 8:
                raise ValueError
            linha, coluna = divmod(movimento, 3)
            if tabuleiro[2 - linha][coluna] == " ":
                tabuleiro[2 - linha][coluna] = jogador
                break
            else:
                print("Essa posição já está ocupada. Tente novamente.")
        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente.")

def computador(tabuleiro):
    while True:
        movimento = random.randint(0, 8)
        linha, coluna = divmod(movimento, 3)
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = "O"
            break

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
modo = input("Digite '1' para jogar contra outro jogador ou '2' para jogar contra o computador: ")

jogador = "X"

while True:
    print_tabuleiro(tabuleiro)

    if modo == '1':
        movimento_jogador(tabuleiro, jogador)
    else:
        if jogador == "X":
            movimento_jogador(tabuleiro, jogador)
        else:
            computador(tabuleiro)
            print("\n")

    vencedor = check_tabuleiro(tabuleiro)
    if vencedor == "X" or vencedor == "O":
        print_tabuleiro(tabuleiro)
        print(f"Jogador {vencedor} ganhou!")
        break
    if empate(tabuleiro):
        print_tabuleiro(tabuleiro)
        print("Empate!")
        break

    jogador = "O" if jogador == "X" else "X"
