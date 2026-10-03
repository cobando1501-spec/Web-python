# Cajero automatico sencillo con python
print("=============================")
print("     CAJERO AUNTOMATICO ")
print("=============================")
user = input("¿Cual es su usuario? : ")
password = input("¿Cual es su contraseña?: ")
saldo_inicial = int(input("Cuanto dinero tiene: "))
print()
print("=============================================")
print("   MENÚ    ")
print("  Precione 1 si desea consultar su saldo           ")
print("  Precione 2 si desea retirar su dinero")
print("=============================================")
opciones = int(input("Seleccione la opción que necesita: "))

if opciones == 1:
    print(f"su saldo seria: {saldo_inicial} ")
elif opciones == 2:
    retiro = float(input("¿Cuánto dinero desea retirar?: "))
    if retiro <= saldo_inicial:
        saldo_restante = saldo_inicial - retiro
        print("Si se pudo retirar")
        print(f"Su nuevo saldo es: {saldo_restante}")
    else:
        print("No se puede retirar, saldo insuficiente")
