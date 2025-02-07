tabuleiro = [[ '-' for _ in range(3)] for _ in range(3)]

def jogo():

  for linha in tabuleiro:
    print(*linha)
    
while True:

  jogo()

  linhas = int(input('Digite um numero de 1 a 3 para escolher a linha: '))
  linhas -= 1
  if linhas < 0 or linhas > 2:
    print('Digite apenas 1 2 3')
    
  coluna = int(input('Degite um numero de 1 a 3 para a coluna: '))
  coluna -= 1
  if coluna < 0 or coluna > 2:
    print('Digite apenas 1 2 3')

  valor = input('Agora escolha se voce é X ou O: ').upper()
  if valor not in ('O', 'X'):
    print('Digite apenas X ou O')

  if tabuleiro[linhas][coluna] != '-':
    print('Lugar ocupado')

  tabuleiro[linhas][coluna] = valor

  #usar um for
  if tabuleiro[0][0] == 'X' and tabuleiro[0][1] == 'X' and tabuleiro[0][1] == 'X':
    print('Jogador X ganhou!')
    break
  
  if tabuleiro[0][0] == 'O' and tabuleiro[0][1] == 'O' and tabuleiro[0][1] == 'O':
    print('Jogador O ganhou!')
    break

  if tabuleiro[1][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[1][1] == 'X':
    print('Jogador X ganhou!')
    break
  
  if tabuleiro[1][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[1][1] == 'O':
    print('Jogador 0 ganhou!')
    break

  if tabuleiro[2][0] == 'X' and tabuleiro[2][1] == 'X' and tabuleiro[2][1] == 'X':
    print('Jogador X ganhou!')
    break



  


