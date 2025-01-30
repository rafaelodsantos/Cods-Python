from random import choice

def banco_palavras():
  palavras = [
    "arroz"]


  return choice(palavras)

def jogo_da_forca():
  palavra = banco_palavras()
  letra_advinhada = []
  tentativas = 3
  tamanho = len(palavra)

  while tentativas > 0:
    estado_palavra=''.join(letra if letra in letra_advinhada or letra == ' ' else '_' for letra in palavra)
    
    print(f'Palavra: {estado_palavra}')
    print(f'N° Letras: {tamanho}')
    print(f'Tentativas: {tentativas}')

    letra=input('Digite uma letra: ').lower()
    
    if letra == palavra:
      print(f'\nParabéns você acertou a palavra!')
      break

    if tentativas > 0 and estado_palavra in palavra:
      print(f'Parabéns você acertou a palavra!')
      break
    
    if letra in letra_advinhada:
      print(f'\nVocê já advinhou essa letra, tente novamente')

    if letra in list(palavra):
      print(f'\nVocê acertou uma letra')
     
    if letra not in palavra:
      tentativas -= 1
      print(f'\nLetra incorreta, tente outra')

    letra_advinhada.append(letra)
  
  if tentativas == 0:
      print(f'\nVocê perdeu, a palavra era "{palavra}"')
  
jogo_da_forca()


