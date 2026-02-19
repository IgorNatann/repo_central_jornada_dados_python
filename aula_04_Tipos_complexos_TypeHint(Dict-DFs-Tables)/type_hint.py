# Type Hints em Python

# Type hints (ou dicas de tipo) são anotações opcionais no código Python que indicam os tipos esperados para variáveis, parâmetros de funções, valores de retorno e outros elementos. Elas foram introduzidas na PEP 484 (Python 3.5+) e não afetam a execução do código em tempo de execução — o Python continua sendo dinamicamente tipado. Seu propósito principal é melhorar a legibilidade, facilitar a manutenção e permitir verificações estáticas de tipo com ferramentas como `mypy`.

## Sintaxe Básica
# - Use `:` para parâmetros e variáveis.
# - Use `->` para retorno de funções.
# - Tipos vêm do módulo `typing` para casos avançados (ex: `List`, `Dict`, `Optional`).

## Exemplos de Type Hints
idade: int = 26
nome: str = "Igor"
altura: float = 1.72
is_student: bool = True