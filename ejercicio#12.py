bajo = 0
medio = 0
alto = 0

for i in range(5):
    print("\n--- Registro", i+1, "---")
    nombre = input("Nombre: ")
    
    
    dias = -1 
    while dias < 0 or dias > 7:
        try:
            dias = int(input("Días asistidos en la semana (0-7): "))
            if dias < 0 or dias > 7:
                print("❌ Error: La semana solo tiene de 0 a 7 días. Intenta de nuevo.")
        except ValueError:
            print("❌ Error: Debes ingresar un número entero para los días.")
            dias = -1 

    
    minutos = -1.0
    while minutos < 0:
        try:
            minutos = float(input("Minutos promedio por día: "))
            if minutos < 0:
                print("❌ Error: Los minutos no pueden ser negativos. Intenta de nuevo.")
        except ValueError:
            print("❌ Error: Debes ingresar un número (puedes usar decimales) para los minutos.")
            minutos = -1.0 
    
    if dias < 3:
        bajo = bajo + 1
    elif dias == 3 or dias == 4:
        medio = medio + 1
    else:
        alto = alto + 1

print("\n" + "="*20)
print("CONTEO FINAL")
print("Bajo compromiso:", bajo)
print("Compromiso medio:", medio)
print("Compromiso alto:", alto)
print("="*20)