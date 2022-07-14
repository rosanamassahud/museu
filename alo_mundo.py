idade = 40
nome = 'Rosana'
print("meu nome é", nome, sep='-', end='!')
print("Tenho", idade, 'anos', sep='+')
print(type(idade))
print(type(nome))
idade = 'quarenta'
print(type(idade))
idade = 40.9
print(type(idade))
print(idade)
print(int(idade))

if (idade >= 18):
    print('eleitor obrigatorio')
    x = 2
    print(x)
elif ((idade < 18 and idade >= 16) or idade >=70):
    print('eleitor facultativo')
else:
    print('não eleitor')

for i in range(0,5):
    print(i)

for i in range(10):
    print(i)

for i in range(0,10, 2):
    print(i)

lista = [3, 'toni luiz', 2.5, True, 5]
print(lista)
print(type(lista))
print(len(lista))
print(lista[2])
print(type(lista[2]))

print()

for i in lista:
    print(i, type(i), sep='--')
    #print(type(i))
    #print()
'''      
tupla = (3, 'toni luiz', 2.5, True, 5)
print(tupla)
print(type(tupla))
print(len(tupla))
'''
