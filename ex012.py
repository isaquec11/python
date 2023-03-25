preco = float(input('Qual é o preço do produto? R$'))
desconto = preco*5/100
print('O produto que custava R${:.2f}, na promoção de 5% de desconto, passou a custar R${:.2f}'.format(preco, preco - desconto))

