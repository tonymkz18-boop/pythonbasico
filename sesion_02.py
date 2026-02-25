# Tuplas
mi_tupla = (2, 4)
print("mi tupla: ",mi_tupla)

# Lista
mi_lista = [1, 2.1416, "ian", mi_tupla]
print("El primer elemento de mi lista:",mi_lista[0])
print("El cuarto elemento de mi lista:",mi_lista[3])
print("El tercero elemento de mi lista:",mi_lista[2])

# Diccionarios
mi_diccionario = {"mi_lista": mi_lista,
                  "nombre": "ian" ,
                  "pi": 3.1416,
                  "tel": "664-5580828"}
print("llave para accesar a mi diccionario mi_lista", mi_diccionario["mi_lista"])
print("llave para accesar a mi diccionario pi", mi_diccionario["pi"])
print("llave para accesar a mi diccionario tel", mi_diccionario["tel"])
