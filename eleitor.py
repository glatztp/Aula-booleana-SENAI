def verificar_elegibilidade_para_votar(idade):
    return idade >= 18

idade_usuario = int(input("Digite sua idade: "))

if verificar_elegibilidade_para_votar(idade_usuario):
    print("Você é elegível para votar!")
else:
    print("Você não é elegível para votar.")
