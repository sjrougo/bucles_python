# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
while True:
    print("Ingrese un número entero:")
    numero_1 = int(input())
    print("Ingrese otro número entero:")
    numero_2 = int(input())
    resultado = 0
    print("A continuación ingrese la operación que desea realizar (+, -, *, /, **) \nNOTA: Si desea finalizar la tarea, ingrese la palabra FIN")
    operacion = input()
    if (operacion == '+') or (operacion == '-') or (operacion == '*') or (operacion == '/') or (operacion == '**') or (operacion == 'FIN'):
        if (operacion == '+'):
            resultado = numero_1 + numero_2
        elif (operacion == '-'):
            resultado = numero_1 - numero_2
        elif (operacion == '*'):
            resultado = numero_1 * numero_2
        elif (operacion == '/'):
            resultado = numero_1 / numero_2
        elif (operacion == '**'):
            resultado = numero_1 ** numero_2
        else:
            break
        print("El resultado es: ", resultado)
    else:
        print("Debe ingresar un valor válido (+, -, *, /, **, FIN")
print("Muchas gracias!")

''' En el ejercicio realiza dentro del bucle una consulta para ver si el valor ingresado por el usuario se corresponde con alguno de los
solicitados, de ser así, ingresa al if y luego hay una serie de if anidados para determinar qué valor ingresó el usuario. De haber ingresado
un valor diferente, devuelve un mensaje de aviso y vuelve a ingresar al bucle. En cada ciclo, se pide dos nros nuevos.'''
