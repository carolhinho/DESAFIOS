'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

lista1 = funcionarios que tem carro e trabalham a noite
lista2 = funcionarios que tem carro e trabalham durante o dia
lista3 = funcionarios que não tem carro


'''


funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']


func_set = set(funcionarios)
dia = set(turno_dia)
noite = set(turno_noite)
carro = set(tem_carro)


print(carro & noite)
print(carro & dia)
print(func_set - carro)

