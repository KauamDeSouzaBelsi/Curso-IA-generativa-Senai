# while True:
#     try:
#         nome_cliente = input("coloque o seu nome : ")
#         break
#     except ValueError:
#         print("valor errado! confira se a sua idade esta certa")


# while True: 
#     try:
#         idade_cliente = int(input("coloque a sua idade: "))
#         break
#     except ValueError:
#         print("valor errado! confira se a sua idade esta certa")



# email_cliente = input("coloque o seu email: ")
# # print(nome_cliente)
# # print(idade_cliente)
# # print(email_cliente)

# print(f"o seu nome é {nome_cliente}.\n sua idade é {idade_cliente}.\n seu nome é {email_cliente}")

# idade_futura = 1 + idade_cliente
# print(idade_futura)

# dados do cliente
valor_pizza = float(input("coloque o valor da pizza para que o desconto seja aplicado: "))
valor_desconto = float(input("Digite o valor do desconto: "))
# contas
percentual = valor_desconto/100
desconto = valor_pizza * percentual
valor_final = valor_pizza - desconto
print(f"o valor final é:{valor_final}")