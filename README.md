 <h1 style="text-align: center;">JOGO DA <b style="color: green;">F</b> <b style="color: red;">O</b> R <b style="color: red;">C</b> <b style="color: green;">A</b>. </h1>
 <p>
        Este é um jogo simples da forca em Python. O programa sorteia uma palavra 
        aleatória e o jogador tenta adivinhar a palavra, digitando uma letra por vez.
</p>

<h2 style="text-align:center;">Instruções</h2>    
<ol>
    <li>Certifique-se de ter o Python instalado em seu sistema.</li>
    <li>Baixe os arquivos `sorteio.py` e `linha.py` no mesmo diretório que este script.</li>
    <li>Execute o script `forca.py` no terminal.</li>
</ol>


<h2 style="text-align: center;">Como Jogar</h2>

<ol>
    <li>O programa escolhe aleatoriamente uma palavra.</li>
    <li>Você tem 5 chances para adivinhar a palavra</li>
    <li>Digite uma letra a cada rodada.</li>
    <li>O programa informará se você acertou ou errou.</li>
    <li>Você ganha se adivinhar a palavra ou perde se ficar sem chances.</li>
</ol>



<h2 style="text-align: center;">Inicialização de Variáveis</h2>

<p>
palavra_sorteada = palavra_sort().lower()<br>
letras = []<br>
ganhou = False<br>
contador = 5
</p>

<li><b>palavra_sorteada:</b> Obtém uma palavra sorteada e a converte para minúsculas.</li>
<li><b>letras:</b> Lista de letras corretamente adivinhadas.</li>
<li><b>ganhou:</b> Flag que indica se o jogador ganhou o jogo.</li>
<li><b>contador:</b> Número de chances que o jogador tem.</li>

<h2 style="text-align:center">Apresentação do Jogo</h2><br>

<p>
    linha()<br>
    print("======== Vamos jogar o jogo da forca ========".center(80))<br>
    linha()
</p>

<p style="text-align:center"><u>Funções para desenhar linhas e apresentar uma mensagem estilizada.</u></p>

<h2 style="text-align: center;">Como Funciona:</h2>

<ol>
<b><li>Inicialização:</li></b>
<ul>
<li>Uma palavra é sorteada, e o jogo começa com 5 chances.</li></ul>
<br>
<b><li>Entrada do Jogador:</li></b>
<ul>
<li>O jogador digita uma letra.</li>
</ul>
<br>
<b><li>Atualização das Letras:</li></b>
<ul><li>Se a letra estiver na palavra, ela é adicionada à lista de letras corretas.li></ul><br>
<b><li>Análise e Exibição:</li></b>
<ul>
    <li>A palavra é exibida com letras corretas reveladas e espaços ocultos.</li>
</ul>
<br>
<b><li>Atualização das Chances:</li></b>
<ul>
    <li>
        As chances diminuem se a letra digitada estiver errada.
    </li>
</ul>
<br>
<b><li>Verificação de Vitória ou Derrota:</li></b>
<ul>
    <li>O jogo verifica se o jogador acertou todas as letras ou perdeu todas achances.</li>
</ul>
<br>
<b><li>Mensagem de Resultado:</li></b>
<ul>
    <li>O jogo exibe uma mensagem indicando se o jogador ganhou ou perdeu.</li>
    </ul></ol>
<br>
<h2>Loop While:</h2>
<br>

    while True:
    # Entrada do Jogador
    letra_jogador = input("\nDigite uma letra: ").lower()

    # Verifica se a letra está na palavra sorteada
    if letra_jogador in palavra_sorteada:
        letras.append(letra_jogador)

    # Estética do código
    print("\n")
    linha()
    print("======== Analisando ========".center(80))
    linha()
    sleep(1)

    # Exibe a palavra com letras reveladas e espaços ocultos
    for letra in palavra_sorteada:
        if letra in letras:
            print(letra, end='  ')
        else:
            print('-', end='  ')

    # Verifica se a letra digitada está correta e atualiza as chances
    if letra_jogador in palavra_sorteada:
        print(f"\nAcertou, você tem {contador} chances")
    elif letra_jogador not in palavra_sorteada:
        contador -= 1
        print(f"\nErrou, você tem {contador} chances")
        if contador == 0:
            print(f"\nVocê Perdeu a palavra correta era {palavra_sorteada}")

    # Verifica se o jogador ganhou
    ganhou = all(letra in letras for letra in palavra_sorteada)

    # Condição de parada
    if contador == 0 or ganhou:
        break

<h2>Condição caso o usuário ganhe o jogo:</h2>

    if ganhou:
        print(f"Você ganhou!!! A palavra era {palavra_sorteada}.")