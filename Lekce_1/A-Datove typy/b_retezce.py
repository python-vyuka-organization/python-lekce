######  Řetězce   #######
# Definice řetězce: Řetězce se definují jako posloupnost znaků
# uzavřených v jednoduchých nebo dvojitých uvozovkách (např. 'hello' nebo "world").cls


print("toto je retezec")



############# Uvozovky uvnitř řetězce #############

print("Toto je 'uvozovka' v uvozovkách")
print('Toto je řetězec s "uvozovkami" v uvozovkách')


# lze použít i tzv. escape sekvence

print("Toto je \"uvozovka\" v uvozovkách a tady je lomítko \\")

########### Přechod na nový řádek ###########
# Pokud chceme vypsat řetězec na více řádků, můžeme použít speciální znak \n

print("Toto je řetězec na prvním řádku\na toto je na druhém řádku")



########### Tabulátor ###########
# Pokud chceme vypsat tabulátor, můžeme použít speciální znak \t

print("Jméno\tPříjmení")
print("Jan\tNovák")
print("Petr\tSvoboda")


########### Print s více parametry ###########
print("Toto je", "řetězec", "s více parametry", "oddělenými mezerami", 45.8)

############# Funkce print() má také pojmenované parametry sep a end #############
print("Ahoj", end="")
print(" Karle")

print("Ahoj", "Karle", sep="*****************")


############ f-string ############
jmeno = "Karle"
retezec = f"Ahoj {jmeno}"
print(retezec)
