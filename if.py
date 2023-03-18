#Condicional if
"""si la condicion es verdadera ejecuta un bloque de codigo segun lo requerido
palabra reservada condicion termina en dos puntos (:) y automaticamente se le asigna la identacion,
si se sale ya no haria parte de la condicional. la condicion que si es verdadera ejecuta en el mismo bloque"""
#ingresar edad usuario y muestre si es mayor de edad
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print(nombre,"Eres mayor de edad")
else:
    print("eres menot de edad")