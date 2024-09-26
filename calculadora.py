#adição, subtração, divisão, multiplicação, porcentagem, potencia, raiz

#adição
def soma (x,y):
  return x + y

#subtração
def subtracao (x,y):
  return x - y

#multiplicação
def multiplicacao (x,y):
  return x * y

#divisão
def divisao (x,y):
  if y != 0:
    return x / y
  else:
    return print("Error")

#porcentagem
def porcentagem (x,y):
  return x / 100 * y

#potencia
def potencia (x,y):
  return x ** y

#raiz
def raiz (x):
  return x ** 0.5

def calculadora():
  print("Escolha sua operacao:")
  print("1. Adição")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  print("5. Porcentagem")
  print("6. Potencia")
  print("7. Raiz Quadrada")

  while True:
    escolha=input("1, 2, 3, 4, 5, 6, 7: ")

    if escolha in ['1', '2', '3', '4', '5', '6' , '7']:
      num1 = float(input("Escolha o primeiro número: "))

      if escolha == '7':
        resultado = raiz(num1)
        print(resultado)

        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
          break

      num2 = float(input("Escolha o segundo número (coloque zero se for raiz): "))

      if escolha == '1':
        resultado = soma(num1,num2)
        print(resultado)

      elif escolha == '2':
        resultado = subtracao(num1,num2)
        print(resultado)

      elif escolha == '3':
        resultado = multiplicacao(num1,num2)
        print(resultado)

      elif escolha == '4':
        resultado = divisao(num1,num2)
        print(resultado)
      
      elif escolha == '5':
        resultado = porcentagem(num1,num2)
        print(resultado)

      elif escolha == '6':
        resultado = potencia(num1,num2)
        print(resultado)

      continuar = input("Deseja realizar outra operação? (s/n): ")
      if continuar.lower() != 's':
        break
    
    else:
      print("Opção inválida")

calculadora()