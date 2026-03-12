total_acumulado_dia = 0

while True:
    
    entrada = input("\nProducto (café, capuchino, pastel) o 'salir': ").lower().strip()
    
    if entrada == "salir":
        break
    
    
    if entrada == "cafe" or entrada == "café":
        producto = "café"
        precio_unitario = 4000
    elif entrada == "capuchino":
        producto = "capuchino"
        precio_unitario = 7000
    elif entrada == "pastel":
        producto = "pastel"
        precio_unitario = 6000
    else:
        print("❌ Ese producto no existe. Intenta de nuevo.")
        continue

    
    cantidad = -1
    while cantidad <= 0:
        try:
            cantidad = int(input("¿Cuántas unidades desea? "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor a 0.")
        except ValueError:
            print("❌ Error: Debes ingresar un número entero.")
            cantidad = -1

    
    subtotal = precio_unitario * cantidad
    
    
    if subtotal > 20000:
        subtotal = subtotal * 0.90
        print("✨ ¡Descuento del 10% aplicado a esta compra!")

    
    print("----------------------------------")
    print("Detalle: ", cantidad, " ", producto)
    print("TOTAL A PAGAR CLIENTE: $", subtotal)
    print("----------------------------------")
    
    
    total_acumulado_dia = total_acumulado_dia + subtotal


print("\n" + "="*35)
print("REPORTE DE CIERRE DE CAJA")
print("TOTAL ACUMULADO DEL DÍA: $", total_acumulado_dia)
print("="*35)