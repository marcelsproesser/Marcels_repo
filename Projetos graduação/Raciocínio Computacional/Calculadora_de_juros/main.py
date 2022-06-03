nome_produto = input("qual o nome do produto? ")
quantidade_produto = input("qual a quantidade disponível desse produto? ")
valor_produto = input("qual o preço de cada unidade? ")
preco_final = int(valor_produto) * int(quantidade_produto)
preco_a_vista = int(preco_final) * 0.75

forma_de_pagamento = input("Qual a forma de pagamento? a vista digite 1, parcelado digite 2: ")

if forma_de_pagamento == "1":
    print("O preço final do/a " + nome_produto + " é" + str(preco_a_vista) + " reais")

elif forma_de_pagamento == "2":
    quantidade_parcelas = input("Em quantas parcelas você deseja pagar? ")
    preco_parcelas_sem_juros = int(preco_final) / int(quantidade_parcelas)
    porcentagem_juros_parcela = (int(quantidade_parcelas) / 100)
    preco_parcelas = preco_parcelas_sem_juros * (1 + porcentagem_juros_parcela)
    print("O preço final do/a " + nome_produto + " é " + str(preco_final) + " reais, dividido em " + quantidade_parcelas + " parcelas de " + str(preco_parcelas) + " reais")

else:
    raise ValueError("Escolha um método de pagamento válido")
