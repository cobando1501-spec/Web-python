print("=== SISTEMA DE ACCESO ===")

usuario_correcto = input("Cree un nombre de usuario: ")
clave_correcta = input("Cree una contraseña: ")

intentos = 0
acceso = False

while intentos < 3 and acceso == False:

    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("¡Acceso concedido!")

    else:
        intentos += 1
        print("Usuario o contraseña incorrectos.")

        if intentos < 3:
            print("Te quedan", 3 - intentos, "intentos.")

if acceso == False:
    print("Has superado el número de intentos.")
