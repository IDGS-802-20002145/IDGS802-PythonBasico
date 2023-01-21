num1=20
num2=0

#print("La división de {0} entre {1} es: ".format(num1,num2,(num1/num2)))

try:
    resultado = num1/num2
except ZeroDivisionError:
    print("¡ERROR! La división entre cero no es posible")
finally:
    print("Yo siempre aparezco")