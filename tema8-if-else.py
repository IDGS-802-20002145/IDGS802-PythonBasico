print("Suma de Números")

num1=int(input("Dame el primer número: "))

num2=int(input("Dame el segundo número: "))

if num1 > num2 :
    print("El {} es mayor que el {}".format(num1,num2))
else:
    print("El {1} es mayor que el {0}".format(num1,num2))

print("--------------------Pedir Edad-----------------")

edad=int(input("Ingrese su edad: "))

if edad > 18 :
    print("Es mayor de edad")
elif edad == 18 :
    print("Tiene 18 años cumplidos")
else:
    print("el es menor de edad")
