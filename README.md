# Jornada de Dados - Python (Guia de Estudos)

Este README resume os conceitos-chave demonstrados nos arquivos de cada pasta do repositorio.

## Mapa rapido das pastas

- `aula_01_Python_do_Zero/`: primeiros scripts, entrada de dados e operacoes basicas.
- `aula_02_TypeError_TypeCheck/`: validacao, conversao de tipos e tratamento de erros.
- `aula_03_controle_Fluxo_DEBUG_IF_FOR_While_Listas_Dicionarios/`: controle de fluxo, listas e dicionarios aplicados a cenarios de dados.
- `aula_04_Tipos_complexos_TypeHint(Dict-DFs-Tables)/`: type hints, listas e dicionarios tipados.
- `cola_de_bolso/`: resumo pratico dos principais padroes usados.

## Conceitos-chave por pasta

### 1) `aula_01_Python_do_Zero`

Arquivos: `exemplo_001.py`, `desafio.py`, `desafio_2.py`, `desafio_3.py`, `desafio_4.py`, `desafio_5.py`, `main.py`.

Conceitos praticados:
- Primeira execucao com `print()`.
- Entrada de dados com `input()`.
- Conversao de tipo com `int()`, `float()` e `str()`.
- Operacoes aritmeticas simples (principalmente soma).
- Tamanho de string com `len()`.
- Formatacao de saida com `f-string`.
- Uso de variaveis e constante (`constante_valor_bonus`).

### 2) `aula_02_TypeError_TypeCheck`

Arquivos: `desafio.py`, `exercicios.py`.

Conceitos praticados:
- Validacao de nome (vazio, contem numero) com `len()`, `any()` e `isdigit()`.
- Validacao de entradas numericas com `try/except ValueError`.
- Tratamento de divisao por zero com `ZeroDivisionError`.
- Fluxo condicional com `if/elif/else`.
- Verificacao de tipo com `isinstance()`.
- String processing para palindromo (`replace`, `lower`, slicing `[::-1]`).
- Conversao de lista de strings para inteiros com `split()`, `strip()` e `int()`.
- Classificacao de numeros (positivo/negativo/zero e par/impar).

### 3) `aula_03_controle_Fluxo_DEBUG_IF_FOR_While_Listas_Dicionarios`

Arquivo: `exercicios.py`.

Conceitos praticados:
- Regras de negocio com operadores logicos (`and`, `or`) para validacao de dados.
- Classificacao por faixa de valores (`if/elif/else`).
- Leitura de dados em dicionarios e filtros por condicao (`log['level'] == 'ERROR'`).
- Validacao de campos obrigatorios em registros.
- Contagem de palavras com acumulador em dicionario.
- Normalizacao de dados em escala 0-1 com `min()` e `max()`.
- Filtragem de registros completos vs incompletos.
- Extracao de subconjuntos (numeros pares).
- Agregacao por categoria em dicionario (somatorio incremental).
- Lacos `while` com sentinela (`while True` + `break`).
- Simulacao de paginacao de API com funcao + loop.
- Simulacao de tentativas de conexao com limite de repeticoes.
- Condicao de parada em processamento (`STOP`).

### 4) `aula_04_Tipos_complexos_TypeHint(Dict-DFs-Tables)`

Arquivos: `type_hint.py`, `exercicio_type_hint.py`, `exercicios_list_dict.py`.

Conceitos praticados:
- Introducao a type hints em Python.
- Anotacao de variaveis com tipos primitivos (`int`, `str`, `float`, `bool`).
- Uso de colecoes tipadas (`list[int]`, `list[str]`, `dict[str, int]`, `dict[str, float]`).
- Validacao de input com loop de repeticao ate dado valido.
- Operacoes de lista (`remove`, `append`).
- Manipulacao de dicionario para contagem e lookup de precos.
- Soma condicional de valores e mensagem para chave ausente.

### 5) `cola_de_bolso`

Arquivo: `COLA_DE_BOLSO_PYTHON.md`.

Conceitos praticados:
- Resumo de sintaxe e padroes mais usados no projeto.
- Mini templates para validacao, agregacao e normalizacao.
- Checklist de revisao antes de executar scripts.

## Roteiro de revisao sugerido

1. Comece por `aula_01_Python_do_Zero/` para reforcar base de entrada/saida e tipos.
2. Passe para `aula_02_TypeError_TypeCheck/` e foque em validacao robusta com `try/except`.
3. Avance para `aula_03_controle_Fluxo_DEBUG_IF_FOR_While_Listas_Dicionarios/` para dominar logica aplicada em dados.
4. Feche com `aula_04_Tipos_complexos_TypeHint(Dict-DFs-Tables)/` para ganhar clareza com type hints e colecoes tipadas.
5. Use `cola_de_bolso/COLA_DE_BOLSO_PYTHON.md` como revisao rapida antes de praticar.

## Como executar os scripts

```bash
python aula_01_Python_do_Zero/exemplo_001.py
python aula_02_TypeError_TypeCheck/exercicios.py
python aula_03_controle_Fluxo_DEBUG_IF_FOR_While_Listas_Dicionarios/exercicios.py
python aula_04_Tipos_complexos_TypeHint(Dict-DFs-Tables)/exercicios_list_dict.py
```
