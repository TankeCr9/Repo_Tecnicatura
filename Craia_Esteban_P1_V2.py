# --- SISTEMA DE CONTROL DE INVENTARIO ---
# Estudiante: Craia, Esteban 

# Estructuras de Datos
herramientas = []
existencias = []

opcion = ""

while opcion != "8":
    print("\n========================================")
    print("      CONTROL DE INVENTARIO")
    print("========================================")
    print("1. Carga Inicial de Herramientas")
    print("2. Carga de Existencias")
    print("3. Visualización de Inventario")
    print("4. Consulta de Stock")
    print("5. Reporte de Agotados")
    print("6. Alta de Nuevo Producto")
    print("7. Actualización de Stock")
    print("8. Salir")
    print("========================================")
    
    opcion = input("Seleccione una opción (1-8): ")

    # 1. CARGA INICIAL
    if opcion == "1":
        cantidad_str = input("¿Cuántas herramientas desea registrar?: ")
        if cantidad_str.isdigit():
            cantidad = int(cantidad_str)
            for i in range(cantidad):
                nombre_valido = False
                while not nombre_valido:
                    nombre = input(f"Nombre herramienta {i+1}: ").strip()
                    if nombre == "":
                        print("Error: El nombre no puede estar vacío.")
                    else:
                        # Validar duplicados
                        existe = False
                        for h in herramientas:
                            if h.lower() == nombre.lower():
                                existe = True
                        if existe:
                            print("Error: El producto ya existe.")
                        else:
                            herramientas.append(nombre)
                            existencias.append(0)  # Inicializo con stock 0
                            nombre_valido = True
        else:
            print("Error: Debe ingresar un número entero.")

    # 2. CARGA DE EXISTENCIAS (VALIDACIÓN DE STOCK)
    elif opcion == "2":
        if len(herramientas) == 0:
            print("Error: No hay herramientas ingresadas. Use las opciones 1 o 6.")
        else:
            for i in range(len(herramientas)):
                valido = False
                while not valido:
                    print(f"\nProducto: {herramientas[i]}")
                    print(f"Stock actual: {existencias[i]}")
                    stock_in = input("Nuevo stock (0 para no modificar el stock actual): ")
                    
                    if stock_in.isdigit():
                        nuevo_valor = int(stock_in)
                        # Si pone 0 pero ya tenía stock, se mantiene el anterior
                        if nuevo_valor == 0 and existencias[i] > 0:
                            print(f"Stock no sufrio modificaciones: {existencias[i]} unidades")
                        else:
                            existencias[i] = nuevo_valor
                        valido = True
                    else:
                        print("Error: Ingrese un número entero positivo.")

    # 3. VISUALIZACIÓN
    elif opcion == "3":
        print("\n--- INVENTARIO ACTUAL ---")
        if len(herramientas) == 0:
            print("El inventario está vacío.")
        else:
            for i in range(len(herramientas)):
                print(f"[{i}] Herramienta: {herramientas[i]:<15} | Stock: {existencias[i]}")

    # 4. CONSULTA DE STOCK
    elif opcion == "4":
        busqueda = input("Buscar herramienta: ").strip()
        encontrado = False
        for i in range(len(herramientas)):
            if herramientas[i].lower() == busqueda.lower():
                print(f"Resultado: {herramientas[i]} tiene {existencias[i]} unidades.")
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")

    # 5. REPORTE DE AGOTADOS
    elif opcion == "5":
        print("\n--- PRODUCTOS SIN STOCK ---")
        hay_agotados = False
        for i in range(len(herramientas)):
            if existencias[i] == 0:
                print(f"AGOTADO: {herramientas[i]}")
                hay_agotados = True
        if not hay_agotados:
            print("No hay productos agotados.")

    # 6. ALTA DE NUEVO PRODUCTO
    elif opcion == "6":
        nombre_nuevo = input("Nombre del nuevo producto: ").strip()
        duplicado = False
        for h in herramientas:
            if h.lower() == nombre_nuevo.lower():
                duplicado = True
        
        if nombre_nuevo == "":
            print("Error: Nombre vacío. Volviendo al menú.")
        elif duplicado:
            print("Error: El producto ya existe. Volviendo al menú.")
        else:
            stock_nuevo = input("Ingrese stock inicial: ")
            if stock_nuevo.isdigit() and int(stock_nuevo) >= 0:
                herramientas.append(nombre_nuevo)
                existencias.append(int(stock_nuevo))
                print("Producto registrado exitosamente.")
            else:
                print("Error: Stock inválido. Volviendo al menú.")

    # 7. ACTUALIZACIÓN (VENTA/INGRESO)
    elif opcion == "7":
        buscar = input("Nombre del producto a actualizar: ").strip()
        indice = -1
        for i in range(len(herramientas)):
            if herramientas[i].lower() == buscar.lower():
                indice = i
        
        if indice == -1:
            print("Error: Producto no encontrado.")
        else:
            print(f"Producto: {herramientas[indice]} | Stock: {existencias[indice]}")
            print("1. Venta (Quitar) / 2. Ingreso (Agregar)")
            accion = input("Seleccione: ")
            cant_str = input("Cantidad: ")
            
            if cant_str.isdigit():
                cant = int(cant_str)
                if accion == "1":
                    if existencias[indice] >= cant:
                        existencias[indice] -= cant
                        print("Venta finalizada.")
                    else:
                        print("Error: Stock insuficiente.")
                elif accion == "2":
                    existencias[indice] += cant
                    print("Stock actualizado.")
            else:
                print("Error: Cantidad no válida.")

    elif opcion == "8":
        print("Saliendo del sistema. ¡Chau, Gracias nos estamos viendo!")
    else:
        print("Opción inválida, intente de nuevo.")