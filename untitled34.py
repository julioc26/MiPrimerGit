cadena = 'Hola Mundo'

l=[c for c in cadena if c.isupper()]
print(l)

cadena = 'Hola Mundo'
lista = [[letra for letra in cadena if letra.isupper()], [letra for letra in cadena if letra.islower()]]
print(lista)


cadena = 'Hola Mundo'
l=[[c for c in cadena if c.isupper()], [c for c in cadena if c.islower()]]
print(l)


