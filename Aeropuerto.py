reservas = {}
id_compra = [1]

def generar_id_compra():
    id = id_compra[0]
    id_compra[0] += 1

def registrar_reserva():
    id = id_compra[0]
    generar_id_compra()
    nombre = input("Ingrese nombre del pasajero: ")
    tipo_viaje = input("Ingrese tipo de viaje (nacional/internacional): ")
    destino = input("Ingrese destino: ")
    fecha = input("Ingrese fecha de viaje: ")
    peso_equipaje = float(input("Ingrese peso del equipaje: "))
    if tipo_viaje.lower() == "nacional":
        precio_base = 200000
    else:
        precio_base = 1000000
    if peso_equipaje <= 20:
        costo_equipaje = 50000
    elif peso_equipaje <= 30:
        costo_equipaje = 70000
    else:
        costo_equipaje = 100000
    costo_total = precio_base + costo_equipaje
    reservas[id] = {
        "nombre": nombre,
        "tipo_viaje": tipo_viaje,
        "destino": destino,
        "fecha": fecha,
        "peso_equipaje": peso_equipaje,
        "costo_total": costo_total
    }
    print(f"ID de compra: {id}")
    print(f"Nombre del pasajero: {nombre}")
    print(f"Tipo de viaje: {tipo_viaje}")
    print(f"Destino: {destino}")
    print(f"Fecha de viaje: {fecha}")
    print(f"Peso del equipaje: {peso_equipaje} kg")
    print(f"Costo total: ${costo_total}")

def reporte_reservas():
    for id, reserva in reservas.items():
        print(f"ID de compra: {id}")
        print(f"Nombre del pasajero: {reserva['nombre']}")
        print(f"Tipo de viaje: {reserva['tipo_viaje']}")
        print(f"Destino: {reserva['destino']}")
        print(f"Fecha de viaje: {reserva['fecha']}")
        print(f"Peso del equipaje: {reserva['peso_equipaje']} kg")
        print(f"Costo total: ${reserva['costo_total']}")
        print("------------------------")

def buscar_reserva():
    id = int(input("Ingrese ID de compra: "))
    if id in reservas:
        reserva = reservas[id]
        print(f"Nombre del pasajero: {reserva['nombre']}")
        print(f"Tipo de viaje: {reserva['tipo_viaje']}")
        print(f"Destino: {reserva['destino']}")
        print(f"Fecha de viaje: {reserva['fecha']}")
        print(f"Peso del equipaje: {reserva['peso_equipaje']} kg")
        print(f"Costo total: ${reserva['costo_total']}")
    else:
        print("Reserva no encontrada")

while True:
        print("1. Registrar reserva")
        print("2. Reporte de reservas")
        print("3. Buscar reserva")
        print("4. Salir")
        opcion = input("Ingrese opción: ")
        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            reporte_reservas()
        elif opcion == "3":
            buscar_reserva()
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

