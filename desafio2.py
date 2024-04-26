'''

Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. 
O usuario deverá fornecer as seguintes informações: 
- Rendimento
- Altura
- Largura
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'


'''

def qnt():
    
    qnt = total_latas

rendimento = int(input('Qual o rendimento?: '))
altura = int(input('Qual a altura da parede?: '))
largura = int(input('Qual a largura da parede?: '))

total_latas = altura * largura / rendimento

print(f'Você precisa de {total_latas} latas de tinta')



