## Exercícios de Listas e Dicionários
# 1- Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
numeros: list[int] = list(range(1, 11))

for numero in numeros:
    print(numero ** 2)

# 2- Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

linguagens: list[str] = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")
print(linguagens)

# 3- Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livros = {
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano_publicacao": 1954
}

print(f"Título: {livros['titulo']}")
print(f"Autor: {livros['autor']}")
print(f"Ano de Publicação: {livros['ano_publicacao']}")
print(f"{livros}")


# 4- Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

texto: str = "Hellow World"
texto_formatado: str = texto.lower()

ocorrencias: dict[str, int] = {}

for caractere in texto_formatado:
    if caractere != " ":
        if caractere in ocorrencias:
            ocorrencias[caractere] += 1
        else:
            ocorrencias[caractere] = 1

print(ocorrencias)

# 5- Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

produtos: list[str] = ["maçã", "banana", "cereja", "laranja"]
precos: dict[str, float] = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
preco_total: float = 0.0

for produto in produtos:
    if produto in precos:
        preco_total += precos[produto]
    else:
        print(f"Atenção: O produto '{produto}' não foi encontrado no dicionário de preços.")

print(f"O preço total da lista de compras é: R${preco_total:.2f}")