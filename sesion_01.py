# Nuemros
print(int(7))
print(float(7.7))
print(type(7))
print(type(7.7))
print(int(1+2))
print(int(10*2))
print(int(1 + 4 - 2))
print(float(1 + 2.0))

# Operadores matematicos
# +
# -
# *
# /
# **
# % modulo

print(int(2**3))
print(int(4**8))
print(float(10%3))
print(float(25%4))
print(float(16%2))
print(float(10 / 3))

# Variables 
print("========VARIABLES========")
x = 100
y = 1
print(x+y)

ventas = 199991
print("muestras ventas fueron:",ventas)

is_active = True
print(is_active)

game_over = False
print(game_over)

some_string = "Hola soy un string"
print(some_string)

print("========Condicionales========")
edad = 14

if(edad >= 18):
    print("Si puedes entrar a el bar!!!!!")
else:
     print("No puedes entrar a el bar!!!!!")

mi_numero = int(input("¿Cual es numero que deseas verificar?:"))
print(f"El numero que se desea verificar es {mi_numero}")
if mi_numero % 2 == 0:
     print(f"El numero {mi_numero} es par!!!")
else:
     print(f"El numero {mi_numero} es impar!!!!")

def par_inpar(numero):
    if numero % 2 == 0:
     print(f"El numero {numero} es par!!!")
    else:
     print(f"El numero {numero} es inpar!!!")

mi_numero = int(input("¿Cual es numero que deseas verificar?:"))
print(par_inpar(mi_numero))