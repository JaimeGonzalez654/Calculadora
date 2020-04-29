print ("Calculadora")
print("=======================================================================")
print ("¿que operacion desea realizar?")
print("presione 1 para una adicion")
print("presione 2 para una sustraccion")
print("presione 3 para una multiplicacion")
print("presione 4 para una division")

opcion = float(input())
if opcion == 1:
 print ("introduce el primer numero")
 num_1 = float (input())
 print ("introduce el segundo numero")

 num_2 = float (input())
 resultado_1 = (num_1 + num_2)
 print("el resultado de tu suma es ", resultado_1)

##########################################

elif opcion == 2:
 print ("introduce el primer numero")
 num_3 = float (input())
 print ("introduce el segundo numero")

 num_4 = float (input())
 resultado_2 = (num_3 - num_4)
 print("el resultado de tu resta es ", resultado_2)

##########################################

elif opcion == 3:
 print ("introduce el primer numero")
 num_5 = float (input())
 print ("introduce el segundo numero")

 num_6 = float (input())
 resultado_3 = (num_5 * num_6)
 print("el resultado de tu multiplicación es ", resultado_3)

##########################################

elif opcion == 4:
 print ("introduce el primer numero")
 num_7 = float (input())
 print ("introduce el segundo numero")

 num_8 = float (input())
 resultado_4 = (num_7 / num_8)
 print("el resultado de tu multiplicación es ", resultado_4)

##########################################

else:
 print("la operacion no existe")

 ###JAIME GONZALEZ###
