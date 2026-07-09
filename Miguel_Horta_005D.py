Listas_Juegos
juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}
inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}
def clave_case_insensitive(diccionario, codigo):
    buscada = codigo.strip().lower()
    for clave in diccionario:
        if clave.lower() == buscada:
            return clave
    return None
def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("\n1. Stock por plataforma")
    print("\n2. Búsqueda de juegos por rango de precio")
    print("\n3. Actualizar precio de juego")
    print("\n4. Agregar juego")
    print("\n5. Eliminar juego")
    print("\n6. Salir")
def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-6): ").strip())
            if 1 <= opcion <= 6:
                return opcion 
        except ValueError:
            pass
        print("Opcion invalida")

def stock_por_categoria(juegos_dict, inventario_dict, categoria):
    total_stock = 0
    categoria_busqueda = categoria.strip().lower()
    for codigo_juego, datos_juego in juegos_dict.items():
        if datos_juego[1].strip().lower() == categoria_busqueda:
            clave_inventario = clave_case_insensitive(inventario_dict, codigo_juego)
            if clave_inventario:
                total_stock += int(inventario_dict[clave_inventario][1])
    print(f"Stock total para '{categoria}': {total_stock}")

def busqueda_por_rango_precio(juegos_dict, inventario_dict, precio_minimo, precio_maximo):
    resultados = []
    for codigo_inventario, datos_inventario in inventario_dict.items():
        precio = int(datos_inventario[0])
        stock = int(datos_inventario[1])
        if precio_minimo <= precio <= precio_maximo and stock != 0:
            nombre_juego = juegos_dict.get(codigo_inventario, ["nombre desconocido"][0])
            resultados.append(f"{nombre_juego}--{codigo_inventario}")
    if resultados:
        for item in sorted (resultados):
            print(item)
    else:
        print("No hay coincidencias en ese rango")

def actualizar_precio(inventario_dict, codigo, nuevo_precio):
    clave_inventario = clave_case_insensitive(inventario_dict, codigo)
    if clave_inventario: 
        inventario_dict clave_inventario[0] = int(nuevo_precio)
        return True
    return False
def agregar_juego (juegos_dict, inventario_dict, codigo, nombre, categoria, editor, precio, stock)
    if clave_case_insensitive(juegos_dict)

def eliminar_juego ()
    
def validar_


programa_princi

def men():
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            stock_por_categoria(juegos, inventario, input("categoria: "))
        elif opcion == 2:
            try:
                precio_minimo = int(input("precio minimo: ").strip())
                precio_maximo = int(input("precio maximo:").strip())
            except ValueError:
                print("precios deben ser enteros.")
                continue
            busqueda_por_rango_precio(juegos, inventario, precio_minimo, precio_maximo)
        elif opcion == 3:
            codigo_actualizar = input("Codigo a actualizar: ").strip()
            nuevo_precio_input = input("Nuevo precio (entero > 0)").strip()
            if not es_entero_positivo 
            





