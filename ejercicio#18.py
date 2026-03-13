suma_promedios_grupo = 0
total_estudiantes = 0
mejor_nota = 0
nombre_mejor = ""
bajo = 0
medio = 0
alto = 0

continuar = "si"
while continuar == "si":
    nombre = input("\nNombre del estudiante: ")
    n1 = int(input("Nota Speaking: "))
    n2 = int(input("Nota Listening: "))
    n3 = int(input("Nota Reading: "))
    
    promedio = (n1 + n2 + n3) / 3
    print("Promedio individual:", promedio)
    
    
    if promedio < 60:
        print("Nivel: Bajo")
        bajo = bajo + 1
    elif promedio >= 60 and promedio <= 79:
        print("Nivel: Medio")
        medio = medio + 1
    else:
        print("Nivel: Alto")
        alto = alto + 1
        
    
    suma_promedios_grupo = suma_promedios_grupo + promedio
    total_estudiantes = total_estudiantes + 1
    
    if promedio > mejor_nota:
        mejor_nota = promedio
        nombre_mejor = nombre
        
    continuar = input("¿Desea registrar otro estudiante? (si/no): ")

print("\n--- INFORME FINAL ---")
print("Promedio general del grupo:", suma_promedios_grupo / total_estudiantes)
print("Mejor estudiante:", nombre_mejor, "con nota de", mejor_nota)
print("Niveles -> Bajo:", bajo, "Medio:", medio, "Alto:", alto)
