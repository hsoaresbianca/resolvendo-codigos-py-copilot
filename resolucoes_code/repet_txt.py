# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado

# Solicita uma string do usuário
string_usuario = input("Digite uma string: ")

# Solicita um número do usuário
numero_usuario = int(input("Digite um número: "))

# Repete a string pelo número informado
resultado = (string_usuario + '') * numero_usuario

# Exibe o resultado
print("Resultado:", resultado)
