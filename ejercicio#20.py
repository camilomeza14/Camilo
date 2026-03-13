total_dinero = 0
c_basico = 0
c_premium = 0
c_familiar = 0

opcion = "si"
while opcion == "si":
    nombre = input("\nNombre: ")
    edad = int(input("Edad: "))
    
    
    if edad < 18:
        print("Aviso: Registro juvenil")
    elif edad >= 60:
        print("Aviso: Beneficio senior")
        
    plan = input("Tipo de plan (básico, premium, familiar): ")
    
    if plan == "básico":
        total_dinero = total_dinero + 50000
        c_basico = c_basico + 1
    elif plan == "premium":
        total_dinero = total_dinero + 90000
        c_premium = c_premium + 1
    elif plan == "familiar":
        total_dinero = total_dinero + 130000
        c_familiar = c_familiar + 1
        
    opcion = input("¿Registrar otra persona? (si/no): ")

print("\n--- CIERRE DE CAJA ---")
print("Total recaudado: $", total_dinero)
print("Ventas -> Básico:", c_basico, "| Premium:", c_premium, "| Familiar:", c_familiar)


if c_basico > c_premium and c_basico > c_familiar:
    print("El plan más vendido fue: Básico")
elif c_premium > c_basico and c_premium > c_familiar:
    print("El plan más vendido fue: Premium")
else:
    print("El plan más vendido fue: Familiar")
