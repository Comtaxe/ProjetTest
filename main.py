# Premiers test de python

# importation de la bibliothèque Cmath
import cmath

# ---------- Déclaration de variables ( Pas besoin de mettre des types)
a = 30
b = 20
stringInt = "34"
stringFloat = "30.5"
list1 = ["apple", "banana", "cherry"]
listeTuple = ("apple", "banana", "cherry")
dictList = {"name": "John", "age": 36}
boolean = True
myFirst_name = "Axel"  # pas de tirets ou de nombres dans un nom de variable
x = y = z = "Orange"  # meme valeur dans x, y et z
global myGlobalVar
myGlobalVar = "VariableGlobale"  # Déclaration d'une variable globale

# ---------- Tests de IF, ELSE, ELIF (Else if)

if a > b:
    print("If")
elif a < b:
    print("Elif")
else:
    print("Else")

# ---------- Examples de print
print(str(a) + "J'aime les frites") # str() : mettre une valeur en string
print(a + b)  # Calcul
print(stringInt + "j'aime les fruits")  # Mettre des + entre les variables et les chaînes
print(type(stringInt))  # c = "34" : type int
print(type(stringFloat))  # d = 20.5 : type float
print(type(list1))  # list1 est un tableau : type list
print(type(listeTuple))  # listeTuple est un tuple
print(type(dictList))  # dictList est une dict (Dictionnaire)
print(type(boolean))  # boolean est un booléen (Bool)

# ---------- Conversions de type
a = float(a)  # Transformer a (30) en float (30.0)
stringFloat = int(stringFloat)  # Transformer stringFloat (30.5) en int (30)'

# ---------- Strings
mystring = "Hello world"
print(len(mystring))  # Prendre le nombre de caractères
firstCaraString = mystring[0]  # Récupère le premier caractère
plusieursCarac = mystring[2:5]  # Récupère les caractères de l'index 2 à 4

stringWithSpace = " Y'a des espaces au début et à la fin "
stringWithoutSpace = stringWithSpace.strip()  # Texte sans les espaces au début et à la fin

stringMinuscules = "string que en minuscules"
stringMajuscules = stringMinuscules.upper()  # Mettre le string en maj

stringMaj = "STRING QUE EN MAJ"
stringMin = stringMaj.lower()  # Mettre le string en minuscules

stringToReplace = "String remplacer des lettres"
stringReplace = stringToReplace.replace("r", "x")  # Remplace les "e" par des "x"

#  ---------- Opérateurs






























