"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""

"""
#### Exercício 1

Receba um número inteiro de um usuário. Se ele for para, imprima "Par". Se não, imprima ímpar.

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!!
"""

number = int(input("Digite um número: "))

is_even = (number % 2) == 0

if is_even:
    print("Par")
else:
    print("Ímpar")
  
