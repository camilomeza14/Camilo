

total_vendido = 0
clientes = 0
cono = 0
vaso = 0
banana_split = 0

while True:
    print("\n--- NUEVA VENTA ---")
    producto = input("Producto (cono, vaso, banana split) o 'salir': ").lower()

    if producto == "salir":
        break

    
    if producto != "cono" and producto != "vaso" and producto != "banana split":
        print("Producto inválido. Intente de nuevo.")
        continue

    
    try:
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Error: Debes ingresar un número para la cantidad.")
        continue

    
    if producto == "cono":
        total_cliente = 3000 * cantidad
        cono += cantidad
    elif producto == "vaso":
        total_cliente = 4000 * cantidad
        vaso += cantidad
    elif producto == "banana split":
        total_cliente = 9000 * cantidad
        banana_split += cantidad

    total_vendido += total_cliente
    clientes += 1
    print(f"Total de esta compra: ${total_cliente}")

# --- REPORTE FINAL ---
print("\n==============================")
print("REPORTE FINAL")
print(f"Total vendido: ${total_vendido}")
print(f"Clientes atendidos: {clientes}")


if cono == 0 and vaso == 0 and banana_split == 0:
    print("No se realizaron ventas.")
else:
    
    if cono >= vaso and cono >= banana_split:
        print("Producto más pedido: cono")
    elif vaso >= cono and vaso >= banana_split:
        print("Producto más pedido: vaso")
    else:
        print("Producto más pedido: banana split")
print("==============================")