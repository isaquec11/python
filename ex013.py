salario = float(input('Qual é o salário do funcionário? R$'))
vreajuste = int(input('Digite o valor para aumento: %'))
novo = salario +(salario/100*vreajuste)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}.'.format(salario, vreajuste, novo))

