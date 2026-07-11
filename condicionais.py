# menor ou maior de idade

# idade = int(input("coloque a sua idade: "))
# if idade >= 18:
#     print("maior de idade")
# else:
#     print("menor de idade")

# temperatura do carro

# temaperatura = 100
# if temaperatura >=60:
#     print("O motor do carro ferveu")
# else:
#     print("temperatura agradavel")

# acesso com senhas

# senha = (float(input("Digite sua senha: ")))
# if senha == 1234:
#     print("acesso liberado")
# else:
#     print("acesso negado")

# média escolar

# nota_aluno = float(input("Digote a sua nota: "))
# if nota_aluno >=5:
#     print("aprovado")
# else:
#     print("reprovado")

# primeira nota
while True:
    try:
        nota1 = float(int(input("Coloque sua primeira nota: ")))
        break
    except ValueError:
        print("dados incorretos! verifique oque vc colocou")

# Segunda nota
while True:
    try:
        nota2 = float(int(input("Coloque sua segunda nota: ")))
        break
    except ValueError:
        print("dados incorretos! verifique oque vc colocou")

# terceira nota
while True:
    try:
        nota3 = float(int(input("Coloque sua terceira nota: ")))
        break
    except ValueError:
        print("dados incorretos! verifique oque vc colocou")

# Media das notas
soma = nota1 + nota2 + nota3 
media = soma /3
if media >=6:
    print("aprovado🏆")

elif media >=4 and media <5:
    print("recuperação📝")

else:
    print("reprovado❌")