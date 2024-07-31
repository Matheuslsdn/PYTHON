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

# def media():
#     lista = [14, 85, 2, 29, 45, 12]
#     return sum(lista) / len(lista)

# print("A média é", media())

#Ativ 02

# def alcance(lista):
#     return max(lista) - min(lista)

# lista = [3, 1, 4, 2, 5]
# print(alcance(lista)) 

#-----------------------------------------------

# minha_lista = [3, 4, 5, 9, 1]

# for item in minha_lista:
#     print(item)  

# def tolascado():
#     entrada = input("Digite uma string: ")
#     for caractere in entrada:
#         print(f"{caractere}")
       

# tolascado()

# for i in range(5): # com um argumento repetir um certo argumento 
#     print(i) 

# for i in range(3, 7): # com dois argumentos a função retornará um intervalo entre os dois números. a função range fornece um intervalo começando em A e terminando em B -1
#     print(i)

# for i in range(1, 9, 2): # com três argumentos a funçaõ vai de a para b -1 e finaliza em c a cada passo  
#     print(i)

# for i in range(6, 2, -1): # com argumento negativo a função conta do frente pra trás
#     print(i)

# def inteiro():
#     n = int(input("Digite um número inteiro positivo: "))
#     if n <= 0:
#         print("Erro: o número deve ser positivo.")
#     else:
#         for i in range(-n, n + 1):
#             if i != 0:
#                 print(i)

# inteiro()

#-----------------------------------------------

#Ativ 04

# def lista_estrelas(numeros):
#     for numero in numeros:
#         print("#" * numero)

# numeros = [3, 7, 1, 1, 2]
# lista_estrelas(numeros)

#Ativ 05

# def anagramas(palavra1, palavra2):
#     return sorted(palavra1.lower()) == sorted(palavra2.lower())

# print(anagramas("cagada", "dimensional"))
# print(anagramas("meteoro ", "de pegasu"))
# print(anagramas("kamehame", "haaaaaaa"))
# print(anagramas("casa", "acas"))

#Ativ 06

# def soma_positiva(lista):
#     soma = 0
#     for x in lista:
#         if x > 0:
#             soma += x
#     return soma

# lista = [1, -2, 3, -4, 5]
# print(soma_positiva(lista))

#Ativ 07

# def numeros_pares(lista):
#     pares = []
#     for x in lista:
#         if x % 2 == 0:
#             pares.append(x)
#     return pares

# lista = [9, 20, 66, 13, 5, 63]
# print(numeros_pares(lista))

#Ativ 08

# def lista_soma(lista1, lista2):
#     resultado = []
#     for x, y in zip(lista1, lista2):
#         resultado.append(x + y)
#     return resultado

# lista1 = [20, 10, 23, 17, 25]
# lista2 = [61, 47, 38, 19, 17]
# print(lista_soma(lista1, lista2))  

# def mais_caracteres(string):
#     contador = {}
#     for carater in string:
#         contador[carater] = contador.get(carater, 0) + 1
#     max_count = max(contador.values())
#     for carater, count in contador.items():
#         if count == max_count:
#             return carater
        
# string = "eu desisto, que dogras"                         
# print(mais_caracteres(string))

# Ativ 09

# def sem_vogal(testo):
#     vogais = 'aeiouãõ'
#     resultado = ''
#     for caractere in testo:
#         if caractere not in vogais:
#             resultado += caractere
#     return resultado

# print(sem_vogal("Se meu pau não parar de crescer..."))

# pessoas = [[12, 15, 17], [10, 14], [7, 14, 21]]

# print(pessoas)
# print(print[1])
# print(pessoas[1][1])

# pessoas = [["manga", 12, 15, 17], ["pera", 10, 14], ["mamão", 7, 14, 21]]

# for pessoa in pessoas:
#     nome = pessoas[0]
#     idade = pessoas[1]
#     altura = pessoas[2]
#     print(nome, idade, altura)

# minha_matriz = [[1, 2, 3], [3, 2, 1],[4, 5, 6]]
# print(minha_matriz[0][1]) 
# print(minha_matriz[1][0])
# minha_matriz[1][0] = 10
# print(minha_matriz[1][0])

# conta_elementos_match()

# def conta_elementos_match(minha_matriz: list[list[int]], elemento: int) -> int:
#   contador = 0
#   for linha in minha_matriz:
#     for numero in linha:
#       if numero == elemento:
#         contador += 1
#   return contador
# minha_matriz = [[1, 2, 3], [2, 4, 2], [5, 2, 1]]
# valor_procurado = 2
# resultado = conta_elementos_match(minha_matriz, valor_procurado)
# print(f"O valor {valor_procurado} aparece {resultado} vezes na matriz.")



# def imprime_tabuleiro(sudoku):
#     for a in range(len(sudoku)):
#         for b in range(len(sudoku[0])):
#             valor = sudoku[a][b]
#             if valor == 0:
#                 valor = '-'
#             if b == 8:
#                 print(valor)
#             else:
#                 print(valor, end="")
#         if a != len(sudoku) - 1:
#             print()

# sudoku = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [0, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [0, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# imprime_tabuleiro(sudoku)

# def imprime_tabuleiro(sudoku):
#     for item in sudoku:
#         for itens in item:
#             if itens == 0:
#                 print((" "), end="")
#             else:
#                 print(itens, end="")
#         print("")

# sudoku = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [0, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [0, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# imprime_tabuleiro(sudoku)

# meu_dicionario = {}
# meu_dicionario["apina"] = "macaco"
# meu_dicionario["doguinho"] = "cachorro"
# meu_dicionario["bichano"] = "gato"
# print(meu_dicionario)
# print(meu_dicionario["apina"])
# palavra = input("Por favor, digite uma palavra: ")
# if palavra in meu_dicionario:
#     print("tradução", meu_dicionario[palavra])
# else:
#     print("palavra não encontrada")
          
# resultado = {}
# resultado["Mary"] = 4
# resultado["John"] = 5
# resultado["Jane"] = 3

# lista = {}
# lista[5] = [1, 2, 3]
# lista[42] = [5, 4, 5, 4, 4]
# lista[100] = [5, 2, 3]

# meu_dicionario = {}
# meu_dicionario["apina"] = "macaco"
# meu_dicionario["doguinho"] = "cachorro"
# meu_dicionario["bichano"] = "gato"

# for chave in meu_dicionario:
#     print("chave",chave)
#     print("valor",meu_dicionario[chave])

# lista_palavras = [
#   "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
#   "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
#   "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
#   ]

# def contagens(minha_lista):
#     palavras = {}
#     for palavra in minha_lista:
#         if palavra not in palavras:
#             palavras[palavra] = 0
#         palavras[palavra] += 1
#         return palavras

# print(contagens(lista_palavras))

# def histogram(teste):
#     lista = {}
#     for letra in teste:
#         if letra in lista:
#             lista[letra] += 1
#         else:
#             lista[letra] = 1

#     for letra in sorted(lista.keys()):
#         print(f"{letra}: {'*' * lista[letra]}")

# histogram("Sharizard, pikachu, corrida maluca")


def app():
    comando = int(input("digite o comando: "))
    while comando:
        if comando == 1:
            pesquisa()
        elif comando == 2:
            adicionar()
        elif comando == 3:
            break
        else:
            print("comando invalido, Tente novamente")
            break
    
def pesquisa():
    lista_de_contato = {}
    palavra = input("digite a palavra: ")
    if palavra in lista_de_contato:
        print(f"o contato {palavra} foi encontrado")
    else:
        print(f"o contato {palavra} não foi encontrado")        
        add = str(print("Deseja adicionar? S/N "))
        if add == "S" and add == "s":
            adicionar()
        else:
            return lista_de_contato
app()




