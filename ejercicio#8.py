caros = 0
for i in range(6): 
    precio = float(input(f"Precio producto {i+1}: "))
    if precio > 100000: caros += 1 
print(f"Productos caros: {caros}")