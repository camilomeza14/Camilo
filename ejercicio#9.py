servicios = ["masaje", "facial", "manicure"] 
deseo = input("¿Qué servicio desea? ").lower()
if deseo in servicios: print("Servicio confirmado") 
else: print("Servicio no disponible")