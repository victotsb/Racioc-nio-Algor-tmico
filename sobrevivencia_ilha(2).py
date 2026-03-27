# Integrantes: [Victor da Silva Balduino], [NOME 2], [NOME 3]
# Fluxograma: [https://app.diagrams.net/#G1grp0yGL3JKgWUEY0B15WnftS2QdHKzZv#%7B%22pageId%22%3A%22R7tzPAh8Mn0mJ306VsZo%22%7D / https://github.com/victotsb/Racioc-nio-Algor-tmico/blob/main/Fluxograma-Sobrevivencia-na-Ilha-Jogo.png]

import random
import time
import os

os.system("cls" if os.name == "nt" else "clear")
print("-" * 54)
print("SOBREVIVENCIA NA ILHA")
print("Um jogo de escolhas e instintos")
print("-" * 54)

for caractere in "Voce estava a bordo de um cargueiro quando uma":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "tempestade feroz surgiu do nada. O barco afundou":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "em questao de minutos. Agora, voce acorda sozinho":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "numa ilha desconhecida, sem saber se alguem sabe":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "que voce esta vivo.":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
print()
for caractere in "Voce comeca com 100 pontos de energia.":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "Cada decisao vai custar - ou render - energia.":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "Sobreviva. Seja resgatado. Volte para casa.":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
print("-" * 54)
input("  Pressione ENTER para comecar...\n")

energia = 100
jogando = True

os.system("cls" if os.name == "nt" else "clear")
print("=" * 54)
print("CENARIO 1")
print("=" * 54)

for caractere in "O sol quente bate em sua pele. A areia umida esta":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "colada no seu rosto. As ondas quebram perto de voce.":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "Sua garganta esta seca. Seus musculos doem.":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "Mas voce esta vivo.":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
print()
for caractere in "Ao seu redor: praia aberta de um lado,":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
for caractere in "floresta densa do outro.":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
print()

print("O que voce faz?")
print("(1) Entrar na floresta em busca de recursos")
print("(2) Caminhar pela praia procurando sinais de vida")
escolha_c1 = ""
while escolha_c1 != "1" and escolha_c1 != "2":
    escolha_c1 = input("  Sua escolha (1 ou 2): ").strip()
    if escolha_c1 != "1" and escolha_c1 != "2":
        print("Digite apenas 1 ou 2.")

perda_c1 = random.randint(20, 40)
energia = energia - perda_c1
if energia > 100:
    energia = 100
if energia < 0:
    energia = 0

if escolha_c1 == "1":
    for caractere in "Voce caminha em direcao as arvores.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "O calor abafa, mas a sombra alivia um pouco.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
else:
    for caractere in "Voce arrasta os pes pela areia quente.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "O sol castiga sem piedade.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()

time.sleep(0.4)
for caractere in "  -" + str(perda_c1) + "pontos de energia!":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()
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
    print("=" * 54)
    for caractere in "Voce ficou sem energia e nao resistiu a ilha...":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "A natureza venceu desta vez.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    print("=" * 54)
    for caractere in "FIM DE JOGO - tente novamente!":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    jogando = False

if jogando:
    input("[ENTER para continuar...]\n")

if jogando and escolha_c1 == "1":
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 54)
    print("CENARIO 2A")
    print("=" * 54)

    for caractere in "Entre as arvores, o ar e mais fresco. Voce ouve":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "o som de agua corrente e encontra um pequeno rio.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "A agua parece cristalina - pelo menos e o que parece.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
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
            escolha_rio = input("  Sua escolha (1 ou 2): ").strip()
            if escolha_rio != "1" and escolha_rio != "2":
                print("Digite apenas 1 ou 2.")

        if escolha_rio == "1":
            perda = random.randint(15, 35)
            energia = energia - perda
            if energia > 100:
                energia = 100
            if energia < 0:
                energia = 0
            for caractere in "Voce bebe com avidez... mas logo o estomago vira.":
                print(caractere, end="", flush=True)
                time.sleep(0.018)
            print()
            for caractere in "Tontura. Nausea. A agua estava contaminada.":
                print(caractere, end="", flush=True)
                time.sleep(0.018)
            print()
            time.sleep(0.4)
            for caractere in "  -" + str(perda) + "pontos de energia!":
                print(caractere, end="", flush=True)
                time.sleep(0.018)
            print()
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
                print("=" * 54)
                for caractere in "Voce ficou sem energia e nao resistiu a ilha...":
                    print(caractere, end="", flush=True)
                    time.sleep(0.018)
                print()
                for caractere in "A natureza venceu desta vez.":
                    print(caractere, end="", flush=True)
                    time.sleep(0.018)
                print()
                print("=" * 54)
                for caractere in "FIM DE JOGO - tente novamente!":
                    print(caractere, end="", flush=True)
                    time.sleep(0.018)
                print()
                jogando = False
            else:
                for caractere in "Voce ainda tem sede. O que faz agora?":
                    print(caractere, end="", flush=True)
                    time.sleep(0.018)
                print()
                print()
                escolha_rio = ""

        else:
            ganho = random.randint(5, 15)
            energia = energia + ganho
            if energia > 100:
                energia = 100
            if energia < 0:
                energia = 0
            for caractere in "Voce acha um coqueiro carregado.":
                print(caractere, end="", flush=True)
                time.sleep(0.018)
            print()
            for caractere in "Agua de coco fresca! Voce sente um alivio imenso.":
                print(caractere, end="", flush=True)
                time.sleep(0.018)
            print()
            time.sleep(0.4)
            for caractere in "  +" + str(ganho) + "pontos de energia!":
                print(caractere, end="", flush=True)
                time.sleep(0.018)
            print()
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

    for caractere in "Voce caminha pela orla. O calor e intenso,":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "a fome aperta e suas pernas comecam a pesar.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "Voce precisa de comida. E precisa agora.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
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
        escolha_c2b = input("  Sua escolha (1 ou 2): ").strip()
        if escolha_c2b != "1" and escolha_c2b != "2":
            print("Digite apenas 1 ou 2.")

    if escolha_c2b == "1":
        perda = random.randint(15, 35)
        energia = energia - perda
        if energia > 100:
            energia = 100
        if energia < 0:
            energia = 0
        for caractere in "Voce passa horas tentando pescar com um graveto.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "Nada. Os peixes parecem estar te zoando.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        time.sleep(0.4)
        for caractere in "  -" + str(perda) + "pontos de energia!":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        time.sleep(0.5)
    else:
        ganho = random.randint(10, 25)
        energia = energia + ganho
        if energia > 100:
            energia = 100
        if energia < 0:
            energia = 0
        for caractere in "Voce encontra bananeiras na beira da mata.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "Come ate saciar. A energia volta aos poucos.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        time.sleep(0.4)
        for caractere in "  +" + str(ganho) + "pontos de energia!":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
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
        print("=" * 54)
        for caractere in "Voce ficou sem energia e nao resistiu a ilha...":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "A natureza venceu desta vez.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        print("=" * 54)
        for caractere in "FIM DE JOGO - tente novamente!":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        jogando = False

    if jogando:
        input("[ENTER para continuar...]\n")

if jogando:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 54)
    print("CENARIO 3")
    print("=" * 54)

    for caractere in "O ceu alaranjado avisa: o sol vai sumir em breve.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "A temperatura cai e o vento sopra mais forte.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "Voce encontra destrocos do barco: madeira, cordas,":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "tecido e uma caixa de fosforos - ainda seca.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
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
        if energia > 100:
            energia = 100
        if energia < 0:
            energia = 0
        for caractere in "Voce monta um abrigo improvisado com os destrocos.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "Esta exausto, mas protegido.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "Ao amanhecer, pescadores da ilha te encontram.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        time.sleep(0.4)
        for caractere in "  -" + str(perda) + "pontos de energia!":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        time.sleep(0.5)
    else:
        perda = random.randint(5, 15)
        energia = energia - perda
        if energia > 100:
            energia = 100
        if energia < 0:
            energia = 0
        for caractere in "Voce acende uma fogueira enorme na praia.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "A fumaca sobe alta e visivel por quilometros.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "Um navio de resgate aparece no horizonte.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        time.sleep(0.4)
        for caractere in "  -" + str(perda) + "pontos de energia!":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
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
        print("=" * 54)
        for caractere in "Voce ficou sem energia e nao resistiu a ilha...":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "A natureza venceu desta vez.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        print("=" * 54)
        for caractere in "FIM DE JOGO - tente novamente!":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        jogando = False

    if jogando:
        input("[ENTER para ver o desfecho...]\n")

if jogando:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 54)
    print("VOCE FOI RESGATADO!")
    print("=" * 54)

    for caractere in "O helicoptero pousa na praia.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
    for caractere in "A equipe de resgate corre em sua direcao.":
        print(caractere, end="", flush=True)
        time.sleep(0.018)
    print()
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
        for caractere in "Voce esta tao bem que tira selfie com os socorristas.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "Um deles te pede autografo. Voce passou ileso":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "e ja pensa em escrever um livro sobre a aventura.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
    elif energia >= 30:
        print("FINAL IRONICO")
        print("-" * 54)
        for caractere in "Voce esta vivo, mas parece que saiu de um filme":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "de zumbi. Mal consegue sorrir para o reporter.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "Voce sobreviveu. E o suficiente. Por enquanto.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
    else:
        print("FINAL SURREAL")
        print("-" * 54)
        for caractere in "Voce esta deitado na areia murmurando sobre":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "coqueiros e fosforos. Confunde o medico com um peixe.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()
        for caractere in "Vai precisar de muito cafe - e talvez de terapia.":
            print(caractere, end="", flush=True)
            time.sleep(0.018)
        print()

    print()
    print("=" * 54)
    print("Energia final: " + str(energia) + " / 100 pontos")
    print("=" * 54)

print()
print("-" * 54)
for caractere in "Ate a proxima aventura, sobrevivente.":
    print(caractere, end="", flush=True)
    time.sleep(0.018)
print()