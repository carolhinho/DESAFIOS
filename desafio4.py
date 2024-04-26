'''
Criar uma calculadora de IMC

Qual é a sua altura em cm:
Qual é o seu peso em kg:

'''

# MENOR QUE 18,5         MAGREZA
# ENTRE 18,5 E 24,9      NORMAL
# ENTRE 25,0 E 29,9      SOBREPESO
# ENTRE 30,0 E 39,9      OBESIDADE
# MAIOR QUE 40,0         OBESIDADE GRAVE




altura = int(input('Qual a sua altura em cm?: '))
peso = int(input('Qual é o seu peso em kg?: '))

calculo_imc = peso / ((altura/100)**2)

if calculo_imc < 18.5:
    print('Magreza')

elif calculo_imc < 24.9:
    print('Normal')

elif calculo_imc < 29.9:
    print('Sobrepeso')

elif calculo_imc < 39.9:
    print('Obesidade')

elif calculo_imc > 40.0:
    print('Obesidade grave')