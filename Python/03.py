# Peça ao usuário para digitar três valores inteiros e imprima a soma deles 
x = []
for c in range(0,3):
    x.append(int(input('Digite um valor inteiro: ')))

print(sum(x))