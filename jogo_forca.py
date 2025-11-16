# Gerar palavra aleatória
# Imprimir traços de acordo com o tamanho da palavra
# O jogador deve enviar uma letra, validar se é tipo string e tem apenas um caractere

# Verificar se a letra está na palavra
# Caso esteja, substituir os traços pela letra correta
# Caso não esteja, diminuir o número de tentativas
# Mostrar letras já utilizadas
# Finalizar o jogo quando o jogador acertar a palavra ou acabar as tentativas
import random

palavras = ['banana', 'abacaxi', 'laranja', 'melancia', 'uva', 'pera', 'manga', 'caju', 'goiaba', 'kiwi']

palavra = random.choice(palavras).lower()
quantidade_letras = len(palavra)

tracos = ['_'] * quantidade_letras
letras_usadas = []

tentativas = 7


#enumerate(palavra) retorna pares (índice, letra)
#palavra = "python" → enumerate(palavra) dá (0, 'p'), (1, 'y'), (2, 't'), ...

while tentativas > 0 and '_' in tracos:
    letra_escolhida = ''

    while len(letra_escolhida) != 1 or not letra_escolhida.isalpha(): # Validar entrada se é uma letra
        letra_escolhida = input("Digite uma letra: ").lower()[:1] # Limitar a um caractere

    if letra_escolhida in letras_usadas or letra_escolhida in tracos:
        print("Você já tentou essa letra!")
        continue

    letra_encontrada = False

    for indice, letra in enumerate(palavra):  
        if letra_escolhida == letra:
            tracos[indice] = letra_escolhida
            letra_encontrada = True

    if letra_encontrada:
        print(tracos)
    else:
        letras_usadas.append(letra_escolhida)
        tentativas -= 1

    print(f"Letras usadas: {letras_usadas}")
    print(f"Tentativas restantes: {tentativas}")
    print(tracos)

if '_' not in tracos:
    print("Parabéns! Você ganhou!")
elif tentativas == 0:
    print("Você não tem mais tentativas.")
    print("Você perdeu! A palavra era:", palavra)
else:
    print("Algo deu errado")

