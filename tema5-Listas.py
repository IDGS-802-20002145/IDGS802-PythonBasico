'''
Listas
* Una lista es una secuencia de elementos
* Cuando se asigna a una variable, permite agrupar varios elementos en un solo lugar
* Se crean los [] o con la Keyword list

'''


lista1=[] #Esta es una lista vacía 
lista=["Sergio",33,9.5,True,"Alba",20,8]

print(lista)
print(lista[:]) #Recorre toda la lista

print(lista[2])
print(lista[-1])
print(lista[0:3])

print(lista[3:])

lista.append("Arguello")
print(lista)

lista.insert(2,"Laura")
print(lista)
lista.extend(["uno",1.1,False])
print(lista)

lista.remove(8)
print(lista)

lista.pop()
print(lista)

lista2=["tres","cuatro"]

lista3 = lista + lista2

print(lista3)

print(lista2*4)

lista4=[2,1,5,4,3]
lista4.sort()
print(lista4)

del lista4[0]
print(lista4)