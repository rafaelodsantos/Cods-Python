import random

def banco_palavras():
  palavras=['carregador', 'algema', 'carta', 'poltrona', 'bandeira']
  return random.choice(palavras)

def jogo_da_forca():
  palavra = banco_palavras()
  letra_advinhada = []
  tentativas = 6

  while tentativas > 0:
    estado_palavra=''.join(letra if letra in letra_advinhada else '_' for letra in palavra)
    print(f'Palavra: {estado_palavra}')
    print(f'Tentativas: {tentativas}')

    letra=input('Digite uma letra: ').lower()

    if tentativas == 0:
      print(f'Você perdeu, a palavra era "{palavra}"')
      break
    
    if letra == palavra:
      print(f'Parabéns você acertou a palavra!')
      break

    if letra in letra_advinhada:
      print(f'Você já advinhou essa letra, tente novamente')
      continue

    letra_advinhada.append(letra)
    print(f'Continue')

    if letra not in palavra:
      tentativas -= 1
      print(f'Letra incorreta, tente outra')



jogo_da_forca()


