'''
Leer el número del tecado 

Respuesta esperada...

5x1 = 5
.
.
.

5 x 10 = 50 

'''


t=int(input("Ingresa el número de la tabla que deseas generar: "))

print("La tabla es: ")
for tb in range(1,11):
    print("{} x {} = {}".format(t,tb,(t*tb)))

print()
print("La tabla con un while")
i=1
while i <=10 :
    print("{} x {} = {}".format(t,i,(t*i)))
    i+=1

