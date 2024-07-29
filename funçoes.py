#Ativ 01

# def media():
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite um número: "))
#     num3 = int(input("Digite um número: "))
#     media = (num1 + num2 + num3) / 3
#     print("A média dos números é: ", media)

# media()

#Ativ 02

# def printa_varias_vezes(texto, vezes):
#     for i in range(vezes):
#         print(texto)
# texto = input("Digite um texto: ")
# vezes = int(input("Digite quantas vezes deseja imprimir: "))
        
# printa_varias_vezes(texto, vezes);

#Ativ 03

# def quadrado_hashtag(tamanho):
#     for i in range(tamanho):
#         print("#" * tamanho)
# tamanho = int(input("Digite o tamanho do quadrado: "))
# quadrado_hashtag(tamanho)

#Ativ 04

# def mesa_xadrez():
#     for x in range(8):
#         for y in range(8):
#             if (x + y) % 2 == 0:
#                 print("1", end="")
#             else:
#                 print("0", end="")
#         print()
# mesa_xadrez()
# def mesa_xadrez(tamanho):
#     x = 0
#     while x < tamanho:
#         y = 0
#         while y < tamanho:
#             if (x + y) % 2 == 0:
#                 print("1", end=" ")
#             else:
#                 print("0", end=" ")
#             y += 1
#         print()
#         x += 1
# mesa_xadrez(40)

#Ativ 05

# def quadrado_string(tamanho):
#     x = 0
#     while x < tamanho:
#         y = 0
#         while y < tamanho:
#             if (x + y) % 2 == 0:
#                 print(".", end=" ")
#             else:
#                 print("1", end=" ")
#             y += 1
#         print()
#         x += 1
# quadrado_string(10)  

# def cumprimentar(nome):
#     print("Olá, ",nome)

# def cumprimentar_infinitamente(nome, vezes):
#     while vezes > 0:
#         cumprimentar(nome)
#         vezes -= 1

# cumprimentar_infinitamente("Emily", 3)


#Ativ 06

#Ativ 07

# def caixa_de_hashtag(tamanho):
#     x = 0
#     while x < tamanho:
#         y = 0
#         while y < tamanho:
#             if (x + y) % 2 == 0:
#                 print("#", end=" ")
#             else:
#                 print("#", end=" ")
#             y += 1
#         print()
#         x += 1

# def retangulo(tamanho, vezes):
#     while vezes > 0:
#         caixa_de_hashtag(tamanho)
#         vezes -= 1

# retangulo(3 ,2)

#Ativ 08

# def triangulo():
#     x = 0
#     while x <= 8:
#         y = 0
#         while y < x:
#             print("#", end=" ")
#             y += 1
#         print()
#         x += 1
# triangulo() 

# def minha_soma(a, b):
#     return a + b

# resultado = minha_soma(4,6)
# print("A soma é",resultado)  

#Ativ 09

# def o_maior_numero(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# resultado = o_maior_numero(5, 3, 7)
# print("O maior número é:", resultado) 

#Ativ 10

# def mesmo_caracter(stri, inti, inte):
#     if stri != inti & inti== inte:
#         return True
#     else:
#         return False

# resultado = (mesmo_caracter("nada", 5, 5))  
# print(resultado)

#Ativ 11

# lista = [1, 2, 3, 4, 5]

# lista[2] = input("Escreva um numero menor que 5 para parar a sequência ")
# while lista[2] == -1:
#     if lista[2] > -1:
#         print(input("Escreva um numero menor que 5 para parar a sequência "))

#Ativ 12

# lista = []
# lista.append(5)
# lista.append(7)
# lista.append(1)
# print(lista) 

# num_itens = int(input("Digite o número de itens a serem adicionados: "))

# lista = []

# for i in range(num_itens):
#     valor = input(f"Digite o valor {i+1}: ")
#     lista.append(valor)

# print("Lista:", lista)

# lista = []

# while True:
#     escolha = input("Deseja adicionar (A) ou remover (R) um item? ")
#     if escolha.upper() == "A":
#         if not lista:
#             lista.append(1)
#         else:  
#             lista.append(lista[-1] + 1)
#         print("Lista:", lista)
#     elif escolha.upper() == "R":
#         if lista:
#             lista.pop()
#             print("Lista:", lista)
#         else:
#             print("Lista vazia! Não há itens para remover.")
#     else:
#         print("Escolha inválida. Por favor, digite A para adicionar ou R para remover.")
#     break

# def main():
#     lista = []

#     while True:
#         print(f"Lista atual: {lista}")
#         escolha = input("Digite 'add' para adicionar um item ou 'remove' para remover um item: ").strip().lower()
        
#         if escolha == 'add':
#             if lista:
#                 novo_item = lista[-1] + 1
#             else:
#                 novo_item = 1
#             lista.append(novo_item)
#             print(f"Item {novo_item} adicionado à lista.")
        
#         elif escolha == 'remove':
#             if lista:
#                 removido_item = lista.pop()
#                 print(f"Item {removido_item} removido da lista.")
#             else:
#                 print("A lista está vazia. Não há itens para remover.")
        
#         else:
#             print("Escolha inválida. Por favor, digite 'add' ou 'remove'.")
        
#         continuar = input("Deseja continuar? (s/n): ").strip().lower()
#         if continuar != 's':
#             break

#     print("Programa encerrado.")

# if __name__ == "__main__":
#     main()

# recebe uma lista como parametro
# show_tamanhos = [45, 44, 36, 39, 40]
# def mediana(minha_lista: list):
#     ordenada = sorted(minha_lista)
#     centro_lista = len(ordenada) // 2 
#     return ordenada[centro_lista]

# print("A mediana é", mediana(show_tamanhos))

# idades = [1, 56, 34, 22, 5, 77, 5]
# print("A média das idades é", mediana(idades))

#retorna uma lista
# def entrada_numeros():
#     numeros = []
#     while True:
#         entrada_usuario = input("Por favor, digite um número inteiro, deixe em branco para sair: ")
#         if len(entrada_usuario) == 0:
#             break
#         numeros.append(int(entrada_usuario))
#     return numeros

# entrada_numeros()

# def tamanho():
#     lista = [5, 12, 19, 65, 32]
#     return len(lista)

# print(tamanho())

#Ativ 01

def media():
    lista = [14, 85, 2, 29, 45, 12]
    return sum(lista) / len(lista)

print("A média é", media())


# def alcance(lista):
#     return max(lista) - min(lista)

# lista = [3, 1, 4, 2, 5]
# print(alcance(lista)) 