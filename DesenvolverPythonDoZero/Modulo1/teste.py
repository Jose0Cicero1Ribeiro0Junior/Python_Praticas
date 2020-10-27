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
