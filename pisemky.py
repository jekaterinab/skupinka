znamky = [1,2,3,2,4,3,5,5,1,2,3]

jednicky = 0
dvojky = 0
trojky = 0
ctyrky = 0
petky = 0

for znamka in znamky:
    if znamka == 1:
        # jednicky = jednicky + 1
        jednicky += 1
    elif znamka == 2:
        dvojky += 1
    elif znamka == 3:
        trojky += 1
    elif znamka == 4:
        ctyrky += 1
    else:
        petky += 1

print(f"Pocet jednicek: {jednicky}")
print(f"Pocet dvojek: {dvojky}")
print(f"Pocet trojek: {trojky}")
print(f"Pocet ctyrek: {ctyrky}")
print(f"Pocet petek: {petky}")