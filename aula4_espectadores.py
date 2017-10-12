otimo,bom,regular = 0,0,0

for i in range(5):
    opiniao = int(input("Opinião(3=ótimo/2=bom/1=regular): "))

    if opiniao == 3:
        otimo += 1
    elif opiniao == 2:
        bom += 1
    else:
        regular += 1

print("Ótimo: %d" % otimo)
print("Bom: %d" % bom)
print("Regular: %d" % regular)
