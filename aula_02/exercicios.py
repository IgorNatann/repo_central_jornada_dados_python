# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
number_1 = int(input("Digite o primeiro numero inteiro: "))
number_2 = int(input("Digite o segundo numero inteiro:"))

result = number_1 + number_2

print(f"A soma de {number_1} e {number_2} é: {result}")
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
number = int(input("Digite um numero inteiro: "))

result = number % 5

print(f"O resto da divisão de {number} por 5 é: {result}")
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
number_1 = int(input("Digite o primeiro numero inteiro: "))
number_2 = int(input("Digite o segundo numero inteiro: "))

result = number_1 * number_2

print(f"O produto de {number_1} e {number_2} e: {result}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
number_1 = int(input("Digite o primeiro numero inteiro: "))
number_2 = int(input("Digite o segundo numero inteiro: "))

result = number_1 // number_2

print(f"A divisao inteira de {number_1} por {number_2} e: {result}")
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
number = int(input("Digite um numero inteiro: "))

result = number ** 2

print(f"O quadrado de {number} e: {result}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
number_1 = float(input("Digite o primeiro numero flutuante: "))
number_2 = float(input("Digite o segundo numero flutuante: "))

result = number_1 + number_2

print(f"A soma de {number_1} e {number_2} é: {result}")
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
number_1 = float(input("Digite o primeiro numero flutuante: "))
number_2 = float(input("Digite o segundo numero flutuante: "))

result = (number_1 + number_2) / 2

print(f"A média de {number_1} e {number_2} é: {result}")
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base (numero flutuante): "))
exponent = float(input("Digite o expoente (numero flutuante): "))

result = base ** exponent

print(f"A potência de {base} elevado a {exponent} é: {result}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 1.8) + 32

print(f"{celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit.")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

raio = float(input("Digite o raio do circulo: "))
area = math.pi * (raio ** 2)

print(f"A área do circulo de raio {raio} é: {area}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
user_string = input("Digite uma string: ")
upper_string = user_string.upper() 
print(f"A string {user_string} em maiúsculas é: {upper_string}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
user_name = input("Digite seu nome completo: ")
lower_name = user_name.lower()
print(f"Seu nome {user_name} em minúsculas é: {lower_name}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
user_phrase = input("Digite uma frase: ")
print(f"A frase sem espaços em branco no início e no final é: {user_phrase.strip()}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
date_input = input("Digite uma data no formato dd/mm/aaaa: ")
day, month, year = date_input.split('/')
print(f"Dia: {day}")
print(f"Mês: {month}")
print(f"Ano: {year}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string_1 = input("Digite a primeira string: ")
string_2 = input("Digite a segunda string: ")
concatenated_string = string_1 + string_2
print(f"A string concatenada é: {concatenated_string}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
bool_1 = input("Digite o primeiro valor booleano (True/False): ")
bool_2 = input("Digite o segundo valor booleano (True/False): ")
result = bool_1 and bool_2
print(f"O resultado da operação AND entre {bool_1} e {bool_2} é: {result}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
bool_1 = input("Digite o primeiro valor booleano (True/False): ")
bool_2 = input("Digite o segundo valor booleano (True/False): ")
result = bool_1 or bool_2
print(f"O resultado da operação OR entre {bool_1} e {bool_2} é: {result}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
bool_value = input("Digite um valor booleano (True/False): ")
inverted_bool = not bool_value
print(f"O valor invertido de {bool_value} é: {inverted_bool}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
number_1 = float(input("Digite o primeiro numero: "))
number_2 = float(input("Digite o segundo numero: "))
result = number_1 == number_2
print(f"Os números {number_1} e {number_2} são iguais? {result}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
number_1 = float(input("Digite o primeiro numero: "))
number_2 = float(input("Digite o segundo numero: "))
result = number_1 != number_2
print(f"Os números {number_1} e {number_2} são diferentes? {result}")


# #### try-except e if

# 21: Conversor de Temperatura


# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
