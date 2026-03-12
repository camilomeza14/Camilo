# --- CONFIGURACIÓN INICIAL ---

capacidad = 0
while capacidad <= 0:
    try:
        capacidad = int(input("Ingrese la capacidad total de la sala: "))
        if capacidad <= 0:
            print("❌ La capacidad debe ser al menos de 1 persona.")
    except ValueError:
        print("❌ Error: Debes ingresar un número entero para la capacidad.")

# Variables para contar
ingresados = 0
niños = 0
adultos = 0
mayores = 0

# --- PROCESO DE INGRESO ---

while ingresados < capacidad:
    print("\nAsientos ocupados:", ingresados, "de", capacidad)
    opcion = input("Ingrese la edad de la persona (o escriba 'salir' para cerrar): ").lower().strip()
    
    if opcion == "salir":
        break
    
    
    try:
        edad = int(opcion)
        if edad < 0:
            print("❌ La edad no puede ser negativa. Intente de nuevo.")
            continue # Vuelve a pedir la edad para este mismo asiento
            
        
        if edad < 12:
            print("Clasificación: Niño")
            niños = niños + 1
        elif edad >= 12 and edad <= 59:
            print("Clasificación: Adulto")
            adultos = adultos + 1
        else:
            print("Clasificación: Adulto Mayor")
            mayores = mayores + 1
        
        
        ingresados = ingresados + 1
        
    except ValueError:
        print("❌ Error: Ingrese la edad en números o la palabra 'salir'.")

# --- REPORTE FINAL ---
print("\n" + "="*35)
print("REPORTE DE LA SALA")
print("="*35)
print("Total personas ingresadas:", ingresados)
print("Cantidad de Niños:", niños)
print("Cantidad de Adultos:", adultos)
print("Cantidad de Adultos Mayores:", mayores)


if ingresados == capacidad:
    print("ESTADO DE LA SALA: Totalmente llena ✅")
else:
    asientos_libres = capacidad - ingresados
    print("ESTADO DE LA SALA: Quedaron", asientos_libres, "asientos vacíos 🪑")