tarifa_carro = 4000
tarifa_moto = 2000 
contador_carro = 0
contador_moto = 0
total_recaudado = 0
pago_mayor = 0
vehiculo_mas_pago = ""


for i in range(8):
    print("\n--- Registro del vehículo ---")
    
    placa = input("Ingrese la placa: ")
    tipo_de_vehiculo = input("Carro o Moto: ")
    horas_parqueado = int(input("¿Cuántas horas llevas parqueado?: "))
    
    if tipo_de_vehiculo == "Carro": 
        contador_carro = contador_carro + 1 
        tarifa = tarifa_carro
    elif tipo_de_vehiculo == "Moto":
        contador_moto = contador_moto + 1 
        tarifa = tarifa_moto

    
    pagado = tarifa * horas_parqueado 
    print("Este vehículo debe pagar: $", pagado)

    
    total_recaudado = total_recaudado + pagado

    
    if pagado > pago_mayor:
        pago_mayor = pagado
        vehiculo_mas_pago = "El vehículo que más pagó es el de placa " + placa + " con un total de $" + str(pagado)
    

print("\n--- REPORTE FINAL ---")
print("Total recaudado en el día: $", total_recaudado)
print("Cantidad de carros:", contador_carro)
print("Cantidad de motos:", contador_moto)
print(vehiculo_mas_pago)
