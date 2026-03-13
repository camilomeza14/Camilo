cont_agotado = 0
cont_bajo = 0
cont_normal = 0

for i in range(10):
    print("\n--- Producto", i+1, "---")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad disponible: "))
    
    if cantidad == 0:
        print("Estado: Agotado")
        cont_agotado = cont_agotado + 1
    elif cantidad >= 1 and cantidad <= 5:
        print("Estado: Stock bajo")
        cont_bajo = cont_bajo + 1
    else:
        print("Estado: Stock normal")
        cont_normal = cont_normal + 1

print("\n--- RESUMEN DE INVENTARIO ---")
print("Productos Agotados:", cont_agotado)
print("Productos con Stock Bajo:", cont_bajo)
print("Productos con Stock Normal:", cont_normal)
