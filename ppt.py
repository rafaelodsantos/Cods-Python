from random import choice

def chute_pc():
  escolhapc = ['pedra', 'papel', 'tesoura']
  return choice(escolhapc)

def ppt():
  regras = {
    "pedra": "tesoura",  # Pedra ganha de Tesoura
    "papel": "pedra",    # Papel ganha de Pedra
    "tesoura": "papel"   # Tesoura ganha de Papel
}

  print('\nVamos jogar pedra papel e tesoura')
  modo=input('1 - Casual\n2 - Melhor de\nEscolha o modo:')

  if modo == '1':
    chutepc = chute_pc()
    escolhajg=input('Pedra, Papel ou Tesoura:')

    if escolhajg == chutepc:
      print(f'Empate! Ambos escolheram {escolhajg}')
  
    if regras[escolhajg] == chutepc:
      print(f'Venceu, o camputador escolheu {chutepc}')
    else:
      print(f'f, o camputador escolheu {chutepc}')

    jogo=input('Deseja ir denvo? (s/n)')
    if jogo == 's':
      ppt()

  elif modo == '2':
    placarjg = 0
    placarpc = 0

    while placarjg or placarpc <= 3:
      
      chutepc = chute_pc()
      escolhajg=input('Pedra, Papel ou Tesoura:')

      if escolhajg == chutepc:
        print(f'Empate! Ambos escolheram {escolhajg}')
        print(f'Jogador = {placarjg} / PC = {placarpc}')
  
      elif regras[escolhajg] == chutepc:
        print(f'Venceu, o camputador escolheu {chutepc}')
        placarjg += 1
        print(f'Jogador = {placarjg} / PC = {placarpc}')

      else:
        print(f'f, o camputador escolheu {chutepc}')
        placarpc += 1
        print(f'Jogador = {placarjg} / PC = {placarpc}')

    if placarjg or placarpc == 3:
      jogo=input('Deseja ir denvo? (s/n)')
      if jogo == 's':
        ppt()

ppt()