Num = 23
num1 = 1.25
valor = "hola"
v1 = True
print(type(num1)) 

# un solo rengloncito
#para un parrafo grande se utilizan estos("""""")

#operaciones basicas
dato1 = 4
dato2 = 2
potenciacion = dato1**dato2
print("El resultado de la operacion es:", potenciacion)

dato1 = 4
dato2 = 2
division = dato1 // dato2
print("El resultado de la operacion es:", division)

#para una division si se poine / el resultado va a ser float si se pone // el resultado queda entero

dato1 = 40
dato2 = 2
division = dato1 // dato2
print(f"El resultado de la operacion es {division}")

dato1 = 40
dato2 = 2
division = dato1 // dato2
print("El resultado de la operacion es {0}".format(division))

dato1 = 40
dato2 = 2
division = dato1 // dato2
print("Elresultado es %d" % (division))

#tipos de formatos
# la f hace que las {} funcionen 
# format se pone el texto "jiji{0}".format ""por fuera se pone el format(nombre variable)""
# la otra forma es con &d


dato1 = int(input("Ingrese un numero:")) 
dato2 = int(input("Ingrese un numero:"))
division = dato1 // dato2
print("El resultado es %d" % (division))
#si no se pone int(no muestra como entrero) va a arrojar un error

#metodos lower(), upper(), title()
texto = "hola grupo!!!"
print(texto.lower())
print(texto.upper())
print(texto.title())
#upper lo convierte en mayuscula y lower para miniscula y title para iniciar la primera letra con mayuscula

horallegada = 8
horasalida = 12
preciohora = 3500
totalhoras = horasalida - horallegada
total = preciohora * totalhoras
print("el valor hora es", totalhoras, "total hora", total)

dato1 = int(input("Ingrese un numero:")) 
dato2 = int(input("Ingrese un numero:"))
division = dato1 // dato2
residuo = dato1 % dato2
print ("Su dividendo es %d" % (dato1))
print ("Su divisor es %d" % (dato2))
print("Su cociente es %d" % (division))
print("Su residuo es %d" % (residuo))

print ("El cociente es", dato1 // dato2, "El residuo es", dato1 % dato2, "El dividendo es","\n", "y el divisor es", dato2)
dato1 = int(input("Ingrese un numero:")) 
dato2 = int(input("Ingrese un numero:"))
print (f"\tcociente {dato1//dato2}\n\tresiduo {dato1%dato2}\n\tdividendo {dato1}\n\tdivisor {dato2}")

#\n es para hacer un salto de linea
#\t es para hacer una tabulacion