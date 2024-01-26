##### Python jako kalkulačka #####

# Sčítání
print(2 + 3)
print(2 + 3.5)

# Odčítání
print(2 - 3)

# Násobení
print(2 * 3)

# Dělení
print(2 / 3)

# Celočíselné dělení
print(7 // 3)

# Zbytek po dělení
print(7 % 2)

# modul math, ten obsahuje funkce pro matematické operace
import math # importování modulu math
print(math.sqrt(9)) # odmocnina
print(math.log(1)) # logaritmus

from math import sqrt, log # importování konkrétních funkcí z modulu math
print(sqrt(100))
print(math.log(1))
print(math.pi) # konstanta pi

print(len("3.141592653589793"))  # délka řetězce

# Umocňování
print(2 ** (1/2))

# Celá čísla jsou typu int
print(type(1))  # int

# Čísla s desetinnou čárkou jsou typu float
print(type(1.1111222))  # float

# komplexní čísla
print(type(1 + 1j))

# Boolovské hodnoty: True, False

# Logické výrazy
print(5 > 3)  # výsledek je True
print(5 < 3)  # výsledek je False
print(5 <= 3)  # výsledek je False
print(5 >= 3)  # výsledek je True
print(5 == 3)  # výsledek je False

x = 5
print(x == 5)  # výsledek je True

# Logické spojky: and, or, not
print(True and True)  
print(True and False)
print(False and False)
print(True == True and True == False)
print(4 == 4 or 4 == 5)
# příklad na not
print(not True)
print(not False)
print(not 4 == 4)

# operátor !=
print(4 != 5)  # 4 se nerovná 5, výsledek je True