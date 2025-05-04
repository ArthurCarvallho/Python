print("-----Calculadora-----")

while True:
    print("Escolha uma operação:")
    print("'+' para soma\n'-' para subtração\n'*' para multiplicação\n'/' para divisão\n's' para sair")
    operacao = input("Digite a operação desejada: ")
    
    if operacao == 's': 
        break
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, insira números válidos.")
        continue

    if operacao == '+':
        total = num1 + num2
    elif operacao == '-':
        total = num1 - num2
    elif operacao == '*':
        total = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            continue
        total = num1 / num2
    else:
        print("Operação inválida. Tente novamente.")
        continue

    print("Resultado:", total)
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        break

print("Obrigado por usar a calculadora!")