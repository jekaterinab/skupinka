with open("zustatky.txt", encoding="utf8") as f:
    radky = [radek.strip() for radek in f]

zustatky = [float(zustatek) for zustatek in radky]
# print(zustatky)


# a)
print("Vsechny zustatky")
for zustatek in zustatky:
    zustatek_s_urokem = zustatek * 1.025
    print(zustatek_s_urokem)

# a) chroustanim
# zustatky_s_uroky = [str(zustatek * 1.025) for zustatek in zustatky]
# print("\n".join(zustatky_s_uroky))

# b)
print("Nezaporne zustatky")
for zustatek in zustatky:
    if zustatek >= 0:
        zustatek_s_urokem = zustatek * 1.025
        print(zustatek_s_urokem)


# c)
print("Ocislovane zustatky")
cislo_radku = 0
for zustatek in zustatky:
    zustatek_s_urokem = zustatek * 1.025
    print(f"{cislo_radku}, {zustatek_s_urokem}")
    # cislo_radku = cislo_radku + 1
    cislo_radku += 1


# c) jinak
print("Ocislovane zustatky jinak")
for cislo_radku, zustatek in enumerate(zustatky):
    zustatek_s_urokem = zustatek * 1.025
    print(f"{cislo_radku + 1}, {zustatek_s_urokem}")