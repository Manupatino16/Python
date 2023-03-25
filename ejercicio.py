#Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a 2.500.000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no

edad = int(input("¿Cuál es tu edad? "))
ingresos = float(input("¿Cuál es tu ingreso mensual? "))

if edad >= 18 and ingresos >= 2500000:
    print("Debes tributar.")
else:
    print("No debes tributar.")

#Escribir un programa donde se ingrese la nota de las materias: desarrollo de software, matemáticas, lógica programación, si el promedio es mayor o igual que 3,0 muestre en pantalla aprobado, de lo contrario muestre en pantalla reprobado

desarrollo_de_software = float(input("Ingrese la nota de desarrollo de software: "))
matematicas = float(input("Ingrese la nota de matemáticas: "))
logica_programacion = float(input("Ingrese la nota de lógica programación: "))

promedio = (desarrollo_de_software + matematicas + logica_programacion) / 3

if promedio >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")

#ELIF 
#Comparar 4 números solicitados al usuario, escribir condiciones que permita mostrar que un número fue escrito 2, que todos son iguales o por el contrario todos son diferentes

num1 = int(input("Ingresa el numero 1 :"))
num2 = int(input("Ingresa el numero 2 :"))
num3 = int(input("Ingresa el numero 3 :"))
num4 = int(input("Ingresa el numero 4 :"))
if num1 == num2 or num1 == num3 or num1 == num4:
    print("Se escribió al menos un número dos veces.")
elif num1 == num2 == num3 == num4:
    print("Todos los números son iguales.")
else:
    print("Todos los números son diferentes.")

#Realizar un programa que muestre un menú con opciones de colores primario (Amarillo, azul, rojo, blanco y negro), el usuario debe escoger 2 colores de los ofrecidos en el menú y con una secuencia de if y elif evaluar las posibles combinaciones generadas con los colores primarios. Si el usuario escogió colores que no generan otro al ser combinados debe mostrar un mensaje de “opciones no validas”

print("Menú de colores primarios:")
print("1. Amarillo")
print("2. Azul")
print("3. Rojo")
print("4. Blanco")
print("5. Negro")

color1 = int(input("Elija el primer color (escriba el número correspondiente): "))
color2 = int(input("Elija el segundo color (escriba el número correspondiente): "))

if color1 == 1 and color2 == 2 or color1 == 2 and color2 == 1:
    print("La combinación de amarillo y azul da como resultado el color verde")
elif color1 == 1 and color2 == 3 or color1 == 3 and color2 == 1:
    print("La combinación de amarillo y rojo da como resultado el color naranja")
elif color1 == 2 and color2 == 3 or color1 == 3 and color2 == 2:
    print("La combinación de azul y rojo da como resultado el color morado")
elif color1 == 1 and color2 == 4 or color1 == 4 and color2 == 1:
    print("La combinación de amarillo y blanco da como resultado el color amarillo claro")
elif color1 == 2 and color2 == 4 or color1 == 4 and color2 == 2:
    print("La combinación de azul y blanco no genera otro color primario")
elif color1 == 3 and color2 == 4 or color1 == 4 and color2 == 3:
    print("La combinación de rojo y blanco no genera otro color primario")
elif color1 == 1 and color2 == 5 or color1 == 5 and color2 == 1:
    print("La combinación de amarillo y negro no genera otro color primario")
elif color1 == 2 and color2 == 5 or color1 == 5 and color2 == 2:
    print("La combinación de azul y negro no genera otro color primario")
elif color1 == 3 and color2 == 5 or color1 == 5 and color2 == 3:
    print("La combinación de rojo y negro no genera otro color primario")
elif color1 == 4 and color2 == 5 or color1 == 5 and color2 == 4:
    print("La combinación de blanco y negro no genera otro color primario")
else:
    print("Opciones no válidas")
