#Registro de uma meta finaceira de ganhos ao ano 
# 1 - Armazenar
# 2 - Cacular porsentagem para alcansar a meta
# 3 - Fazer provições para alcançar a meta
text = open('teste.txt', 'w')
n1 = str(input('Quanto você espara ganhar este ano ? R$'))
n2 = str(input('Quanto ganhou no ano passado? R$'))
n3 = str(input('Quanto gostaria de ganhar no ano que vem? R$'))
print(n1, n2, n3)
text.write(n1)