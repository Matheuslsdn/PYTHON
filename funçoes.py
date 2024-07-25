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

def quadrado_string(tamanho):
    x = 0
    while x < tamanho:
        y = 0
        while y < tamanho:
            if (x + y) % 4 == 0:
                print("C", end=" ")
            elif (x + y) % 4 == 1:
                print("A", end=" ")
            elif (x + y) % 4 == 2:
                print("Z", end=" ")
            else:
                print("S", end=" ")
            y += 1
        print()
        x += 1
quadrado_string(10)                