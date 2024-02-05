#################### Operace s retězci ####################

############ Spojování řetězců ############

# spojení řetězců pomocí operátoru +
print("Ahoj"," ", "Karle")
print("Ahoj" + " " + "Karle")

# opakování řetězce pomocí operátoru *

print("abrakadabra" * 3)
print("abrakadabra" + "abrakadabra" + "abrakadabra")
print("+" * 30)

############ Indexování řetězců ############

# řetězce jsou indexovány od 0
# indexujeme pomocí hranatých závorek []

print("abrakadabra"[0])  # vypíše první znak
print("abrakadabra"[2])  # vypíše třetí znak
print("abrakadabra"[-1])  # vypíše poslední znak
print("abrakadabra"[-2])  # vypíše předposlední znak
print("abrakadabra"[len("abrakadabra") - 1])  # vypíše poslední znak

############## Ořezávání (slicing) řetězců ##############

# zobrazme prvních 5 znaků z řetězce "abrakadabra"
print("abrakadabra"[0:5])  # vypíše "abrak"
print("abrakadabra"[2:6])  # vypíše "raka"
# zobrazme prvních 5 znaků z řetězce "abrakadabra" 
print("abrakadabra"[:5])  # vypíše "abrak"
# zobrazme podlední 4 znaky z řetězce "abrakadabra"
print("abrakadabra"[-4:])  # vypíše "abra"

############## Změna velikosti písmen ##############

print("karel".upper())  # vypíše "KAREL"

print("Karel".lower())  # vypíše "karel"

print("petr".title())  # vypíše "Petr"
print("petr".capitalize())  # vypíše "Petr"