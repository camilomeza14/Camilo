total_dia = 0
cont_corte = 0
cont_cepillado = 0
cont_tintura = 0

for i in range(7):
    print("\n--- Cliente", i+1, "---")
    nombre = input("Nombre: ")
    servicio = input("Servicio (corte, cepillado, tintura): ")
    pago = int(input("Valor pagado: "))
    
    total_dia = total_dia + pago
    
    if servicio == "corte":
        cont_corte = cont_corte + 1
    elif servicio == "cepillado":
        cont_cepillado = cont_cepillado + 1
    elif servicio == "tintura":
        cont_tintura = cont_tintura + 1

print("\n--- REPORTE ---")
print("Total recaudado: $", total_dia)
print("Cortes:", cont_corte, "| Cepillados:", cont_cepillado, "| Tinturas:", cont_tintura)


if cont_corte > cont_cepillado and cont_corte > cont_tintura:
    print("Servicio más solicitado: Corte")
elif cont_cepillado > cont_corte and cont_cepillado > cont_tintura:
    print("Servicio más solicitado: Cepillado")
else:
    print("Servicio más solicitado: Tintura")
