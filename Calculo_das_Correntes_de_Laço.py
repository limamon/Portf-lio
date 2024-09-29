import numpy as np

def criar_matriz_resistencia(num_malhas, resistencias, interconexoes):
    matriz_resistencia = np.zeros((num_malhas, num_malhas))

    for i in range(num_malhas):
        matriz_resistencia[i][i] = sum(resistencias[i])

    for (i, j), resistencia in interconexoes.items():
        matriz_resistencia[i][j] -= resistencia
        matriz_resistencia[j][i] -= resistencia

    return matriz_resistencia

def criar_matriz_tensao(num_malhas, fontes_tensao):
    matriz_tensao = np.zeros((num_malhas, 1))

    for malha, tensao in fontes_tensao.items():
        matriz_tensao[malha] += tensao  # Acumula a tensão da malha

    return matriz_tensao

def correntes_de_laco(matriz_resistencia, matriz_tensao):
    try:
        # Inverte a matriz de resistência
        matriz_resistencia_inv = np.linalg.inv(matriz_resistencia)

        # Multiplica a matriz invertida pela matriz de tensão
        resultado = np.dot(matriz_resistencia_inv, matriz_tensao)

        return resultado
    except np.linalg.LinAlgError:
        print("Erro: A matriz de resistência não é inversível.")
        return None

num_malhas = int(input("Digite o número de malhas: "))
print("Se a resistência se repetir nas malhas não se incomode, isso será tratado no codigo")

resistencias = []
for i in range(num_malhas):
    resistencia_input = input(f"Digite as resistências da malha {i + 1} (separadas por espaço, ex: 50 10 100): ")
    resistencias.append(list(map(int, resistencia_input.split())))

interconexoes = {}
for i in range(num_malhas):
    for j in range(i + 1, num_malhas):
        resposta = input(f"Quais resistências estão entre a malha {i + 1} e a malha {j + 1}? ")
        if resposta:
            resistencias_interconexao = list(map(int, resposta.split()))
            total_resistencia = sum(resistencias_interconexao)
            interconexoes[(i, j)] = total_resistencia

matriz_resistencia = criar_matriz_resistencia(num_malhas, resistencias, interconexoes)
print("Matriz de Resistência:")
print(matriz_resistencia)

# Leitura das fontes de tensão
fontes_tensao = []
fontes_tensao = {i: 0 for i in range(num_malhas)}
fontes = []
print('''
Se atente ao sinal correto das fontes (sentido horário positivo)
Caso tenha dificuldade, pense em um ponto no meio da malha, e coloque uma flexa na fonte de tensão
Sendo que, a ponta da flexa está apontando para o sinal positivo (+) da fonte
Então veja, se a flexa está em sentido horário, caso esteja a fonte é positiva naquela malha, e ela poderá se negativa em outra
Tudo depende do referencial, não se preocupe
Também não se importe em repetir os valores da fontes, quando ela aparece em mais de uma malha
'''
      )

for i in range(num_malhas):
    fontes_input = input(f"Digite as fontes da malha {i + 1} (separadas por espaço): ")
    fontes.append(list(map(int, fontes_input.split())))
    fontes_tensao[i] = sum(fontes[i])

matriz_tensao = criar_matriz_tensao(num_malhas, fontes_tensao)
print("Matriz de Tensão:")
print(matriz_tensao)

resultado = correntes_de_laco(matriz_resistencia,matriz_tensao)

print("As correntes de laço do circuito são respectivamentes: ")
n = 0
for i in resultado:
    n += 1
    print(f"Corrente de lanço da malha {n} é {i[0]:.2f}")
