# Exemplos simples de uso de decorators.
# Cada bloco abaixo mostra um tipo de transformacao aplicada a uma funcao.

from decorator import my_decorator, split_string, uppercase_decorator


# Exemplo 1:
# `my_decorator` executa codigo antes e depois da funcao original.
@my_decorator
def my_function():
    print("Dentro da funcao")


my_function()

# Resultado esperado:
# Antes de executar a função
# Dentro da funcao
# Depois de executar a função


# Exemplo 2:
# `uppercase_decorator` transforma o texto retornado em letras maiusculas.
@uppercase_decorator
def text():
    return "Hello WOrld"


print(text())

# Resultado esperado:
# HELLO WORLD


# Exemplo 3:
# Os decorators sao aplicados de baixo para cima:
# 1. `uppercase_decorator` deixa o texto em maiusculas.
# 2. `split_string` divide a string em uma lista de palavras.
@split_string
@uppercase_decorator
def example():
    return "Aprendendo Decorators"


print(example())

# Resultado esperado:
# ['APRENDENDO', 'DECORATORS']
