soubor = open("pasazeri.txt", encoding="utf8")
radky = [radek.strip() for radek in soubor]
soubor.close()

print(radky)

# radek = radky[0]  # a)
radek = " ".join(radky)  # b)

cesty = [cesta.strip() for cesta in radek.split(" ")]

tam_i_zpet = [cesta.split(",") for cesta in cesty]
print(tam_i_zpet)

tam = [int(cesta[0]) for cesta in tam_i_zpet]
zpet = [int(cesta[1]) for cesta in tam_i_zpet]
print(tam)
print(zpet)

celkem_tam = sum(tam)
celkem_zpet = sum(zpet)

print(f"Celkem jelo {celkem_tam} pasazeru tam a {celkem_zpet} pasazeru zpet.")