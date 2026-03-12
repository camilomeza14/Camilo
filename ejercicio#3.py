bebida = input("¿Qué desea (café, té, jugo)? ").lower()
cantidad = int(input("¿Cuántas unidades? "))
precios = {"café": 4000, "té": 3500, "jugo": 5000} 

total = precios.get(bebida, 0) * cantidad
print(f"Total a pagar: ${total}") 