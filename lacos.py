for i in range(1, 11, 1):
    print(i)


for i in range(0, 21, 2):
    print(i)


for i in range(20, 0, -1): 
    print(i)

print('Decolar');

soma = 0
for  i in range(1, 101, 1):
    soma += i;

print('A soma dos números de 1 a 100 é: {}'.format(soma));



#Tabuada 

num = int(input('Digite um número para ver a tabuada: '));
for i in range(1, 11, 1):
    print('{} x {} = {}'.format(num, i, num * i));


n = 1 

while n <= 10 :
    print(n)
    n += 1



senha = 'python123'

senha_usuario = input('Digite a senha: ')
while senha_usuario != senha:
    print('Senha incorreta. Tente novamente.')
    senha_usuario = input('Digite a senha: ')
print(f'Senha correta! Acesso permitido.')

