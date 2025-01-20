from random import choice

def banco_palavras():
  palavras = [
    'minecraft', 'fortnite', 'among us', 'cyberpunk', 'the witcher', 'red dead redemption',
    'the legend of zelda', 'super mario odyssey', 'god of war', 'grand theft auto',
    'halo infinite', 'call of duty', 'apex legends', 'valorant', 'league of legends',
    'world of warcraft', 'overwatch', 'hollow knight', 'celeste', 'stardew valley', 'terraria', 'cuphead',
    'fall guys', 'pubg', 'the sims', 'animal crossing', 'genshin impact', 'assassins creed valhalla',
    'dark souls', 'bloodborne', 'sekiro shadows die twice', 'hades', 'dead cells', 'doom eternal',
    'resident evil village', 'persona', 'final fantasy', 'dragon quest', 'the last of us',
    'uncharted', 'spider man', 'ghost of tsushima', 'ratchet and clank', 'horizon zero dawn',
    'mass effect', 'elden ring', 'bioshock infinite', 'dishonored', 'control',
    'nier automata', 'monster hunter world', 'kingdom hearts', 'metroid dread', 'splatoon',
    'mario kart deluxe', 'smash bros ultimate', 'fire emblem three houses', 'xenoblade chronicles',
    'bayonetta', 'donkey kong country', 'yoshi crafted world', 'luigi mansion', 'octopath traveler',
    'bravely default', 'triangle strategy', 'shin megami tensei', 'deltarune',
    'undertale', 'bastion', 'transistor', 'pyre', 'frostpunk', 'cities skylines', 'the binding of isaac',
    'slay the spire', 'rogue legacy', 'spelunky', 'risk of rain', 'no man sky', 'subnautica',
    'outer wilds', 'the outer worlds', 'death stranding', 'control', 'hellblade senua sacrifice',
    'a plague tale innocence', 'the evil within', 'little nightmares', 'inside', 'limbo',
    'what remains of edith finch', 'gone home', 'firewatch', 'life is strange', 'telltale the walking dead',
    'detroit become human', 'heavy rain', 'beyond two souls', 'journey', 'flower', 'gris', 'ori and the blind forest',
    'ori and the will of the wisps', 'katana zero', 'enter the gungeon', 'the messenger', 'shovel knight'
]


  return choice(palavras)

def jogo_da_forca():
  palavra = banco_palavras()
  letra_advinhada = []
  tentativas = 6

  while tentativas > 0:
    estado_palavra=''.join(letra if letra in letra_advinhada or letra == ' ' else '_' for letra in palavra)
    print(f'Palavra: {estado_palavra}')
    print(f'Tentativas: {tentativas}')

    letra=input('Digite uma letra: ').lower()
    
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
  
  if tentativas == 0:
      print(f'Você perdeu, a palavra era "{palavra}"')

  


jogo_da_forca()


