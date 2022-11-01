def main():
  print('Escolha o tipo de calculo:')
  print('Soma - 1 ')
  print('Subtração - 2')
  print('Multiplicação - 3')
  escolha = input('$: ')

  if escolha == '1':
    x = int(input('Coloque o primeiro número: '))
    y = int(input('Coloque o segundo número: '))
    print(f'A soma total é de {x + y}!')
    main()


  elif escolha == '2':
    x = int(input('Coloque o primeiro número: '))
    y = int(input('Coloque o segundo número: '))
    print(f'A soma total é de {x - y}!')
    main()


  elif escolha == '3':
    x = int(input('Coloque o primeiro número: '))
    y = int(input('Coloque o segundo número: '))
    print(f'A soma total é de {x * y}!')
    main()

  else:
    print('Coloque um número válido...')
    main()



main()