vainilla = 0
chocolate = 0
fresa = 0

for i in range(5): # Registrar 5 clientes 
    sabor = input("Elija sabor (vainilla, chocolate, fresa): ").lower()
    if sabor == "vainilla": vainilla += 1
    elif sabor == "chocolate": chocolate += 1
    elif sabor == "fresa": fresa += 1

print(f"Resultados: Vainilla: {vainilla}, Chocolate: {chocolate}, Fresa: {fresa}") 