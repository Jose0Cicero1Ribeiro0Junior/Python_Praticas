#1) Escreva um programa em Python para contar de 1 até 10. 

#a) usando a instrução while 

cont = 1
while cont <= 10:
    print(cont, end=' ')
    cont +=1

print()    

#b) usando a instrução for e a função range 

for cont in range(10):
    print(cont + 1, end=' ')
print()

#2) Escreva um programa para contar quantos números pares e ímpares existentes entre 1 e 10 bem como a soma deles. 

#a) usando a instrução while 

# PAR

soma_par = cont_par = 0
cont = 1
while cont <= 10:
    if cont == 1:
        print(f'O total da soma de Par: ', end='')
    if cont % 2 == 0:
        print(cont, end='')
        soma_par += cont
        cont_par += 1 
        if cont <= 9:
            print(end=' + ')
        else:
            print(end=' = ')
            print(soma_par)
    cont += 1
print(f'Com um total de {cont_par} números Par')

# IMPARES

cont = 1
cont_impares = soma_impar = 0 
while cont <= 10:
    if cont == 1:
        print(f'O total da soma de Impares: ', end='')
    if cont % 2 == 1:
        print(cont, end='')
        soma_impar += cont
        cont_impares += 1 
        if cont <= 8:
            print(end=' + ')
        else:
            print(end=' = ')
            print(soma_impar)
    cont += 1
print(f'Com um total de {cont_impares} números Impares')



#b) usando a instrução for e as funções range e sum 

impar, par = list(), list()
for cont in range(1,11):
    if cont % 2 == 0:
        par.append(cont)
    else:
        impar.append(cont)
print(f'O total de Ímpares é de {len(impar)} e a soma total  =', end=' ')
cont = 0 
for cont in range(0,len(impar)):
    print(f'{impar[cont]}', end='')
    if cont <= len(impar)-2:
        print(end=' + ')
    else:
        print(end=' = ')
        print(sum(impar))
    cont += 1
print()

print(f'O total de Pares é de {len(par)} e a soma total =', end=' ')
cont = 0
for cont in range(0,len(par)):
    print(f'{par[cont]}', end='')
    if cont <= len(par)-2:
        print(end=' + ')
    else:
        print(end=' = ')
        print(sum(par))
    cont += 1
print()



#3) Escreva um programa para resolver equações do segundo grau representadas por: ax² + bx + c = 0
#https://mundoeducacao.uol.com.br/matematica/tres-passos-para-resolver-uma-equacao-segundo-grau.htm

#a) sem usar o módulo math 
#Primeiro passo: Escreva os valores numéricos dos coeficientes a, b e c.
a = int(input('Valor de "a": '))
b = int(input('Valor de "b": '))
c = int(input('Valor de "c": '))

#Segundo passo: Calcule o valor de delta. Δ = b2 – 4ac
delta = b*b -4*a*c

#Terceiro passo: calcule os valores de x da equação. x = – b ± √Δ / 2·a
x1 = (-b - (delta ** 0.5)) / (2*a)
x2 = (-b + (delta ** 0.5)) / (2*a)

print(f'O valor de x1: {x1:.2f}\nO valor de x2: {x2:.2f}')
#b) usando o módulo math 
from math import sqrt

a = int(input('Valor de "a": '))
b = int(input('Valor de "b": '))
c = int(input('Valor de "c": '))

delta = b*b -4*a*c
x1 = (-b - (sqrt(delta))) / (2*a)
x2 = (-b + (sqrt(delta))) / (2*a)

print(f'O valor de x1: {x1:.2f}\nO valor de x2: {x2:.2f}')



#4) Reescreva o programa acima criando uma função bhaskara que recebe como parâmetros os coeficientes a, b e c e retorna as raízes da equação. 
#https://brasilescola.uol.com.br/matematica/formula-bhaskara.htm x = – b ± √b2 – 4ac / 2·a

def formula_de_2grau(a,b,c):
    from math import sqrt
    x1 = (-b - (sqrt(b*b -4*a*c))) / (2*a)
    x2 = (-b + (sqrt(b*b -4*a*c))) / (2*a)

    print(f'O valor de x1: {x1:.2f}\nO valor de x2: {x2:.2f}')  
let = 'a', 'b', 'c' 
n = list()
for cont in range(3):
    n.append(int(input(f'Digite o valor de {let[cont]}: ')))
formula_de_2grau(n[0],n[1],n[2])

#5) Considerando a string s = 'Mentorama' escreva um programa que: 

#a) converta a string para maiúsculo, em seguida 
s = 'Mentorama'
s = s.upper()
print(s)
#b) imprima-a de trás para frente 
for x in range(1,len(s)+1):
    print(s[-x], end='')
print()
#c) imprima somente as vogais 
for x in range(len(s)):
    if s[x] in 'AEIOU':
        print(s[x],end=' ')
print()
