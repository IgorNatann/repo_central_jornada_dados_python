### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = 10
preco = 25.5   

try:
    if quantidade > 0 and preco > 0:
        print("Dados validos")
    else:
        print("Dados inválidos")
except ValueError as e:
    print(e)
    
### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperatura = 22.5

if temperatura < 18:
    print("Baixa")
elif temperatura >= 18 and temperatura <= 25:
    print("Normal")
else:
    print("Alta")


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])
else:
    print("Log não é de erro")

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# Coleta os dados
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

# Valida idade
if 18 <= idade <= 65:
    # Idade válida, agora valida email
    if "@" in email and "." in email:
        print("Dados de usuário válidos")
    else:
        print("Erro: Email inválido")
else:
    print("Erro: Idade deve estar entre 18 e 65 anos")


### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# Entrada de dados
transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita")
else:
    print("Transação não é suspeita")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "exemplo de texto exemplo de contagem de palavras"

# Separando o texto em palavras
palavras = texto.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# Lista original
numeros = [10, 20, 30, 40, 50]

# Encontra o menor e maior valor
min_val = min(numeros)
max_val = max(numeros)

# Cria lista vazia para guardar os normalizados
numeros_normalizados = []

# Percorre cada número e normaliza
for num in numeros:
    num_normalizado = (num - min_val) / (max_val - min_val)
    numeros_normalizados.append(num_normalizado)

# Mostra o resultado
print("Original:", numeros)
print("Normalizado:", numeros_normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {'nome': 'Ana', 'idade': 25, 'email': 'ana@email.com'},
    {'nome': 'Bruno', 'idade': 30},  # falta o 'email'
    {'nome': 'Carla', 'email': 'carla@email.com'},  # falta a 'idade'
    {'nome': 'Diego', 'idade': 28, 'email': 'diego@email.com'}
]
# cria lista vazia
usuarios_completos = []  
usuarios_incompletos = []

 # percorre cada usuário
for usuario in usuarios: 
    if 'nome' in usuario and 'idade' in usuario and 'email' in usuario:
        usuarios_completos.append(usuario)  # adiciona se estiver completo
    else:
        usuarios_incompletos.append(usuario)  # adiciona se estiver incompleto
print(f"Usuários completos: {usuarios_completos}")
print(f"Usuários incompletos: {usuarios_incompletos}")

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.