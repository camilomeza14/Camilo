tarifa_carro = 4000
tarifa_moto = 2000 
contador_carro = 0
contador_moto = 0
vehiculo_mas_pago =" "
pago_mayor = 0
for i in range(1,2,1):
    placa = input("Ingrese la placa: ")
    tipo_de_vehiculo = input("Carro o Moto: ")
    horas_parqueado = int(input("Cuantas horas llevas parqueado?: "))
    
    if tipo_de_vehiculo == "Carro": 
        contador_carro += 1 
        tarifa = tarifa_carro
    elif tipo_de_vehiculo == "Moto":
        contador_moto += 1 
        tarifa = tarifa_moto


    pagado = tarifa * horas_parqueado 

    if pagado > pago_mayor:
        pago_mayor= pagado
        vehiculo_mas_pago = f"El producto que mas pagó es: {tipo_de_vehiculo}  placa {placa}"
    
    print("vehiculo_mas_pago") 