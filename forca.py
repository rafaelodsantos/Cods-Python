from random import choice

def banco_palavras():
  palavras = [
    'afeganistao', 'albania', 'algeria', 'andorra', 'angola', 'antigua e barbuda', 'argelia', 'argentina', 
    'armenia', 'australia', 'austria', 'azerbaijao', 'bahamas', 'bahrein', 'bangladesh', 'barbados', 'bielorrussia',
    'belgica', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia e hercegovina', 'botswana', 'brasil', 'brunei', 
    'bulgaria', 'burkina faso', 'burundi', 'butao', 'caboverde', 'cambodia', 'camerun', 'canada', 'catar', 'chile',
    'china', 'chipre', 'colombia', 'comores', 'congo', 'coreia do norte', 'coreia do sul', 'costa do marfim', 'croacia', 
    'cuba', 'dinamarca', 'dominica', 'ecuador', 'egito', 'el salvador', 'emirados arabes unidos', 'equador', 'eritrea', 
    'eslovaquia', 'eslovenia', 'espanha', 'estados unidos', 'estonia', 'etiopia', 'fiji', 'filipinas', 'finlandia', 
    'franca', 'gabao', 'gambia', 'gania', 'georgia', 'gana', 'grenada', 'guatemala', 'guine', 'guine-bissau', 'guyana',
    'haiti', 'honduras', 'hungria', 'india', 'indonesia', 'irlanda', 'iraque', 'islandia', 'israel', 'italia', 
    'jamaica', 'japao', 'jordania', 'josefina', 'kiribati', 'kosovo', 'kuwait', 'laos', 'lesoto', 'letonia', 'libano',
    'liberia', 'libia', 'liechtenstein', 'lituania', 'luxemburgo', 'macedonia', 'madagascar', 'malasia', 'malawi', 
    'maldivas', 'mali', 'malta', 'marrocos', 'marshall', 'mauricio', 'mauritania', 'mexico', 'micronesia', 'mocambique', 
    'moldavia', 'monaco', 'mongolia', 'mozambique', 'namibia', 'nauru', 'nepal', 'nicaragua', 'niger', 'nigeria', 
    'noruega', 'nova zelandia', 'omao', 'ouganada', 'paises baixos', 'palau', 'panama', 'papua nova guine', 'paraguai', 
    'peru', 'polonia', 'portugal', 'quenia', 'reino unido', 'rep. dominicana', 'rep. tcheca', 'romenia', 'ruanda', 
    'russias', 'saint kitts e nevis', 'saint lucia', 'samoa', 'sao tome e principe', 'senegal', 'serbia', 'singapura', 
    'siria', 'somalia', 'sri lanka', 'suazilandia', 'suecia', 'suica', 'suriname', 'tailandia', 'tanzania', 'timor leste', 
    'togo', 'tonga', 'trinidad e tobago', 'tunisia', 'turcomenistao', 'turquia', 'tuvalu', 'uganda', 'uruguai', 'uzbequistao',
    'vanuatu', 'venezuela', 'vietna', 'zambia', 'zimbabue']


  return choice(palavras)

def jogo_da_forca():
  palavra = banco_palavras()
  letra_advinhada = []
  tentativas = 6
  tamanho = len(palavra)

  while tentativas != 0:
    estado_palavra=''.join(letra if letra in letra_advinhada or letra == ' ' else '_' for letra in palavra)
    
    print(f'Palavra: {estado_palavra}')
    print(f'N° Letras: {tamanho}')
    print(f'Tentativas: {tentativas}')

    if tentativas > 0 and estado_palavra == palavra:
      print(f'\nParabéns você acertou a palavra!')
      break

    letra=input('Digite uma letra: ').lower().strip() # Letras minusculas; Remove espaços extras
    
    if len(letra) != 1 and letra.isalpha(): # .isalpha() Verifica se é uma letra
      print('\nDigite apenas uma letra')
    
    if letra == palavra:
      print(f'\nParabéns você acertou a palavra!')
      break

    if letra in letra_advinhada:
      print(f'\nVocê já advinhou essa letra, tente novamente')

    if letra in list(palavra):
      print(f'\nVocê acertou uma letra')
     
    if len(letra) == 1 and letra not in palavra:
      tentativas -= 1
      print(f'\nLetra incorreta, tente outra')

    letra_advinhada.append(letra)
  
  if tentativas == 0:
      print(f'\nVocê perdeu, a palavra era "{palavra}"')
  
jogo_da_forca()


