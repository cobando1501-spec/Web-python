print("=========================")
print(" TIENDA DE VIDEOJUEGOS")
print("=========================")

Minecraft = 15000
Fifa = 25000
Gta = 20000
Fortnite = 18000
CallOfDuty = 30000
Roblox = 12000

print("Videojuegos disponibles:")
print("1. Minecraft - 15000")
print("2. Fifa - 25000")
print("3. GTA - 20000")
print("4. Fortnite - 18000")
print("5. Call of Duty - 30000")
print("6. Roblox - 12000")

opcion = int(input("Seleccione un número del 1 al 6: "))
cantidad = int(input("¿Cuántas unidades desea comprar? "))

# Condicionales
if opcion == 1:
    total = Minecraft * cantidad

elif opcion == 2:
    total = Fifa * cantidad

elif opcion == 3:
    total = Gta * cantidad

elif opcion == 4:
    total = Fortnite * cantidad

elif opcion == 5:
    total = CallOfDuty * cantidad

elif opcion == 6:
    total = Roblox * cantidad

else:
    total = 0
    print("Opción no válida.")

print("===========================================")
print("El total de su compra es:", total)
