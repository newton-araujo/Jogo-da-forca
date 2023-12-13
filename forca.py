from sorteio import palavra_sort
from time import sleep
from linha import linha

#Variaveis
palavra_sorteada = palavra_sort().lower() #Função criada para sortear uma palavra.
letras = [] #Lista de letras
ganhou = False 
contador = 5

#Estética do código
linha()
print("======== Vamos jogar o jogo da forca ========".center(80))
linha()

#Criando o loop para instanciar o código.
while True:
    letra_jogador = input("\nDigite uma letra: ").lower()
    #Aqui, a lista de letras recebe as letras caso elas estejam na palavra sorteada.
    if letra_jogador in palavra_sorteada:
        letras.append(letra_jogador)

    #Estética do código
    print("\n")
    linha()
    print("======== Analisando ========".center(80))
    linha()
    sleep(1)

    """ Percorre toda a palavra e identifica todas as letras. Foi criada uma condição que verifica se a letra está na palavra. Caso a letra esteja na palavra,
      ela mantém sua posição; caso contrário, ela é ocultada, sendo mantida por um " - ". """
    for letra in palavra_sorteada:
        if letra in letras:
            print(letra, end='  '.center())
        else:
            print('-', end='  ')
    

    """
    Verificamos se a palavra digitada pelo usuário está presente na palavra. Caso a letra informada esteja correta, o usuário poderá tentar acertar a palavra 
    sem perder número de chances. Caso contrário, ele perde uma chance por letra errada.

    Criamos uma condição para que, se o usuário perder todas as chances, ele perderá o jogo.

    """
    if letra_jogador in palavra_sorteada:
        print(f"\nAcertou, você tem {contador} chances")
    elif letra_jogador not in palavra_sorteada:
        contador -= 1
        print(f"\nErrou, você tem {contador} chances")
        if contador == 0:
            print(f"\nVocê Perdeu a palavra correta era {palavra_sorteada}")
            

    """
    Alteramos o status de "ganhou" para verdadeiro; após isso, instanciamos uma condição para verificar se todas as letras que estão na palavra 
    estão na lista. Se sim, o usuário ganhou a partida.

    """
    ganhou = True

    for letra in palavra_sorteada:
        if letra not in letras:
            ganhou = False
    

    """
    Condição de parada.
    """
    if contador == 0 or ganhou:
        break


if ganhou:
    print(f"Você ganhou!!! A palavra era {palavra_sorteada}.")


    
