# seznam = [100, 1, 3, 4, 2, 6, 7, 10]
seznam = [1, 2, 3, 4, 5]

# Varianta A
# serazeny_seznam = sorted(seznam)

# if seznam == serazeny_seznam:
#     print("Seznam je serazeny")
# else:
#     print("Seznam neni serazeny")


# Varianta B
serazeno = True
for i in range(len(seznam) - 1):
    if seznam[i] > seznam[i + 1]:
        serazeno = False

if serazeno:
    print("Seznam je serazeny")
else:
    print("Seznam neni serazeny")