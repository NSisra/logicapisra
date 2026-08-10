print("GENERADOR SEGURO DE CONTRASEÑAS")

longitud = int(input("Ingrese la longitud de la contraseña:"))

#Bucle para solicitar un valor que este dentro del rango solicitado

while longitud < 8 or longitud > 30:

    if longitud < 8:
        print("La contraseña debe tener al menos 8 caracteres.")

    elif longitud > 30:
        print("La contraseña no puede superar los 30 caracteres.")

    longitud = int(input("Ingrese nuevamente la longitud de la contraseña:"))

#Fin de bucle, valor dentro del rango

print("Longitud válida.")

#Variables de configuración para la contraseña

mayusculas = input("¿Desea incluir mayúsculas? (s/n):")
minusculas = input("¿Desea incluir minúsculas? (s/n):")
numeros = input("¿Desea incluir números? (s/n):")
simbolos = input("¿Desea incluir símbolos? (s/n):")

#Otro bucle, donde si el usuario no elije almenos una variable, el ciclo se repite

while mayusculas != "s" and minusculas != "s" and numeros != "s" and simbolos != "s":
    print("Debe seleccionar al menos un tipo de carácter.")

    mayusculas = input("¿Desea incluir mayúsculas? (s/n):")
    minusculas = input("¿Desea incluir minúsculas? (s/n):")
    numeros = input("¿Desea incluir números? (s/n):")
    simbolos = input("¿Desea incluir símbolos? (s/n):")

print("Configuración aceptada.")
print("Por favor espere mientras su contraseña segura se genera...")