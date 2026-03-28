# Integrantes: [Victor da Silva Balduino], [NOME 2], [NOME 3]
# Fluxograma: [https://app.diagrams.net/#G1grp0yGL3JKgWUEY0B15WnftS2QdHKzZv / https://github.com/victotsb/Racioc-nio-Algor-tmico/blob/main/Fluxograma-Sobrevivencia-na-Ilha-Jogo.png]

"""versão sem def"""

import random
import time
import os

os.system("cls" if os.name == "nt" else "clear")
print("=" * 54)
print("SOBREVIVENCIA NA ILHA")
print("Um jogo de escolhas e instintos")
print("=" * 54)
print("Voce estava a bordo de um cargueiro quando uma")
print("tempestade feroz surgiu do nada. O barco afundou")
print("em questao de minutos. Agora, voce acorda sozinho")
print("numa ilha desconhecida, sem saber se alguem sabe")
print("que voce esta vivo.")
print()
print("Voce comeca com 100 pontos de energia.")
print("Cada decisao vai custar - ou render - energia.")
print("Sobreviva. Seja resgatado. Volte para casa.")
print("-" * 54)
input("Pressione ENTER para comecar...\n")

energia = 100
jogando = True

os.system("cls" if os.name == "nt" else "clear")
print("=" * 54)
print("CENARIO 1")
print("=" * 54)
print("O sol quente bate em sua pele. A areia umida esta")
print("colada no seu rosto. As ondas quebram perto de voce.")
print("Sua garganta esta seca. Seus musculos doem.")
print("Mas voce esta vivo.")
print()
print("Ao seu redor: praia aberta de um lado,")
print("floresta densa do outro.")
print()
print("O que voce faz?")
print("(1) Entrar na floresta em busca de recursos")
print("(2) Caminhar pela praia procurando sinais de vida")

escolha_c1 = ""
while escolha_c1 != "1" and escolha_c1 != "2":
    escolha_c1 = input("Sua escolha (1 ou 2): ").strip()
    if escolha_c1 != "1" and escolha_c1 != "2":
        print("Digite apenas 1 ou 2.")

perda_c1 = random.randint(20, 40)
energia = energia - perda_c1
if energia < 0:
    energia = 0

if escolha_c1 == "1":
    print("Voce caminha em direcao as arvores.")
    print("O calor abafa, mas a sombra alivia um pouco.")
else:
    print("Voce arrasta os pes pela areia quente.")
    print("O sol castiga sem piedade.")

time.sleep(0.4)
print("-" + str(perda_c1) + " pontos de energia!")
time.sleep(0.5)

blocos_cheios = energia // 10
barra = ""
i = 0
while i < blocos_cheios:
    barra = barra + "#"
    i = i + 1
j = blocos_cheios
while j < 10:
    barra = barra + "."
    j = j + 1
if energia > 70:
    estado = "Otimo"
elif energia > 30:
    estado = "Regular"
else:
    estado = "Critico"
print("-" * 54)
print("ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
print("-" * 54)

if energia <= 0:
    print("Voce ficou sem energia e nao resistiu a ilha...")
    print("FIM DE JOGO - tente novamente!")
    jogando = False

if jogando:
    input("[ENTER para continuar...]\n")

if jogando and escolha_c1 == "1":
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 54)
    print("CENARIO 2A")
    print("=" * 54)
    print("Entre as arvores, o ar e mais fresco. Voce ouve")
    print("o som de agua corrente e encontra um pequeno rio.")
    print("A agua parece cristalina - pelo menos e o que parece.")
    print()

    escolha_rio = ""
    while escolha_rio != "2" and jogando:
        blocos_cheios = energia // 10
        barra = ""
        i = 0
        while i < blocos_cheios:
            barra = barra + "#"
            i = i + 1
        j = blocos_cheios
        while j < 10:
            barra = barra + "."
            j = j + 1
        if energia > 70:
            estado = "Otimo"
        elif energia > 30:
            estado = "Regular"
        else:
            estado = "Critico"
        print("-" * 54)
        print("ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
        print("-" * 54)
        print("O que voce faz?")
        print("(1) Beber a agua do rio agora mesmo")
        print("(2) Procurar uma fonte de agua mais segura")

        escolha_rio = ""
        while escolha_rio != "1" and escolha_rio != "2":
            escolha_rio = input("Sua escolha (1 ou 2): ").strip()
            if escolha_rio != "1" and escolha_rio != "2":
                print("Digite apenas 1 ou 2.")

        if escolha_rio == "1":
            perda = random.randint(15, 35)
            energia = energia - perda
            if energia < 0:
                energia = 0
            print("Voce bebe com avidez... mas logo o estomago vira.")
            print("Tontura. Nausea. A agua estava contaminada.")
            time.sleep(0.4)
            print("-" + str(perda) + " pontos de energia!")
            time.sleep(0.5)

            blocos_cheios = energia // 10
            barra = ""
            i = 0
            while i < blocos_cheios:
                barra = barra + "#"
                i = i + 1
            j = blocos_cheios
            while j < 10:
                barra = barra + "."
                j = j + 1
            if energia > 70:
                estado = "Otimo"
            elif energia > 30:
                estado = "Regular"
            else:
                estado = "Critico"
            print("-" * 54)
            print("ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
            print("-" * 54)

            if energia <= 0:
                print("Voce ficou sem energia e nao resistiu a ilha...")
                print("FIM DE JOGO - tente novamente!")
                jogando = False
            else:
                print("Voce ainda tem sede. O que faz agora?")
                print()
                escolha_rio = ""
        else:
            ganho = random.randint(5, 15)
            energia = energia + ganho
            if energia > 100:
                energia = 100
            print("Voce acha um coqueiro carregado.")
            print("Agua de coco fresca! Voce sente um alivio imenso.")
            time.sleep(0.4)
            print("+" + str(ganho) + " pontos de energia!")
            time.sleep(0.5)

            blocos_cheios = energia // 10
            barra = ""
            i = 0
            while i < blocos_cheios:
                barra = barra + "#"
                i = i + 1
            j = blocos_cheios
            while j < 10:
                barra = barra + "."
                j = j + 1
            if energia > 70:
                estado = "Otimo"
            elif energia > 30:
                estado = "Regular"
            else:
                estado = "Critico"
            print("-" * 54)
            print("ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
            print("-" * 54)
            time.sleep(1)

    if jogando:
        input("[ENTER para continuar...]\n")

if jogando and escolha_c1 == "2":
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 54)
    print("CENARIO 2B")
    print("=" * 54)
    print("Voce caminha pela orla. O calor e intenso,")
    print("a fome aperta e suas pernas comecam a pesar.")
    print("Voce precisa de comida. E precisa agora.")
    print()

    blocos_cheios = energia // 10
    barra = ""
    i = 0
    while i < blocos_cheios:
        barra = barra + "#"
        i = i + 1
    j = blocos_cheios
    while j < 10:
        barra = barra + "."
        j = j + 1
    if energia > 70:
        estado = "Otimo"
    elif energia > 30:
        estado = "Regular"
    else:
        estado = "Critico"
    print("-" * 54)
    print("ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
    print("-" * 54)
    print("O que voce faz?")
    print("(1) Tentar cacar ou pescar")
    print("(2) Procurar frutas na mata proxima")

    escolha_c2b = ""
    while escolha_c2b != "1" and escolha_c2b != "2":
        escolha_c2b = input("Sua escolha (1 ou 2): ").strip()
        if escolha_c2b != "1" and escolha_c2b != "2":
            print("Digite apenas 1 ou 2.")

    if escolha_c2b == "1":
        perda = random.randint(15, 35)
        energia = energia - perda
        if energia < 0:
            energia = 0
        print("Voce passa horas tentando pescar com um graveto.")
        print("Nada. Os peixes parecem estar te zoando.")
        time.sleep(0.4)
        print("-" + str(perda) + " pontos de energia!")
        time.sleep(0.5)
    else:
        ganho = random.randint(10, 25)
        energia = energia + ganho
        if energia > 100:
            energia = 100
        print("Voce encontra bananeiras na beira da mata.")
        print("Come ate saciar. A energia volta aos poucos.")
        time.sleep(0.4)
        print("+" + str(ganho) + " pontos de energia!")
        time.sleep(0.5)

    blocos_cheios = energia // 10
    barra = ""
    i = 0
    while i < blocos_cheios:
        barra = barra + "#"
        i = i + 1
    j = blocos_cheios
    while j < 10:
        barra = barra + "."
        j = j + 1
    if energia > 70:
        estado = "Otimo"
    elif energia > 30:
        estado = "Regular"
    else:
        estado = "Critico"
    print("-" * 54)
    print("ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
    print("-" * 54)

    if energia <= 0:
        print("Voce ficou sem energia e nao resistiu a ilha...")
        print("FIM DE JOGO - tente novamente!")
        jogando = False

    if jogando:
        input("[ENTER para continuar...]\n")

if jogando:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 54)
    print("CENARIO 3")
    print("=" * 54)
    print("O ceu alaranjado avisa: o sol vai sumir em breve.")
    print("A temperatura cai e o vento sopra mais forte.")
    print("Voce encontra destrocos do barco: madeira, cordas,")
    print("tecido e uma caixa de fosforos - ainda seca.")
    print()

    blocos_cheios = energia // 10
    barra = ""
    i = 0
    while i < blocos_cheios:
        barra = barra + "#"
        i = i + 1
    j = blocos_cheios
    while j < 10:
        barra = barra + "."
        j = j + 1
    if energia > 70:
        estado = "Otimo"
    elif energia > 30:
        estado = "Regular"
    else:
        estado = "Critico"
    print("-" * 54)
    print("ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
    print("-" * 54)
    print("O que voce faz?")
    print("(1) Construir um abrigo para a noite")
    print("(2) Acender uma fogueira bem visivel")

    escolha_c3 = ""
    while escolha_c3 != "1" and escolha_c3 != "2":
        escolha_c3 = input("Sua escolha (1 ou 2): ").strip()
        if escolha_c3 != "1" and escolha_c3 != "2":
            print("Digite apenas 1 ou 2.")

    if escolha_c3 == "1":
        perda = random.randint(15, 30)
        energia = energia - perda
        if energia < 0:
            energia = 0
        print("Voce monta um abrigo improvisado com os destrocos.")
        print("Esta exausto, mas protegido.")
        print("Ao amanhecer, pescadores da ilha te encontram.")
        time.sleep(0.4)
        print("-" + str(perda) + " pontos de energia!")
        time.sleep(0.5)
    else:
        perda = random.randint(5, 15)
        energia = energia - perda
        if energia < 0:
            energia = 0
        print("Voce acende uma fogueira enorme na praia.")
        print("A fumaca sobe alta e visivel por quilometros.")
        print("Um navio de resgate aparece no horizonte.")
        time.sleep(0.4)
        print("-" + str(perda) + " pontos de energia!")
        time.sleep(0.5)

    blocos_cheios = energia // 10
    barra = ""
    i = 0
    while i < blocos_cheios:
        barra = barra + "#"
        i = i + 1
    j = blocos_cheios
    while j < 10:
        barra = barra + "."
        j = j + 1
    if energia > 70:
        estado = "Otimo"
    elif energia > 30:
        estado = "Regular"
    else:
        estado = "Critico"
    print("-" * 54)
    print("ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
    print("-" * 54)

    if energia <= 0:
        print("Voce ficou sem energia e nao resistiu a ilha...")
        print("FIM DE JOGO - tente novamente!")
        jogando = False

    if jogando:
        input("[ENTER para ver o desfecho...]\n")

if jogando:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 54)
    print("VOCE FOI RESGATADO!")
    print("=" * 54)
    print("O helicoptero pousa na praia.")
    print("A equipe de resgate corre em sua direcao.")
    print()

    blocos_cheios = energia // 10
    barra = ""
    i = 0
    while i < blocos_cheios:
        barra = barra + "#"
        i = i + 1
    j = blocos_cheios
    while j < 10:
        barra = barra + "."
        j = j + 1
    if energia > 70:
        estado = "Otimo"
    elif energia > 30:
        estado = "Regular"
    else:
        estado = "Critico"
    print("-" * 54)
    print("ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
    print("-" * 54)

    if energia > 70:
        print("FINAL ALEGRE")
        print("-" * 54)
        print("Voce esta tao bem que tira selfie com os socorristas.")
        print("Um deles te pede autografo. Voce passou ileso")
        print("e ja pensa em escrever um livro sobre a aventura.")
    elif energia >= 30:
        print("FINAL IRONICO")
        print("-" * 54)
        print("Voce esta vivo, mas parece que saiu de um filme")
        print("de zumbi. Mal consegue sorrir para o reporter.")
        print("Voce sobreviveu. E o suficiente. Por enquanto.")
    else:
        print("FINAL SURREAL")
        print("-" * 54)
        print("Voce esta deitado na areia murmurando sobre")
        print("coqueiros e fosforos. Confunde o medico com um peixe.")
        print("Vai precisar de muito cafe - e talvez de terapia.")

    print()
    print("=" * 54)
    print("Energia final: " + str(energia) + " / 100 pontos")
    print("=" * 54)

print()
print("Ate a proxima aventura, sobrevivente.")