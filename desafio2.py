'''

Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. 
O usuario deverá fornecer as seguintes informações: 
- Rendimento
- Altura
- Largura
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'


'''

rendimento = int(input('Qual o rendimento?: '))
altura = int(input('Qual a altura da parede?: '))
largura = int(input('Qual a largura da parede?: '))

def calculo_tinta():
  
    total_latas = largura * altura / rendimento

    print (f'Voce precisa de {total_latas} de tinta')

calculo_tinta()



