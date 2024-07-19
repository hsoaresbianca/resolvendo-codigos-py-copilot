# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita o primeiro número do usuário
numero1 = int(input("Digite o primeiro número: "))

# Solicita o segundo número do usuário
numero2 = int(input("Digite o segundo número: "))

# Solicita a operação matemática do usuário
operacao = input("Digite a operação matemática (+, -, *, /): ")

# Realiza a operação matemática escolhida
if operacao == '+':
    print(numero1 + numero2)
elif operacao == '-':
    print(abs(numero1 - numero2))
elif operacao == '*':
    print(numero1 * numero2)
elif operacao == '/':
    if numero2 != 0:
        print(numero1 / numero2)
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida.")