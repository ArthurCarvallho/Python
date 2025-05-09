nome = []

for i in range(4):
    nome.append(input(f'Digite o {i + 1}° nome: '))

for i in range(3,-1,-1):
    print(f'O {i + 1}° nome é: {nome[i]}')

# soma de vetores

numeros = [2, 4, 6, 8, 10]
resultado = 0
for i in range(len(numeros)):
    resultado += numeros[i]
print(f'A soma dos números é: {resultado}')


#inevertendo lista

letra = ['a', 'b', 'c', 'd', 'e']
letra.reverse()
print(letra)