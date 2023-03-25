lag = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}².'.format(lag, alt, lag*alt))
tinta = lag*alt/2
print('Para pintar esta parede, você precisará de {}l de tinta.'.format(tinta))
