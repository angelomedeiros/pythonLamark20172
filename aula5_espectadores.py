opiniao = [int(input("Opinião(ótimo=1,Bom=2,Regular=3): ")) for i in range(3)]
print("Ótimo: {0}\nBom: {1}\nRegular: {2}" .format(opiniao.count(1),opiniao.count(2),opiniao.count(3)))
