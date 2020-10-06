with open("spinavy_vstup.txt", encoding="utf8") as f:
    radky = [radek for radek in f]

print(radky)

# chci: ["Muj oblibeny film je Star Wars", "Je moc hezky", "Taky je fajn Lord Of The Rings", "Dobra kapela je Swallow the Sun", "HODNE DOBRE JE PULP FICTION"]

# Smazu volne misto na zacatku a na konci.
radky = [radek.strip() for radek in radky]
print(radky)

# Zahodim prazdne radky.
radky = [radek for radek in radky if radek != ""]
print(radky)

# Otazniky nahradim teckami.
radky = [radek.replace("?", ".") for radek in radky]
print(radky)

# Rozdelim vety do samostatnych textovych retezcu.
radky = [radek.split(".") for radek in radky]
print(radky)

# Vycistim vnitrni seznamy.
radky = [[veta.strip() for veta in radek if veta != ""] for radek in radky]
print(radky)

vysledek = []
print("for cyklus")
for radek in radky:
    print(radek)
    for veta in radek:
        print(f"\t{veta}")
        mala_veta = veta.capitalize() + "."
        print(f"\t{mala_veta}")
        vysledek.append(mala_veta)

print("Vysledek programu")
print(vysledek)

# -----------
# seznam = ["pes", "kocka", "medved"]
# for zvire in seznam:
#     print(zvire)

# print("\n".join(seznam))

# seznam = [1, 2, 3]
# print("\n".join([str(prvek) for prvek in seznam]))