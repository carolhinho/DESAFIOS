
'''

criar um programa que dependendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em portugues. O usuario deverá fornecer a temperatura.

Temperaturas - Cozimento

120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (ao ponto par ao mal)
140°F ou 60°C - Medium (ao ponto)
150°F ou 65°C - Medium well (ao ponto para o bem)
160°F ou 71°C - Well done (bem passada)

'''

temperaturas = int(input('Qual é a temperatura da carne?: '))

if temperaturas < 48:
    print('Cozinhar por mais algum tempo')

elif temperaturas in range(48, 53):
    print('Selada')

elif temperaturas in range(54, 59):
    print('Ao ponto para o mal')

elif temperaturas in range(60, 64):
    print('Ao ponto')

elif temperaturas in range(65, 70):
    print('Ao ponto para o bem')

elif temperaturas >= 71:
    print('bem passada')


