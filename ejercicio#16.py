
total_alimento = 0
total_juguete = 0
total_accesorio = 0

for i in range(10):
    print("\n--- Venta", i+1, "---")
    categoria = input("Categoría (alimento, juguete, accesorio): ")
    valor = int(input("Valor de la compra: "))
    
    if categoria == "alimento":
        total_alimento = total_alimento + valor
    elif categoria == "juguete":
        total_juguete = total_juguete + valor
    elif categoria == "accesorio":
        total_accesorio = total_accesorio + valor

print("\n--- RESULTADOS ---")
print("Ventas Alimento: $", total_alimento)
print("Ventas Juguete: $", total_juguete)
print("Ventas Accesorio: $", total_accesorio)


if total_alimento > total_juguete and total_alimento > total_accesorio:
    print("La categoría que más generó fue: Alimento")
elif total_juguete > total_alimento and total_juguete > total_accesorio:
    print("La categoría que más generó fue: Juguete")
else:
    print("La categoría que más generó fue: Accesorio")
