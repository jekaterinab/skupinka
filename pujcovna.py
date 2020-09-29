# soubor = open("C:\Users\Tomas\Desktop\skupinky\auta.txt")
import sys

print(f"Argumenty: {sys.argv}")

cesta = sys.argv[1]

soubor = open(cesta, encoding="utf8")
radky = [radek for radek in soubor]
soubor.close()

print(radky)



cisla = [radek.split(" ")[1].strip() for radek in radky if radek != "\n"]

print(cisla)

cisla = [float(cislo.replace(",", ".")) for cislo in cisla]

print(cisla)

soucet = sum(cisla)

print(f"Celkovy pocet kilometru je {soucet}.")