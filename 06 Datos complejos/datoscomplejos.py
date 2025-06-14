#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

#3
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

#4
contactos = {}

for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    contactos[nombre] = telefono

nombre_consulta = input("Ingrese el nombre que desea buscar: ")
print(contactos.get(nombre_consulta, "No encontrado"))

#5
frase = input("Ingrese una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento)

#6
alumnos = {}

for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(map(int, input("Ingrese tres notas separadas por espacio: ").split()))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Promedio = {promedio:.2f}")

#7
parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {3, 4, 5, 6, 7}

ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2
total_aprobados = parcial_1 | parcial_2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Total de aprobados:", total_aprobados)

#8
stock = {}

while True:
    accion = input("Consultar (C), Agregar stock (A), Nuevo producto (N), Salir (S): ").upper()
    
    if accion == "C":
        producto = input("Ingrese el producto a consultar: ")
        print(f"Stock de {producto}: {stock.get(producto, 'No encontrado')}")
    
    elif accion == "A":
        producto = input("Ingrese el producto a actualizar: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        stock[producto] = stock.get(producto, 0) + cantidad
    
    elif accion == "N":
        producto = input("Ingrese el nuevo producto: ")
        cantidad = int(input("Ingrese la cantidad inicial: "))
        stock[producto] = cantidad
    
    elif accion == "S":
        break

#9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")
print(agenda.get((dia, hora), "No hay eventos en este horario"))

#10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}
print("Diccionario invertido:", invertido)
