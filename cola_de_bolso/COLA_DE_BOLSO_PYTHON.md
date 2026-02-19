# Cola de Bolso - Jornada de Dados (Python)

## 1) Entrada, saida e tipos basicos
- `input()` sempre retorna `str`.
- Converta quando precisar de numero: `int()`, `float()`.
- Mostre dados com `print()` e `f-string`: `f"Valor: {x}"`.
- Tamanho de texto: `len(texto)`.

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"{nome} tem {idade} anos.")
```

## 2) Operacoes e strings
- Soma: `+`
- Subtracao: `-`
- Multiplicacao: `*`
- Divisao: `/`
- Remover espacos: `texto.replace(" ", "")`
- Minusculo: `texto.lower()`
- Inverter string: `texto[::-1]`

```python
entrada = input("Palavra: ")
formatado = entrada.replace(" ", "").lower()
print(formatado == formatado[::-1])  # palindromo?
```

## 3) If / Elif / Else e operadores logicos
- `and`: todas as condicoes precisam ser verdadeiras.
- `or`: pelo menos uma condicao precisa ser verdadeira.
- `not`: inverte a condicao.
- Comparacoes encadeadas: `18 <= idade <= 65`.

```python
if 18 <= idade <= 65 and "@" in email and "." in email:
    print("Dados validos")
else:
    print("Dados invalidos")
```

## 4) Tratamento de erros (try/except)
- Use `try/except` para entradas invalidas.
- Erros comuns: `ValueError`, `ZeroDivisionError`.
- Voce pode criar erro manual com `raise ValueError(...)`.

```python
try:
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))
    print(n1 / n2)
except ValueError:
    print("Digite numeros validos.")
except ZeroDivisionError:
    print("Nao pode dividir por zero.")
```

## 5) Listas: padroes que voce usou
- Separar texto em lista: `split(",")`
- Adicionar item: `append()`
- Adicionar varios: `extend()`
- Filtrar com `for` + `if`

```python
entrada = input("Numeros (1,2,3): ")
itens = entrada.split(",")
numeros = []
for item in itens:
    numeros.append(int(item.strip()))
print(numeros)
```

## 6) Dicionarios: padroes que voce usou
- Acesso por chave: `d["chave"]`
- Checar chave: `"email" in usuario`
- Contagem/agregacao incremental:
  - se chave existe: soma
  - senao: inicia

```python
contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
```

## 7) For: repeticao com colecoes
- Percorre lista, string, dicionario etc.
- Bom para contagem, filtro e transformacao.

```python
pares = []
for n in [1, 2, 3, 4, 5, 6]:
    if n % 2 == 0:
        pares.append(n)
print(pares)
```

## 8) While: repeticao ate condicao
- Use quando nao sabe quantas iteracoes tera.
- `while True` + `break` para loop com sentinela.

```python
dados = []
while True:
    nome = input("Nome (ou sair): ")
    if nome == "sair":
        break
    dados.append(nome)
print(dados)
```

## 9) Funcoes simples
- Defina com `def`.
- Retorne com `return`.
- Usado por voce para simular paginas de API e conexao.

```python
def buscar_pagina(pagina, base):
    if pagina in base:
        return base[pagina]
    return None
```

## 10) Mini templates de prova/exercicio

### Validador de numero em faixa
```python
while True:
    try:
        n = int(input("Numero entre 1 e 10: "))
        if 1 <= n <= 10:
            break
        print("Fora da faixa.")
    except ValueError:
        print("Entrada invalida.")
```

### Soma por categoria (agregacao)
```python
totais = {}
for item in vendas:
    cat = item["categoria"]
    valor = item["valor"]
    totais[cat] = totais.get(cat, 0) + valor
```

### Normalizacao 0 a 1
```python
min_v = min(numeros)
max_v = max(numeros)
normalizados = [(n - min_v) / (max_v - min_v) for n in numeros]
```

## 11) Checklist rapido antes de rodar
- Converteu `input()` para tipo correto?
- Tratou erro de conversao com `try/except`?
- Evitou divisao por zero?
- Condicoes `if` cobrem todos os casos?
- Em `while`, existe condicao de parada?

## 12) Estado atual do repo
- Aulas 1 a 3 tem exercicios praticos cobrindo fundamentos.
- Pasta `aula_04_Tipos_complexos_TypeHint(Dict-DFs-Tables)` esta vazia (sem exemplos ainda).
