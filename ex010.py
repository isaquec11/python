possuido = float(input('Digite o valor possuído em sua Carteira: R$'))
dolar = possuido / 5.16
print('Com R${:.2f} você pode comprar US${:.2f}'.format(possuido, dolar))
