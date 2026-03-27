# Integrantes: [Victor da Silva Balduino], [NOME 2]
# Fluxograma: [https://app.diagrams.net/#G1grp0yGL3JKgWUEY0B15WnftS2QdHKzZv#%7B%22pageId%22%3A%22R7tzPAh8Mn0mJ306VsZo%22%7D / https://github.com/victotsb/Racioc-nio-Algor-tmico/blob/main/Fluxograma-Sobrevivencia-na-Ilha-Jogo.png]

import random
import time
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar(segundos):
    time.sleep(segundos)

def aleatorio(a, b):
    return random.randint(a, b)

def limitar_energia(energia):
    if energia > 100:
        energia = 100
    if energia < 0:
        energia = 0
    return energia

def digitar(texto, velocidade=0.018):
    for caractere in texto:
        print(caractere, end="", flush=True)
        time.sleep(velocidade)
    print()

def linha(caractere="-", tamanho=54):
    print(caractere * tamanho)

def cabecalho(titulo):
    linha("=")
    espacos = (54 - len(titulo)) // 2
    if espacos < 0:
        espacos = 0
    print(" " * espacos + titulo)
    linha("=")

def exibir_energia(energia):
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
    linha()
    print("  ENERGIA  [" + barra + "]  " + str(energia) + "/100  |  " + estado)
    linha()

def ler_escolha(opcao_a, opcao_b):
    print("  O que voce faz?")
    print("  (1) " + opcao_a)
    print("  (2) " + opcao_b)
    while True:
        escolha = input("  Sua escolha (1 ou 2): ").strip()
        if escolha == "1" or escolha == "2":
            return escolha
        print("  Digite apenas 1 ou 2.")

def verificar_morte(energia):
    if energia <= 0:
        linha("=")
        digitar("  Voce ficou sem energia e nao resistiu a ilha...")
        digitar("  A natureza venceu desta vez.")
        linha("=")
        digitar("  FIM DE JOGO - tente novamente!")
        return True
    return False

def mostrar_impacto(valor, ganhou):
    pausar(0.4)
    if ganhou:
        digitar("  +" + str(valor) + " pontos de energia!")
    else:
        digitar("  -" + str(valor) + " pontos de energia!")
    pausar(0.5)

def tela_titulo():
    limpar_tela()
    linha("=")
    print("          SOBREVIVENCIA NA ILHA")
    print("      Um jogo de escolhas e instintos")
    linha("=")
    digitar("  Voce estava a bordo de um cargueiro quando uma")
    digitar("  tempestade feroz surgiu do nada. O barco afundou")
    digitar("  em questao de minutos. Agora, voce acorda sozinho")
    digitar("  numa ilha desconhecida, sem saber se alguem sabe")
    digitar("  que voce esta vivo.")
    print()
    digitar("  Voce comeca com 100 pontos de energia.")
    digitar("  Cada decisao vai custar - ou render - energia.")
    digitar("  Sobreviva. Seja resgatado. Volte para casa.")
    linha()
    input("  Pressione ENTER para comecar...\n")

def cenario_1():
    limpar_tela()
    cabecalho("CENARIO 1")
    digitar("  O sol quente bate em sua pele. A areia umida esta")
    digitar("  colada no seu rosto. As ondas quebram perto de voce.")
    digitar("  Sua garganta esta seca. Seus musculos doem.")
    digitar("  Mas voce esta vivo.")
    print()
    digitar("  Ao seu redor: praia aberta de um lado,")
    digitar("  floresta densa do outro.")
    print()
    escolha = ler_escolha(
        "Entrar na floresta em busca de recursos",
        "Caminhar pela praia procurando sinais de vida"
    )
    perda = aleatorio(20, 40)
    if escolha == "1":
        digitar("  Voce caminha em direcao as arvores.")
        digitar("  O calor abafa, mas a sombra alivia um pouco.")
    else:
        digitar("  Voce arrasta os pes pela areia quente.")
        digitar("  O sol castiga sem piedade.")
    mostrar_impacto(perda, False)
    return escolha, perda

def cenario_2a(energia):
    limpar_tela()
    cabecalho("CENARIO 2A")
    digitar("  Entre as arvores, o ar e mais fresco. Voce ouve")
    digitar("  o som de agua corrente e encontra um pequeno rio.")
    digitar("  A agua parece cristalina - pelo menos e o que parece.")
    print()
    while True:
        exibir_energia(energia)
        escolha = ler_escolha(
            "Beber a agua do rio agora mesmo",
            "Procurar uma fonte de agua mais segura"
        )
        if escolha == "1":
            perda = aleatorio(15, 35)
            energia = energia - perda
            energia = limitar_energia(energia)
            digitar("  Voce bebe com avidez... mas logo o estomago vira.")
            digitar("  Tontura. Nausea. A agua estava contaminada.")
            mostrar_impacto(perda, False)
            exibir_energia(energia)
            if verificar_morte(energia):
                return energia, True
            digitar("  Voce ainda tem sede. O que faz agora?")
            print()
        else:
            ganho = aleatorio(5, 15)
            energia = energia + ganho
            energia = limitar_energia(energia)
            digitar("  Voce acha um coqueiro carregado.")
            digitar("  Agua de coco fresca! Voce sente um alivio imenso.")
            mostrar_impacto(ganho, True)
            exibir_energia(energia)
            pausar(1)
            break
    return energia, False

def cenario_2b(energia):
    limpar_tela()
    cabecalho("CENARIO 2B")
    digitar("  Voce caminha pela orla. O calor e intenso,")
    digitar("  a fome aperta e suas pernas comecam a pesar.")
    digitar("  Voce precisa de comida. E precisa agora.")
    print()
    exibir_energia(energia)
    escolha = ler_escolha(
        "Tentar cacar ou pescar",
        "Procurar frutas na mata proxima"
    )
    if escolha == "1":
        perda = aleatorio(15, 35)
        energia = energia - perda
        energia = limitar_energia(energia)
        digitar("  Voce passa horas tentando pescar com um graveto.")
        digitar("  Nada. Os peixes parecem estar te zoando.")
        mostrar_impacto(perda, False)
    else:
        ganho = aleatorio(10, 25)
        energia = energia + ganho
        energia = limitar_energia(energia)
        digitar("  Voce encontra bananeiras na beira da mata.")
        digitar("  Come ate saciar. A energia volta aos poucos.")
        mostrar_impacto(ganho, True)
    exibir_energia(energia)
    if verificar_morte(energia):
        return energia, True
    return energia, False

def cenario_3(energia):
    limpar_tela()
    cabecalho("CENARIO 3")
    digitar("  O ceu alaranjado avisa: o sol vai sumir em breve.")
    digitar("  A temperatura cai e o vento sopra mais forte.")
    digitar("  Voce encontra destrocos do barco: madeira, cordas,")
    digitar("  tecido e uma caixa de fosforos - ainda seca.")
    print()
    exibir_energia(energia)
    escolha = ler_escolha(
        "Construir um abrigo para a noite",
        "Acender uma fogueira bem visivel"
    )
    if escolha == "1":
        perda = aleatorio(15, 30)
        energia = energia - perda
        energia = limitar_energia(energia)
        digitar("  Voce monta um abrigo improvisado com os destrocos.")
        digitar("  Esta exausto, mas protegido.")
        digitar("  Ao amanhecer, pescadores da ilha te encontram.")
        mostrar_impacto(perda, False)
    else:
        perda = aleatorio(5, 15)
        energia = energia - perda
        energia = limitar_energia(energia)
        digitar("  Voce acende uma fogueira enorme na praia.")
        digitar("  A fumaca sobe alta e visivel por quilometros.")
        digitar("  Um navio de resgate aparece no horizonte.")
        mostrar_impacto(perda, False)
    exibir_energia(energia)
    if verificar_morte(energia):
        return energia, True
    return energia, False

def resultado_final(energia):
    limpar_tela()
    cabecalho("VOCE FOI RESGATADO!")
    digitar("  O helicoptero pousa na praia.")
    digitar("  A equipe de resgate corre em sua direcao.")
    print()
    exibir_energia(energia)
    if energia > 70:
        print("  FINAL ALEGRE")
        linha()
        digitar("  Voce esta tao bem que tira selfie com os socorristas.")
        digitar("  Um deles te pede autografo. Voce passou ileso")
        digitar("  e ja pensa em escrever um livro sobre a aventura.")
    elif energia >= 30:
        print("  FINAL IRONICO")
        linha()
        digitar("  Voce esta vivo, mas parece que saiu de um filme")
        digitar("  de zumbi. Mal consegue sorrir para o reporter.")
        digitar("  Voce sobreviveu. E o suficiente. Por enquanto.")
    else:
        print("  FINAL SURREAL")
        linha()
        digitar("  Voce esta deitado na areia murmurando sobre")
        digitar("  coqueiros e fosforos. Confunde o medico com um peixe.")
        digitar("  Vai precisar de muito cafe - e talvez de terapia.")
    print()
    linha("=")
    print("  Energia final: " + str(energia) + " / 100 pontos")
    linha("=")

def main():
    tela_titulo()
    energia = 100
    escolha_c1, perda_c1 = cenario_1()
    energia = energia - perda_c1
    energia = limitar_energia(energia)
    exibir_energia(energia)
    if verificar_morte(energia):
        return
    input("  [ENTER para continuar...]\n")
    morreu = False
    if escolha_c1 == "1":
        energia, morreu = cenario_2a(energia)
    else:
        energia, morreu = cenario_2b(energia)
    if morreu:
        return
    input("  [ENTER para continuar...]\n")
    energia, morreu = cenario_3(energia)
    if morreu:
        return
    input("  [ENTER para ver o desfecho...]\n")
    resultado_final(energia)
    print()
    linha()
    novamente = input("  Jogar novamente? (s/n): ").strip().lower()
    if novamente == "s":
        main()
    else:
        digitar("  Ate a proxima aventura, sobrevivente.")

main()
